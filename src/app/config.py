from __future__ import annotations

from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parents[2]


class Config(BaseSettings):
    # Paths
    raw_data_dir: Path = ROOT_DIR / "data/raw"
    user_data_dir: Path = ROOT_DIR / "data/user_data"
    temp_dir: Path = ROOT_DIR / "tmp"

    # or use: "models:/random_forest@production"
    mlflow_model_uri: str = "models:/random_forest/1"

    # Env
    mlflow_tracking_uri: str
    userdata_db_user: str
    userdata_db_password: str
    userdata_db_name: str
    userdata_db_host: str
    userdata_db_port: str

    @computed_field
    @property
    def resolve_userdata_db_url(self) -> str:
        return (
            f"postgresql://{self.userdata_db_user}:{self.userdata_db_password}"
            f"@{self.userdata_db_host}:{self.userdata_db_port}/{self.userdata_db_name}"
        )

    model_config = SettingsConfigDict(
        frozen=True,
        extra="ignore",
        env_file=ROOT_DIR / ".env",
    )


config = Config()  # type: ignore
