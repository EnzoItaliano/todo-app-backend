from sqlalchemy import Column, Integer, String
from .database import Base

# We name this TaskItem to match your Sequelize define("TaskItem", ...)
class TaskItem(Base):
    __tablename__ = "task_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))