from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Question(Base):
    __tablename__ = "questions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    question: Mapped[str] = mapped_column(Text)
    option_a: Mapped[str] = mapped_column(String(255))
    option_b: Mapped[str] = mapped_column(String(255))
    option_c: Mapped[str] = mapped_column(String(255))
    option_d: Mapped[str] = mapped_column(String(255))
    correct_answer: Mapped[str] = mapped_column(String(1))
    prize_level: Mapped[int] = mapped_column(Integer)
    category: Mapped[str] = mapped_column(String(100), default="General")

class Game(Base):
    __tablename__ = "games"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    score: Mapped[int] = mapped_column(Integer, default=0)
    prize: Mapped[int] = mapped_column(Integer, default=0)
    questions_answered: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[str] = mapped_column(String(20), default="playing")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class GameAnswer(Base):
    __tablename__ = "game_answers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"))
    selected_answer: Mapped[str] = mapped_column(String(1))
    correct: Mapped[bool] = mapped_column(Boolean)
    answered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
