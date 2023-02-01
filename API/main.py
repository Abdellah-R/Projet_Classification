from fastapi import FastAPI
from model import predict
from pydantic import BaseModel

class Textin(BaseModel):
    NAICS: int
    UrbanRural : int
    NoEmp : int
    RetainedJob : int
    Term : int

class Prediction(BaseModel):
    MIS_Status : int
    
app = FastAPI()

@app.post("/predict", response_model=Prediction)
async def root_predict(payload : Textin):
    value = [x for x in payload.__dict__.values()]
    to_return = predict(value)
    return {"MIS_Status": to_return}