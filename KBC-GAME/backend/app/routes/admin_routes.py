from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Question
from ..schemas import QuestionCreate, QuestionOut
from ..auth import current_user

router = APIRouter(prefix="/api/admin", tags=["Admin"])

# Demo admin protection: replace this with a real role column in production.
def admin_only(user=Depends(current_user)):
    if user.email != "admin@kbc.com":
        from fastapi import HTTPException
        raise HTTPException(403, "Admin access required")
    return user

@router.post("/questions", response_model=QuestionOut)
def create_question(data: QuestionCreate, db: Session = Depends(get_db), _=Depends(admin_only)):
    q = Question(**data.model_dump())
    db.add(q); db.commit(); db.refresh(q)
    return q

@router.delete("/questions/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db), _=Depends(admin_only)):
    q = db.get(Question, question_id)
    if not q:
        from fastapi import HTTPException
        raise HTTPException(404, "Question not found")
    db.delete(q); db.commit()
    return {"message":"Question deleted"}
