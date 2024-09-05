from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str
    dir: Optional[str] = None
    createdAt: datetime = Field(default_factory=datetime.now)
