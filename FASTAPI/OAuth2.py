from fastapi import FastAPI,HTTPException,Depends
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import datetime,timedelta,timezone
from passlib.context import CryptContext

app=FastAPI()

#jwt config
secret_key="mysecret"
algorithm="HS256"
access_token_epire_mintues=30

#password hashing setup
pwd_context=CryptContext(schemes=["bcrypt"])

#OauthSetup
oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")

#Dummy user DB
fake_user_db={
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
    }
}

#hash password
def hash_password(password:str):
    return pwd_context.hash(password)

#varify password
def verify_password(plain_password,hased_password):
    return pwd_context.verify(plain_password,hased_password)

#create token
def create_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    token=jwt.encode(to_encode,secret_key,algorithm=algorithm)

    return token

#login api
@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user=fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid username or password"
        )
    access_token=create_token({"sub":form_data.username})

    return{
        "access_token":access_token,
        "token_type":"bearer"
    }

#token verfiy
def verify_token(token:str=Depends(oauth2_schema)):
    try:
        payload=jwt.decode(token,secret_key,algorithms=[algorithm])
        username:str=payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        return username
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

#protected route
@app.get("/protected")
def protected_route(username:str=Depends(verify_token)):
    return{
        "message":"Hello you have access to this protected route!",
        "user":username
    }