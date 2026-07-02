from sqlalchemy import Column, Integer, String, Boolean

from app.database.database import Base


class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    soil_type = Column(String, nullable=False)
    irrigation = Column(Boolean, nullable=False)