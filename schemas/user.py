import typing
from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id : Optional[str]
    name : str
    quantity : int
    price : int

