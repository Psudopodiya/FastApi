from fastapi import FastAPI
from . import models
from .database import engine,SessionLocal
from .routers import author,book


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(book.router)
app.include_router(author.router)

# DEFAULT ROUTES

@app.get("/",tags=['default'])
def read_root():
    return "Hello, world!"