from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# expose save json file as data api for the front end
@app.get("/data")
def get_data():
    df = pd.read_json("../data/processed.json")
    return df.to_dict(orient="records")