from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
import schemas

def get_category_by_id(db: Session, category_id: int):      # Функиця, которая селектит из базы данных категорию по её айди
    return db.query(models.Category).get(category_id)

def get_categories(db:Session):       # Функиця, которая селектит из базы данных все её категории
    return db.query(models.Category).all()

def get_book_by_id(db: Session, book_id: int):       # Функиця, которая селектит из базы данных книгу по её айди
    return db.query(models.Book).get(book_id) 

def get_book_by_title(db: Session, title: str):           # Функиця, которая селектит из базы данных книгу по её названию
    return db.query(models.Book).filter(models.Book.title == title).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):        # Функиця, которая селектит из базы данных 100 книг
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_category(db: Session, category: schemas.Category):      # Функиця, которая создает в базе данных категорию
    print(category.name)
    new_category = models.Category(name = category.name)      # Переменная, которая создает категорию по её названию
    db.add(new_category)       # Добавляет категорию в базу
    db.commit()           # Сохраняет изменения
    return new_category




# My functions


# ВСЕ ДЕЙСТВИЯ С АВТОРОМ

def get_author_by_id(db: Session, author_id: int):
    return db.query(models.Author).get(author_id)

def get_authors(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Author).offset(skip).limit(limit).all()

def delete_author(db: Session, id):
    try:
        db.delete(get_author_by_id(db, id))
        db.commit()
        return "Автор удален!"
    except: return "Не удалось удалить автора!"

def create_author(db: Session, author: schemas.Author):
    new_author = models.Category(name = author.name)
    db.add(new_author)
    db.commit()
    return new_author


# ВСЕ ДЕЙСТВИЯ С КАТЕГОРИЯМИ

def delete_category(db: Session, id):
    try:
        db.delete(get_category_by_id(db, id))
        db.commit()
        return "Категория удалена!"
    except: 
        return "Не удалось удалить категорию!"


# ВСЕ ДЕЙСТВИЯ С КНИГОЙ

def delete_book(db: Session, id):
    try:
        db.delete(get_book_by_id(db, id))
        db.commit()
        return "Книга удалена!"
    except: return "Не удалось удалить книгу!"

def create_book(db: Session, book: schemas.Book):
    new_book = models.Book(name = book.name, 
    isbn = book.isbn, 
    pageCount = book.pageCount, 
    shortDescription = book.shortDescription, 
    longDescription = book.longDescription, 
    pubDate = book.pubDate,)
    
    db.add(new_book)
    db.commit()
    return new_book

    # isbn: str
    # pageCount: int
    # shortDescription: Optional[str]
    # longDescription: Optional[str]
    # pubDate: datetime