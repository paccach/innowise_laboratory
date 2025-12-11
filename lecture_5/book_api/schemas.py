from typing import Optional
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
