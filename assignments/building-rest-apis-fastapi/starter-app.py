from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Items API - FastAPI Starter")


class Item(BaseModel):
    id: int
    name: str
    price: float


# In-memory store: id -> Item
store: Dict[int, Item] = {}


@app.get("/items/")
def list_items():
    return list(store.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = store.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items/", status_code=201)
def create_item(item: Item):
    if item.id in store:
        raise HTTPException(status_code=400, detail="Item with this id already exists")
    store[item.id] = item
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated: Item):
    if item_id != updated.id:
        raise HTTPException(status_code=400, detail="ID in path and body must match")
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    store[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    del store[item_id]
    return None
