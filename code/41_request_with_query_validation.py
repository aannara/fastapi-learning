from typing import Union, List

from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[Union[str, None], Query(min_length=3, max_length=5)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Query list
# @app.get("/items/")
# async def read_items(q: Annotated[Union[List[str], None], Query()] = ["foo", "bar"]):
#     query_items = {"q": q}
#     return query_items