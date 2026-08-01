from contextlib import asynccontextmanager

from fastapi import FastAPI

# from fastapi.middleware.cors import CORSMiddleware
import mlflow

from app.api.routes import health_check, model_prediction
from app.config import config
from app.utils import empty_temp_dir


@asynccontextmanager
async def lifespan(app: FastAPI):
    mlflow.set_tracking_uri(uri=config.mlflow_tracking_uri)

    empty_temp_dir(config.temp_dir)
    app.state.model = mlflow.pyfunc.load_model(
        model_uri=config.mlflow_model_uri,
        dst_path=config.temp_dir,  # type: ignore
    )

    yield

    app.state.model = None


app = FastAPI(lifespan=lifespan)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(health_check.router, prefix="/health", tags=["health"])
app.include_router(model_prediction.router, prefix="/predict", tags=["model"])
