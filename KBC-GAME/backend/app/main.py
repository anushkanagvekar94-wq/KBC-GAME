from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import auth_routes, question_routes, game_routes, admin_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="KBC Quiz API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)
app.include_router(question_routes.router)
app.include_router(game_routes.router)
app.include_router(admin_routes.router)

@app.get("/")
def root():
    return {"message": "KBC Quiz API is running"}
