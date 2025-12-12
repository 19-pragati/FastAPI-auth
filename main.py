# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from passlib.context import CryptContext

app = FastAPI(title="FastAPI Auth Demo")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
users_db = {}  # Temporary in-memory storage (use a real DB for production)


class User(BaseModel):
    username: str
    password: str


@app.get("/")
def docs_redirect():
    """
    Redirect root to the interactive docs so testers find the API quickly.
    """
    return RedirectResponse(url="/docs")


@app.post("/signup", status_code=201)
def signup(user: User):
    """
    Create a new user. Password is hashed (bcrypt) before storing.
    """
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = pwd_context.hash(user.password)
    users_db[user.username] = hashed_password
    return {"message": "User created successfully"}


@app.post("/login")
def login(user: User):
    """
    Verify username and password against the in-memory store.
    """
    if user.username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    if not pwd_context.verify(user.password, users_db[user.username]):
        raise HTTPException(status_code=401, detail="Incorrect password")

    # In real apps: return JWT or session token here
    return {"message": "Login successful"}
