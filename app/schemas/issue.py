from pydantic import BaseModel
from typing import Optional, Literal

# Input schema — for POST request
class IssueCreate(BaseModel):
    title: str
    description: str
    severity: Literal["low", "medium", "high"]
    status: Optional[Literal["open", "in-progress", "resolved"]] = "open"

# Output schema — for response
class Issue(BaseModel):
    title: str
    description: str
    severity: str
    status: str
    suggested_fix: Optional[str] = None

    class Config:
        orm_mode = True  # important for SQLAlchemy models