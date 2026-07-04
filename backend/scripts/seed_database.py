import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd
from app.database.database import SessionLocal
from app.database.models import Farmer, Season

db = SessionLocal()

# ------------------------
# Import Farmers
# ------------------------

farmers_df = pd.read_excel("data/farmers.xlsx")

for _, row in farmers_df.iterrows():
    farmer = Farmer(
        name=row["name"],
        location=row["location"],
        soil_type=row["soil_type"],
        irrigation=row["irrigation"]
    )

    db.add(farmer)

db.commit()

print("✅ Farmers imported!")

# ------------------------
# Import Seasons
# ------------------------

seasons_df = pd.read_excel("data/seasons.xlsx")

for _, row in seasons_df.iterrows():
    season = Season(
        farmer_id=row["farmer_id"],
        crop=row["crop"],
        season=row["season"],
        year=row["year"],
        weather=row["weather"],
        disease=row["disease"],
        action_taken=row["action_taken"],
        result=row["result"],
        notes=row["notes"]
    )

    db.add(season)

db.commit()

print("✅ Seasons imported!")

db.close()

print("🎉 Database seeded successfully!")