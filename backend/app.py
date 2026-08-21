from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import json

app = FastAPI()


        
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# expose save json file as data api for the front end
@app.get("/employPerDeg")
def get_data():
    with open("../data/employPerDeg.json", "r") as file:
            return json.load(file)

@app.get("/majorEarnings")
def get_data():
    with open("../data/majorEarnings.json", "r") as file:
            return json.load(file)

@app.get("/roadmap")
def get_roadmap():
    with open("../data/roadmap.json", "r") as file:
        return json.load(file)