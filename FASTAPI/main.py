from fastapi import FastAPI

app = FastAPI()

# home route
@app.get("/")
def home():
    return{"message":"welcome to my API"}

# about route
@app.get("/about")
def about():
    return{"message":"this is about page"}

# user route
@app.get("/users")
def users():
    return{
        "users":['mohit','rohit','amit']
        }