from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This defines how data should look
class Item(BaseModel):
    name: str
    description: str

items = []

@app.get("/")
def home():
    return {"message": "Lostify API Running"}

# Now we accept JSON body
@app.post("/add_item")
def add_item(item: Item):
    items.append(item)
    return {"message": "Item added", "item": item}

@app.get("/items")
def get_items():
    return items