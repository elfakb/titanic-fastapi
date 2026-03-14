from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Titanic Survival Predictor")

# Modeli yükle
model = joblib.load("titanic_model.pkl")


class Passenger(BaseModel):
    Pclass: int
    Sex: int  # 0: Male, 1: Female
    Age: float
    SibSp: int
    Parch: int
    Fare: float

@app.get("/")
def home():
    return {"message": "Titanic Prediction API is Running!"}

@app.post("/predict")
def predict_survival(passenger: Passenger):

    data = pd.DataFrame([passenger.dict()])
    prediction = model.predict(data)
    
    status = "Survived" if int(prediction[0]) == 1 else "Not Survived"
    return {"prediction": status, "survived_binary": int(prediction[0])}