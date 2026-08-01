from fastapi import APIRouter

from app.models import Message

router = APIRouter()


@router.get("/health")
def health_check() -> Message:
    return Message(message="ok")
