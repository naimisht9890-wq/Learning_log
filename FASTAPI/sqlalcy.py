from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from fastapi import FastAPI,Depends,HTTPException

app=FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

sessionLocal=sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__= "todos"

    id = Column(Integer,primary_key=True,index=True)
    title= Column(String)
    complete=Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(db: Session=Depends(get_db)):
    return{
        "message":"DB_connected fine"
    }

@app.post("/todos")
def create_todo(title:str,db:Session=Depends(get_db)):
    todo=Todo(title=title,complete="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "data":todo
    }

# read all data
@app.get("/todos")
def get_todos(db:Session=Depends(get_db)):
    todos=db.query(Todo).all()

    return{
        "Total":len(todos),
        "data":todos
    }

# read data based on id
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,detail="todo not found")
    return todo

#update
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo:
            raise HTTPException(status_code=404,detail="todo not found")

    todo.title=title
    db.commit()

    return{
        "message":"Todo Updated",
        "data":todo
    }