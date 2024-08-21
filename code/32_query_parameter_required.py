from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, required: str):
    item = {"item_id": item_id, "required": required}
    return item


# http://127.0.0.1:8000/items/intel - Gives error
# http://127.0.0.1:8000/items/intel?required=cpu - Works