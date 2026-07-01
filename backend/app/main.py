from fastapi import FastAPI
from app.schemas.farmer import Farmer

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Krishi Mitra 🌾"
    }


@app.post("/farmer")
def create_farmer(farmer: Farmer):
    return {
        "message": "Farmer profile created successfully!",
        "farmer": farmer
    }