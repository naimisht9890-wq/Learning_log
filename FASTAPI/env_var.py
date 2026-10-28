from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import os
# from dotenv import load_dotenv
from config import settings

app = FastAPI()
# load_dotenv()

# allowed origins(frontend url)
origins=settings.origins
# secret_key=os.getenv("mysecret")
# db_url=os.getenv("db_url")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return{
        "message":"CORS ENABLE"
    }