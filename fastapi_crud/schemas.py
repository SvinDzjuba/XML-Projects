from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Category(BaseModel):
    id: Optional[int]
    name: str
    class Config:
        orm_mode = True


class Author(BaseModel):
    id: Optional[int]
    name: str
    class Config:
        orm_mode = True


class Book(BaseModel):
    id: Optional[int]
    name: str
    isbn: str
    pageCount: int
    shortDescription: Optional[str]
    longDescription: Optional[str]
    pubDate: datetime
    class Config:
        orm_mode = True