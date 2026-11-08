from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class UserInput(BaseModel):
    username: str
    user_id: int

app = FastAPI()
users: dict[int, str] = {}


@app.post("/users")
def create_user(user: UserInput):
    users[user.user_id] = user.username
    return {"id": user.user_id, "username": user.username}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    username = users.get(user_id)
    if username is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, "username": username}
