from sqlalchemy import Column, Integer, String
from app.db.session import Base

class IssueModel(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    status = Column(String, default="open")  # new column
    suggested_fix = Column(String)  # for AI suggested fix, added for day 6