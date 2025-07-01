from fastapi import FastAPI, Request
from typing import Union
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./sql_app.db"

# instance class เริ่มต้นสำหรับ engine, SessionLocal และ Base
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items")
def create_item(item: Item):
    print(item.name, item.price)
    return {"request body": item}

@app.put("/items/{item_id}")
def edit_item(item_id: int, item: Item):
    return {"id": item_id, "request body": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"massage": f"Item {item_id} deleted"}