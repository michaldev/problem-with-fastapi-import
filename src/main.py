from fastapi import FastAPI

from rest import users

app = FastAPI()

app.include_router(users.router, prefix='/users', tags=['users'])
