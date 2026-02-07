from fastapi import APIRouter

from app.api.routes import competitions

api_router = APIRouter()
api_router.include_router(competitions.router, tags=["competitions"])
