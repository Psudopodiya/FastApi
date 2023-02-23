from .database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Date
from sqlalchemy.orm import relationship

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    lastname_name = Column(String(255))
    date_of_birth = Column(Date)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    image_url = Column(String(255))

