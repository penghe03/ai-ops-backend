from fastapi import FastAPI
from app.routers import issues

# from app.schemas.issue import Issue
# from app.db.session import engine, SessionLocal
# from app.db.models import Base, IssueModel

# from fastapi import Query
# from typing import List, Optional
# from app.schemas.issue import Issue

# from fastapi import HTTPException

# from app.services.ai import generate_suggestion

# import os
# import openai

# AI Suggestion
# openai.api_key = os.getenv("OPENAI_API_KEY")
# def get_ai_suggestion(title: str, description: str, severity: str) -> str:
#     prompt = f"Suggest a priority action for this issue:\nTitle: {title}\nDescription: {description}\nSeverity: {severity}"

#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are an expert IT engineer."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=30
#     )

#     return response.choices[0].message.content.strip()

app = FastAPI()
# Base.metadata.create_all(bind=engine)

app.include_router(issues.router)

# @app.get("/health")
# def health():
#     return {"status": "ok"}

# @app.get("/issues", response_model=List[Issue])
# def list_issues(severity: Optional[str] = Query(None, description="Filter by severity")):
#     db = SessionLocal()
#     query = db.query(IssueModel)
#     if severity:
#         query = query.filter(IssueModel.severity == severity)
#     issues = query.all()
#     db.close()
#     return issues

# @app.post("/issues")
# def create_issue(issue: Issue):
#     db = SessionLocal()

#     # suggestion = get_ai_suggestion(issue.title, issue.description, issue.severity)
#     # Temporary placeholder for AI suggestion
#     # suggestion = "Review and prioritize based on severity"
#     suggestion = generate_suggestion(issue.title, issue.description)

#     db_issue = IssueModel(
#         title=issue.title,
#         description=issue.description,
#         severity=issue.severity,
#         status="open",
#         suggested_fix=suggestion
#     )

#     db.add(db_issue)
#     db.commit()
#     db.refresh(db_issue)

#     return {
#         "id": db_issue.id,
#         "title": db_issue.title,
#         "description": db_issue.description,
#         "severity": db_issue.severity,
#         # "ai_suggestion": suggestion,
#         "suggested_fix": db_issue.suggested_fix
#     }

# @app.patch("/issues/{issue_id}")
# def update_issue_status(issue_id: int, status: str):
#     db = SessionLocal()
#     issue = db.query(IssueModel).filter(IssueModel.id == issue_id).first()
#     if not issue:
#         db.close()
#         raise HTTPException(status_code=404, detail="Issue not found")
#     issue.status = status
#     db.commit()
#     db.refresh(issue)
#     db.close()
#     return {
#         "id": issue.id,
#         "title": issue.title,
#         "description": issue.description,
#         "severity": issue.severity,
#         "status": issue.status
#     }


@app.get("/")
def root():
    return {"message": "AI Ops Backend is running"}
