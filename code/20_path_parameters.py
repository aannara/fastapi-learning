from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/another_items/{item_id}")
async def read_another_item(item_id: int):
    return {"item_id": item_id}