from fastapi import FastAPI

app= FastAPI()

'''A path parameter is a value written directly into a url's path. it lets
one route  handle many similar urls'''

@ app.get("/item/{item_id}")
def get_item(item_id:int):
    return{"item_id":item_id}

'''
1)  /item/{item_id} : is the route. {item_id} marks the part that can change.

2) item_id : in the function receives the value from the url

3) :int  : tells fastapi to convert that value to an integer
'''