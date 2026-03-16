"""Libraries"""
from fastapi import FastAPI
import pandas as pd
import pickle


# Load Model
model = pickle.load(open("model.pkl", "rb"))


# set app for endpoints
app = FastAPI()

#
@app.get("/")
def home():
    return {"message": "House Price Prediction"}

@app.get("/predict")
def predict(size: int, rooms: int, yob:int):
    # Convert input to DataFrame with same columns used in training
    input_df = pd.DataFrame([[size, rooms, yob]], columns=["Square Meters", "Rooms", "Year Built"])
    prediction = model.predict(input_df)

    # Extract scalar safely
    predicted_price = prediction.item()  # <--- converts array([305000.]) to 305000.0
    return {"predicted_price": float(predicted_price)}