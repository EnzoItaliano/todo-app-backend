from pydantic import BaseModel
from typing import Optional

# Common properties for both creating and reading
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

    class Config:
        from_attributes = True

# Properties required when creating a task (POST)
class TaskCreate(TaskBase):
    pass

# Properties returned to the client (includes the ID)
class Task(TaskBase):
    id: int