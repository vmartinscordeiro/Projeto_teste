from pydantic import BaseModel

class FarmCropCreate(BaseModel):
    farm_id: int
    season: str   # ex: "Safra 2021/22"
    crop: str     # ex: "Soja"

class FarmCropRead(BaseModel):
    id: int
    farm_id: int
    season: str
    crop: str
