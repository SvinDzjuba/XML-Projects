from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'root'
password = ''
host = 'localhost'
port = 3306
database = 'library_db'

# Подключение к базе данных
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"      # Создает путь соединения
engine = create_engine(SQLALCHEMY_DATABASE_URL)   # Engine - это класс, который предоставляет подключение к базе данных.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)       # это фабрика, которая упрощает жизнь: вместо того, чтобы каждый раз указывать список аргументов у сессии, 
                                                                                # его достаточно один раз указать в sessionmaker
Base = declarative_base()     #  это функция, которая возвращает базовый класс, и сущности будут наследоваться от него.