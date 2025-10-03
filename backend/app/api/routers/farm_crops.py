from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.farm_crop import FarmCropCreate, FarmCropRead
from app.crud import farm_crop as crud

router = APIRouter()

@router.post("", response_model=FarmCropRead)
def add_farm_crop(payload: FarmCropCreate, db: Session = Depends(get_db)):
    obj = crud.create(db, payload)
    return {"id": obj.id, "farm_id": obj.farm_id, "season": payload.season, "crop": payload.crop}

@router.get("", response_model=list[FarmCropRead])
def list_farm_crops(farm_id: int | None = None, season: str | None = None, crop: str | None = None, db: Session = Depends(get_db)):
    return crud.list_(db, farm_id=farm_id, season=season, crop=crop)
