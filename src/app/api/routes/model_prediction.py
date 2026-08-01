from typing import Annotated

from fastapi import APIRouter, Depends
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sqlmodel import Session

from app.api.deps import get_db, get_model
from app.crud import insert_user_data
from app.models import InputModel, OutputModel

router = APIRouter()


@router.post("/predict")
def model_prediction(
    input: InputModel,
    model: Annotated[RandomForestClassifier, Depends(get_model)],
    session: Annotated[Session, Depends(get_db)],
) -> OutputModel:
    data = pd.DataFrame([row.model_dump() for row in input.rows])

    predictions = model.predict(data)

    data_rows = [
        {**row.model_dump(), "performance_category": prediction}
        for row, prediction in zip(input.rows, predictions)
    ]
    insert_user_data(session, data_rows)

    return OutputModel(predictions=predictions.tolist())
