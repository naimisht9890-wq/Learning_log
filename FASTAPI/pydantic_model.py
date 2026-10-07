from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age:int
    email:str

@app.post("/create_user")
def create_user(user:User):
    return{
        "message":"user created",
        "data":user
    }

# Nested Model

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/create_user_nested")
def create_user(user:User):
    return{
        "message":"user created",
        "data":user
    }