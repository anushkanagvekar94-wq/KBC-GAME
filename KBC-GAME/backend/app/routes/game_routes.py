from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Game, GameAnswer, Question, User
from ..schemas import AnswerRequest, LifelineRequest
from ..auth import current_user
import random

PRIZES = [2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]

router = APIRouter(prefix="/api/game", tags=["Game"])

@router.post("/start")
def start_game(db: Session = Depends(get_db), user: User = Depends(current_user)):
    game = Game(user_id=user.id)
    db.add(game); db.commit(); db.refresh(game)
    return {"game_id": game.id, "prizes": PRIZES}

@router.post("/answer")
def answer(data: AnswerRequest, db: Session = Depends(get_db), user: User = Depends(current_user)):
    game = db.get(Game, data.game_id)
    q = db.get(Question, data.question_id)
    if not game or game.user_id != user.id:
        raise HTTPException(404, "Game not found")
    if game.status != "playing":
        raise HTTPException(400, "Game is already finished")
    if data.answer not in ["A","B","C","D"]:
        raise HTTPException(400, "Invalid answer")
    correct = data.answer == q.correct_answer
    game.questions_answered += 1
    if correct:
        game.score += 1
        game.prize = PRIZES[min(q.prize_level-1, len(PRIZES)-1)]
    else:
        game.status = "lost"
    db.add(GameAnswer(game_id=game.id, question_id=q.id, selected_answer=data.answer, correct=correct))
    if game.questions_answered >= 15 and correct:
        game.status = "won"
    db.commit()
    return {"correct": correct, "correct_answer": q.correct_answer, "prize": game.prize, "status": game.status, "score": game.score}

@router.post("/quit")
def quit_game(game_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    game = db.get(Game, game_id)
    if not game or game.user_id != user.id: raise HTTPException(404, "Game not found")
    game.status = "quit"; db.commit()
    return {"prize": game.prize, "status": game.status}

@router.post("/lifeline")
def lifeline(data: LifelineRequest, db: Session = Depends(get_db), user: User = Depends(current_user)):
    game = db.get(Game, data.game_id); q = db.get(Question, data.question_id)
    if not game or game.user_id != user.id: raise HTTPException(404, "Game not found")
    if data.lifeline == "5050":
        wrong = [x for x in ["A","B","C","D"] if x != q.correct_answer]
        random.shuffle(wrong)
        return {"remove": wrong[:2]}
    if data.lifeline == "audience":
        options = ["A","B","C","D"]
        values = {x: random.randint(5,25) for x in options}
        values[q.correct_answer] += 45
        total = sum(values.values())
        return {"poll": {x: round(values[x]*100/total) for x in options}}
    if data.lifeline == "expert":
        return {"answer": q.correct_answer}
    raise HTTPException(400, "Unknown lifeline")
