from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/data")
def get_data():
    df = pd.read_json("data/processed.json")
    return df.to_dict(orient="records")