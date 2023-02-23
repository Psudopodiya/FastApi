from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from .. import models,schemas,database
from ..database import get_db
from passlib.context import CryptContext
from typing import List


router = APIRouter(
    prefix='/author',
    tags=['Authors']
)

pwd_context = CryptContext(schemes=['bcrypt'],deprecated = 'auto')

@router.get('/')
def read_user(db: Session = Depends(get_db)):
    author = db.query(models.Author).all()
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No Data found")
    return author

@router.get('/{id}')
def read_user(id:int,db:Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == id).first()
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No Data found")
    return author

@router.post('/create',status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.Author, db: Session = Depends(get_db)):
    new_author = models.Author(first_name = request.first_name,last_name = request.last_name,date_of_birth = request.date_of_birth)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@router.delete("/{id}")
def delete_user(id:int,db:Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == id).first()
    if not author:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"This user with id:{id} is not created")
    db.delete(author)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)

@router.get("/{id}")
def read_user(id:int,db:Session = Depends(get_db)):
    return 0