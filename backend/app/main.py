from sqlalchemy import select
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.database.models import Farmer as FarmerModel
from fastapi import FastAPI
from app.schemas.farmer import Farmer
from app.database.database import engine
from app.database.models import Base
from app.schemas.season import Season
from app.database.models import Season as SeasonModel

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
 
@app.post("/season")
def create_season(season: Season, db: Session = Depends(get_db)):

    db_season = SeasonModel(
        farmer_id=season.farmer_id,
        crop=season.crop,
        season=season.season,
        year=season.year,
        weather=season.weather,
        disease=season.disease,
        action_taken=season.action_taken,
        result=season.result,
        notes=season.notes
    )

    db.add(db_season)
    db.commit()
    db.refresh(db_season)

    return {
        "message": "Season created successfully!",
        "season": db_season
    }    
    
    
@app.get("/seasons")
def get_seasons(db: Session = Depends(get_db)):
    seasons = db.scalars(select(SeasonModel)).all()

    return {
        "count": len(seasons),
        "seasons": seasons
    }
    
@app.get("/farmers/{farmer_id}/seasons")
def get_farmer_seasons(farmer_id: int, db: Session = Depends(get_db)):

    seasons = db.scalars(
        select(SeasonModel).where(SeasonModel.farmer_id == farmer_id)
    ).all()

    return {
        "farmer_id": farmer_id,
        "count": len(seasons),
        "seasons": seasons
    }    