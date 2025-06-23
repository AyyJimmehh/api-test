from fastapi import FastAPI
from app.routes import predict

app = FastAPI(title="Iris Classifier API", version="1.0")
app.include_router(predict.router)
