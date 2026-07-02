from sqlalchemy import select
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.database.models import Farmer as FarmerModel
from fastapi import FastAPI
from app.schemas.farmer import Farmer
from app.database.database import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Krishi Mitra 🌾"
    }


@app.post("/farmer")
def create_farmer(farmer: Farmer, db: Session = Depends(get_db)):

    db_farmer = FarmerModel(
        name=farmer.name,
        location=farmer.location,
        soil_type=farmer.soil_type,
        irrigation=farmer.irrigation
    )

    db.add(db_farmer)
    db.commit()
    db.refresh(db_farmer)

    return {
        "message": "Farmer profile created successfully!",
        "farmer": db_farmer
    }
    
@app.get("/farmers")
def get_farmers(db: Session = Depends(get_db)):
    farmers = db.scalars(select(FarmerModel)).all()

    return {
        "count": len(farmers),
        "farmers": farmers
    }