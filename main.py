from typing import List, Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API crash course",
    description="Fast API with SQLAlchemy",
    version="0.0.1",
    contact={
        "name": "Paulo",
        "email": "paulopma@hotmail.com",
    },
    license_info={
        "name": "NASA"
    }
)

users = []

class User(BaseModel): 
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "user created"

@app.get("/users/{id}")
async def get_user_by_id(
    id: int = Path(..., description="The ID of the user", gt=0),
    q: str = Query("lol", max_length=5)
):
    return {"user": users[id], "query": q}