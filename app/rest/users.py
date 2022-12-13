from fastapi import APIRouter

# from app.main import app
from ..main import app
# if I comment this, all works. But I need to use app in this file

router = APIRouter()


@router.get('/hello')
async def hello():
    return {'hello': 'world'}
