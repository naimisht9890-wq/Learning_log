from fastapi import FastAPI

app = FastAPI()

# Query parameter
"""
a query parameter is an optional value added to the end of a url after a ?.
it often controls how results are filtered or displayed"""

@app.get("/name")
def get_name(name:str=None):
    return{"name":name}

# you can combine path and query parameters:

@app.get("/users/{user_id}/items")
def list_user_items(user_id:int,limit:int=10):
    return{"user_id":user_id,"limit":limit}

@app.get("/items")
def get_users(name:str=None,price:int=0):
    return{
        "name":name,
        "price":price
    }