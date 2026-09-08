from pydantic import BaseModel, EmailStr, ConfigDict

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    name: str

class QuestionCreate(BaseModel):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str
    prize_level: int
    category: str = "General"

class QuestionOut(BaseModel):
    id: int
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    prize_level: int
    category: str
    model_config = ConfigDict(from_attributes=True)

class AnswerRequest(BaseModel):
    game_id: int
    question_id: int
    answer: str

class LifelineRequest(BaseModel):
    game_id: int
    question_id: int
    lifeline: str
