from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Question
from ..schemas import QuestionOut

router = APIRouter(prefix="/api/questions", tags=["Questions"])

@router.get("", response_model=list[QuestionOut])
def get_questions(db: Session = Depends(get_db)):
    return db.query(Question).order_by(Question.prize_level).all()
