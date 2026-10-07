from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    
@app.post("/create-user")
def create_user(user:str,age:int):
    return {
        "name": user,
        "age": age
    }

@app.post("/create-user-dict")
def create_user_dict(user: dict):
    return {
        "message":"user created",
        "data":user
    }

@app.post("/create-user-validation")
def create_user_dict(user:User):
    return {
        "message":"user created",
        "data":user
    }