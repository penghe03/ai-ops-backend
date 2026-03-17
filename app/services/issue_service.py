from app.db.models import IssueModel
from app.services.ai import generate_suggestion

def create_issue(db, title, description, severity, status="open"):
    suggestion = generate_suggestion(title, description)

    db_issue = IssueModel(
        title=title,
        description=description,
        severity=severity,
        status=status,
        suggested_fix=suggestion
    )

    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue


def get_issues(db, severity=None):
    query = db.query(IssueModel)
    if severity:
        query = query.filter(IssueModel.severity == severity)
    return query.all()


def update_issue_status(db, issue_id, status):
    issue = db.query(IssueModel).filter(IssueModel.id == issue_id).first()
    if not issue:
        return None

    issue.status = status
    db.commit()
    db.refresh(issue)
    return issue