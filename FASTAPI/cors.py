from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

# allowed origin(front-end url)
origin=[
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin, #allowed FE
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return{
        "message":"CORS ENABLE"
    }