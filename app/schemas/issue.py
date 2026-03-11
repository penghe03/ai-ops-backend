from pydantic import BaseModel
from typing import Optional

class Issue(BaseModel):
    title: str
    description: str
    severity: str
    status: Optional[str] = "open"  # new field, default = "open"