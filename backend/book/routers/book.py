from fastapi import APIRouter,Depends,Response,status,HTTPException
from .. import schemas,models,database
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(
    prefix="/book",
    tags=["Book"]
)

@router.get("/all")
def read_all_books(db:Session = Depends(database.get_db)):
    books = db.query(models.Book).all()
    return books
    
@router.get("/{id}")
def read_book(id:int,response:Response,db:Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"This blog with id:{id} is not created")    
    return book

@router.post("/create" ,status_code=status.HTTP_201_CREATED)
def create_book(request: schemas.Book,db:Session = Depends(get_db)):
    new_book = models.Book(title = request.title ,description = request.description)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.put("/{id}")
def update_book(id: int, request: schemas.Book, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"This book with id:{id} is not present")
    book.title = request.title
    book.description = request.description
    db.commit()
    db.refresh(book)
    return Response(status_code=status.HTTP_200_OK)

@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_book(id:int,db:Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"This blog with id:{id} is not present")
    id = book.id
    db.delete(book)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)
