from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse, FileResponse
from typing import List
from app.schemas.iris import IrisFeatures, PredictionOutput, BatchPredictionOutput
from app.services.iris_model import predict_single, predict_batch_data
from app.utils.security import get_api_key
import os

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/predict", response_model=PredictionOutput)
def predict_endpoint(features: IrisFeatures, _: str = Depends(get_api_key)):
    try:
        return predict_single(features)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(e)})

@router.post("/predict-batch", response_model=BatchPredictionOutput)
def predict_batch_endpoint(inputs: List[IrisFeatures], _: str = Depends(get_api_key)):
    try:
        results, filename = predict_batch_data(inputs)
        return {"results": results, "csv_file": filename}
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(e)})

@router.get("/download/{filename}")
def download_file(filename: str, _: str = Depends(get_api_key)):
    path = os.path.join(".", filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path=path, filename=filename, media_type='text/csv')
