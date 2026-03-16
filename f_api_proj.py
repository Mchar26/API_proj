"""Libraries"""
from fastapi import FastAPI
import pandas as pd
import pickle
from pathlib import Path

# Load Model — absolute path so it works on Render too
BASE_DIR = Path(__file__).resolve().parent
model = pickle.load(open(BASE_DIR / "model.pkl", "rb"))

# set app for endpoints
app = FastAPI()

@app.get("/")
def home():
    return {"message": "House Price Prediction"}

@app.get("/predict")
def predict(size: int, rooms: int, yob: int):
    # Column names must match exactly what was used during training
    input_df = pd.DataFrame([[size, rooms, yob]], columns=["size", "rooms", "yob"])
    prediction = model.predict(input_df)
    predicted_price = prediction.item()
    return {"predicted_price": float(predicted_price)}