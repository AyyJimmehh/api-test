from pydantic import BaseModel, Field
from typing import List

class IrisFeatures(BaseModel):
    sepal_length: float = Field(gt=0, lt=10)
    sepal_width: float = Field(gt=0, lt=10)
    petal_length: float = Field(gt=0, lt=10)
    petal_width: float = Field(gt=0, lt=10)

class PredictionOutput(BaseModel):
    prediction_id: str
    predicted_class: int
    label: str
    confidence: float

class BatchPredictionOutput(BaseModel):
    results: List[PredictionOutput]
    csv_file: str
