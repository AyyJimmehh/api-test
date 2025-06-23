import numpy as np
import pandas as pd
import joblib
import uuid
import os
import glob
import time
from app.schemas.iris import IrisFeatures, PredictionOutput
import logging

model = joblib.load("model.pkl")
label_map = {0: "setosa", 1: "versicolor", 2: "virginica"}

logger = logging.getLogger(__name__)

def predict_single(features: IrisFeatures) -> PredictionOutput:
    data = np.array([[features.sepal_length, features.sepal_width,
                      features.petal_length, features.petal_width]])
    pred = int(model.predict(data)[0])
    prob = model.predict_proba(data)[0]
    return PredictionOutput(
        prediction_id=uuid.uuid4().hex[:8],
        predicted_class=pred,
        label=label_map[pred],
        confidence=round(float(max(prob)), 3)
    )

def predict_batch_data(inputs: list[IrisFeatures]):
    results = [predict_single(feat) for feat in inputs]
    df = pd.DataFrame([r.model_dump() for r in results])
    filename = f"predictions_{uuid.uuid4().hex[:8]}.csv"
    df.to_csv(filename, index=False)
    cleanup_old_csvs()
    return results, filename

def cleanup_old_csvs(directory='.', age_minutes=30):
    now = time.time()
    for file in glob.glob(os.path.join(directory, "predictions_*.csv")):
        if os.path.isfile(file) and (now - os.path.getmtime(file)) > age_minutes * 60:
            try:
                os.remove(file)
                logger.info(f"Deleted old CSV: {file}")
            except Exception as e:
                logger.warning(f"Failed to delete {file}: {e}")
