from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    soil_type = Column(String, nullable=False)
    irrigation = Column(Boolean, nullable=False)

    seasons = relationship(
        "Season",
        back_populates="farmer",
        cascade="all, delete-orphan"
    )


class Season(Base):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True, index=True)

    farmer_id = Column(Integer, ForeignKey("farmers.id"))

    crop = Column(String, nullable=False)
    season = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    weather = Column(String, nullable=True)
    disease = Column(String, nullable=True)
    action_taken = Column(String, nullable=True)
    result = Column(String, nullable=True)
    notes = Column(String, nullable=True)

    farmer = relationship(
        "Farmer",
        back_populates="seasons"
    )