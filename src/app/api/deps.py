from collections.abc import Generator

from fastapi import Request
from sklearn.ensemble import RandomForestClassifier
from sqlmodel import Session

from app.db import engine


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def get_model(request: Request) -> RandomForestClassifier:
    return request.app.state.model
