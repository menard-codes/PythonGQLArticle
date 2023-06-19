from sqlalchemy import Column, String, Integer, Boolean

from .database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    content = Column(String)
    is_done = Column(Boolean, default=False)

    def __repr__(self):
        return f'Task(id={self.id}, content={self.content}, is_done={self.is_done})'
