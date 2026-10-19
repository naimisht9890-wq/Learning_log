import time
import asyncio
from fastapi import FastAPI


app = FastAPI()

#syn code

# def task():
#     time.sleep(3)
#     return "Done"

'''asyn method'''
# async def taks():
#     await asyncio.sleep(3)
#     return "Done"

@app.get("/")
async def home():
    await asyncio.sleep(10)
    return{
        "message":"Async API"
    }