# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

# Initialize the FastAPI app
app = FastAPI(title="To-Do API - Python Edition")

# Create database tables (Equivalent to db.sequelize.sync in your Node version)
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get the DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    Creates a new task. Demonstrates Pydantic validation.
    """
    db_task = models.TaskItem(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/api/tasks")
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieves tasks with pagination, showing a more advanced feature than the Node version.
    """
    return db.query(models.TaskItem).offset(skip).limit(limit).all()