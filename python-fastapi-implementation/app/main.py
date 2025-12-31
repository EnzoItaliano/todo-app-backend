# app/main.py
import sys
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.authy import RoleChecker, get_password_hash, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import status


# Initialize the FastAPI app
app = FastAPI(title="To-Do API - Python Edition")

# Create database tables (Equivalent to db.sequelize.sync in your Node version)
if __name__ == "__main__" or "pytest" not in sys.modules:
    models.Base.metadata.create_all(bind=database.engine)

# Registration Endpoint
@app.post("/api/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Check if user already exists
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Hash the password and save
    hashed_pwd = get_password_hash(user.password)
    new_user = models.User(
        username=user.username, 
        hashed_password=hashed_pwd, 
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Login / Token Generation Endpoint
@app.post("/api/token", response_model=schemas.Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(database.get_db)
):
    # Authenticate user
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create JWT including the 'role' claim for RBAC
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role}
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Only users with "admin" role can access this
allow_admin = RoleChecker(["admin"])

@app.delete("/api/tasks/{task_id}", dependencies=[Depends(allow_admin)])
def delete_task(task_id: int):
    return {"message": f"Task {task_id} deleted by Admin"}

# Both users and admins can access this
allow_any_user = RoleChecker(["user", "admin"])


@app.post("/api/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    """
    Creates a new task. Demonstrates Pydantic validation.
    """
    db_task = models.TaskItem(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/api/tasks")
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    """
    Retrieves tasks with pagination, showing a more advanced feature than the Node version.
    """
    return db.query(models.TaskItem).offset(skip).limit(limit).all()