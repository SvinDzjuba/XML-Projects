from unicodedata import category
from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


def get_db():
    try:
        db = SessionLocal()         # переменной придаются SessionLocal классы из базы
        yield db            # Возращает базу
    finally:
        db.close()

@app.get("/categories/")
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)     # загружает категории из базы на fastApi сервер через функцию из файла crud.py

@app.post("/categories/", response_model=schemas.Category)
def add_category(category: schemas.Category, db: Session = Depends(get_db)):
    return crud.create_category(db, category)    # добавляет категорию в базу через json из fastApi



# My methods


# ВСЕ ДЕЙСТВИЯ С АВТОРАМИ


@app.post("/author/", response_model=schemas.Author)
def add_author(author: schemas.Author, db: Session = Depends(get_db)):
    return crud.create_category(db, author)

@app.delete('/author/{author_id}')
def delete_author(author_id: str, db: Session = Depends(get_db)):
    return crud.delete_author(db, author_id)

@app.get("/authors/")
def read_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)



# ВСЕ ДЕЙСТВИЯ С КНИГАМИ


@app.post("/book/", response_model=schemas.Book)
def add_book(author: schemas.Book, db: Session = Depends(get_db)):
    return crud.create_category(db, author)

@app.delete('/book/{book_id}')
def delete_book(book_id: str, db: Session = Depends(get_db)):
    return crud.delete_book(db, book_id)

@app.get("/books/")
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)



# ВСЕ ДЕЙСТВИЯ С КАТЕГОРИЯМИ


@app.delete('/category/{category_id}')
def delete_category(category_id: str, db: Session = Depends(get_db)):
    return crud.delete_category(db, category_id)