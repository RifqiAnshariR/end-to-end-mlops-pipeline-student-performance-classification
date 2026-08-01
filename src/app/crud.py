from typing import Any

from sqlmodel import Session

from app.models import UserData


def insert_user_data(session: Session, rows: list[dict[str, Any]]) -> None:
    objects = [UserData(**row) for row in rows]
    session.add_all(objects)
    session.commit()
