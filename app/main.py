from fastapi import FastAPI

from app.rest import users

app = FastAPI()

app.include_router(users.router, prefix='/users', tags=['users'])
