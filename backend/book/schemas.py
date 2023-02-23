from pydantic import BaseModel
from datetime import date, datetime
class Book(BaseModel):
    title: str
    description: str

class Author(BaseModel):
    first_name: str
    last_name: str
    date_of_birth : date
