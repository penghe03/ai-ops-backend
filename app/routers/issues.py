from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Literal
from app.db.session import SessionLocal
from app.db.models import IssueModel
from app.schemas.issue import Issue, IssueCreate
from app.services.ai import generate_suggestion

from app.services.issue_service import (
    create_issue,
    get_issues,
    update_issue_status
)

router = APIRouter()

@router.post("/issues", response_model=Issue)
def create_issue_endpoint(issue: IssueCreate):
    db = SessionLocal()
    # suggestion = generate_suggestion(issue.title, issue.description)

    # db_issue = IssueModel(
    #     title=issue.title,
    #     description=issue.description,
    #     severity=issue.severity,
    #     status=issue.status or "open",
    #     suggested_fix=suggestion
    # )

    db_issue = create_issue(
        db,
        issue.title,
        issue.description,
        issue.severity,
        issue.status
    )

    # db.add(db_issue)
    # db.commit()
    # db.refresh(db_issue)
    db.close()
    return db_issue

@router.get("/issues", response_model=list[Issue])
def list_issues(severity: str = None):
    db = SessionLocal()
    # query = db.query(IssueModel)
    # if severity:
    #     query = query.filter(IssueModel.severity == severity)
    # issues = query.all()
    issues = get_issues(db, severity)
    db.close()
    return issues

@router.patch("/issues/{issue_id}", response_model=Issue)
def update_issue(issue_id: int, status: Literal["open", "in-progress", "resolved"]):
    db = SessionLocal()
    # issue = db.query(IssueModel).filter(IssueModel.id == issue_id).first()
    # issue.status = status
    issue = update_issue_status(db, issue_id, status)
    if not issue:
        db.close()
        raise HTTPException(status_code=404, detail="Issue not found")
    # db.commit()
    # db.refresh(issue)
    db.close()
    return issue