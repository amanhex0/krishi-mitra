from pydantic import BaseModel


class Farmer(BaseModel):
    name: str
    location: str
    soil_type: str
    irrigation: bool