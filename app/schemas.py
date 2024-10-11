from pydantic import BaseModel, Field
from typing import List, Optional


class TrainingRequest(BaseModel):
    question: str = Field(..., example="Training 1")
