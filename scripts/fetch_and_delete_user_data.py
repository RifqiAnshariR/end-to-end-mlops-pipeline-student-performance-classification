from datetime import datetime

import pandas as pd
from sqlmodel import Session, create_engine, text

from app.config import config

LIMIT_ROWS = 1000


def fetch_and_delete_user_data(session: Session, limit: int) -> pd.DataFrame:
    query = text("""
        WITH row_to_delete AS (
            SELECT id FROM userdata
            LIMIT :limit
        )
        DELETE FROM userdata
        WHERE id IN (
            SELECT id FROM row_to_delete
        )
        RETURNING *
    """)
    result = session.execute(query, {"limit": limit})
    rows = result.fetchall()
    columns = list(result.keys())

    session.commit()

    return pd.DataFrame(data=rows, columns=columns)


def main():
    engine = create_engine(url=config.resolve_userdata_db_url, echo=True)
    with Session(engine) as session:
        raw_current_df = fetch_and_delete_user_data(session, LIMIT_ROWS)

    if not raw_current_df.empty:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        raw_current_df.to_csv(
            path_or_buf=config.user_data_dir / f"user_data_{timestamp}.csv",
            index=False,
        )


if __name__ == "__main__":
    main()
