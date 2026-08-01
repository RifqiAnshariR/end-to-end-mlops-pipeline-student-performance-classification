from sqlmodel import create_engine

from app.config import config

engine = create_engine(
    url=config.resolve_userdata_db_url,
    pool_size=10,
    max_overflow=20,
    echo=True,
)
