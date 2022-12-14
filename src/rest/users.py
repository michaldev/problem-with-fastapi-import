from fastapi import APIRouter

from main import app

router = APIRouter()


@router.get('/hello')
async def hello():
    return {'hello': 'world'}
