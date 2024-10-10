from pydantic import BaseModel, Field
from typing import List, Optional


class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None

    class Config:
        orm_mode = True
