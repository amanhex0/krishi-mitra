from pydantic import BaseModel


class Season(BaseModel):
    farmer_id: int

    crop: str
    season: str
    year: int

    weather: str | None = None
    disease: str | None = None
    action_taken: str | None = None
    result: str | None = None
    notes: str | None = None