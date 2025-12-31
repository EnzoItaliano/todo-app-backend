import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app

# 1. SETUP: Create an in-memory database for isolated testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. FIXTURE: Override the database dependency
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# 3. THE TESTS

def test_register_user():
    """Test user registration logic"""
    response = client.post(
        "/api/register",
        json={"username": "testuser", "password": "securepassword123", "role": "user"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_login_and_access_protected_route():
    """Test the full flow: Register -> Login -> Get JWT -> Access API"""
    # Register
    client.post("/api/register", json={"username": "admin", "password": "adminpassword", "role": "admin"})
    
    # Login to get token
    login_response = client.post(
        "/api/token",
        data={"username": "admin", "password": "adminpassword"}
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Access protected route
    response = client.get("/api/tasks", headers=headers)
    assert response.status_code == 200

def test_rbac_restriction():
    """Test that a 'user' cannot access 'admin' routes"""
    # Register and login as a regular user
    client.post("/api/register", json={"username": "regular", "password": "password", "role": "user"})
    login_response = client.post("/api/token", data={"username": "regular", "password": "password"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Try to delete a task (Admin only)
    response = client.delete("/api/tasks/1", headers=headers)
    assert response.status_code == 403  # Forbidden
    assert response.json()["detail"] == "You do not have enough permissions"