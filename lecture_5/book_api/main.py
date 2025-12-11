from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_

from models import Base, Book
from database import engine, session_local
from schemas import BookResponse, BookCreate, BookUpdate

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post("/books/", response_model=BookResponse)
async def create_book(book: BookCreate, db: Session = Depends(get_db)) -> BookResponse:
    """add a new book"""
    db_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=List[BookResponse])
async def get_books(db: Session = Depends(get_db)):
    """get all books"""
    return db.query(Book).all()


@app.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    """delete a book by ID"""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail=f"Book {book_id} not found")
    db.delete(book)
    db.commit()
    return {"message": f"Book {book_id} deleted"}


@app.put("/books/{book_id}", response_model=BookResponse)
async def update_book(book_id: int, book_upd: BookUpdate, db: Session = Depends(get_db)) -> BookResponse:
    """update book details"""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail=f"Book {book_id} not found")
    title = book_upd.title
    author = book_upd.author
    year = book_upd.year
    if title:
        book.title = title
    if author:
        book.author = author
    if year:
        book.year = year
    db.commit()
    db.refresh(book)
    return book


@app.get("/books/search/", response_model=List[BookResponse])
async def search_book(
        title: Optional[str] = Query(None, description="title"),
        author: Optional[str] = Query(None, description="author"),
        year: Optional[int] = Query(None, description="year"),
        db: Session = Depends(get_db)):
    """search books by title, author, or year"""
    books = db.query(Book)
    filters = []
    if title:
        filters.append(Book.title.ilike(f"%{title}%"))
    if author:
        filters.append(Book.author.ilike(f"%{author}%"))
    if year is not None:
        filters.append(Book.year == year)
    if filters:
        books = books.filter(or_(*filters))
    return books.all()
