from typing import Union, Any

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Person(BaseModel):
    first_name: str
    last_name: str
    dob: str


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict[str, Any]:
    return {"item_id": item_id, "q": q}