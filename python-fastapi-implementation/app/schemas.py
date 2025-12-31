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

# User Schemas
class UserBase(BaseModel):
    username: str
    role: Optional[str] = "user" # Default role is 'user'

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str