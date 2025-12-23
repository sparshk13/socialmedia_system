from fastapi import FastAPI
from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import select

from database.models import Users
from database.database import get_db

app = FastAPI()

class UserReq(BaseModel):
    user_id: str
    name: str
    username: str

@app.get("/")
def home(db: Session = Depends(get_db)):
    # all_user = db.query(Users).filter
    user = select(Users).where(Users.c.name.startswith("Vi"))
    return {"message": "hello world"}

@app.get("/hello")
def hello_world():
    return {"message": "hello world from page 2"}

@app.post("/sending_data")
def data_func(data: UserReq, db: Session = Depends(get_db)):
    print(data.name)
    
    new_user = Users(user_id=data.user_id, name=data.name, username=data.username)
    # sandy = Users(
    #     user_id="100",
    #     name="Sandy",
    #     username="sand@123"
    # )
    
    # db.add_all([new_user, sandy])
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": f"Got user Info for {data.name} with user_id {data.user_id}"}