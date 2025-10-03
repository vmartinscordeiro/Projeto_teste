from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.db.deps import get_db
from app.models import Farm, Crop, FarmCrop, Season

router = APIRouter()

@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    total_farms = db.scalar(select(func.count()).select_from(Farm)) or 0
    total_area = db.scalar(select(func.coalesce(func.sum(Farm.area_total), 0))) or 0
    return {"total_farms": int(total_farms), "total_hectares": float(total_area)}

@router.get("/pie/state")
def pie_state(db: Session = Depends(get_db)):
    rows = db.execute(select(Farm.state, func.count()).group_by(Farm.state)).all()
    return [{"label": r[0] or "N/A", "value": int(r[1])} for r in rows]

@router.get("/pie/crop")
def pie_crop(db: Session = Depends(get_db)):
    rows = db.execute(
        select(Crop.name, func.count()).join(FarmCrop, FarmCrop.crop_id==Crop.id).group_by(Crop.name)
    ).all()
    return [{"label": name, "value": int(cnt)} for name, cnt in rows]

@router.get("/pie/landuse")
def pie_landuse(db: Session = Depends(get_db)):
    agri, veg = db.execute(
        select(func.coalesce(func.sum(Farm.area_agricultavel), 0),
               func.coalesce(func.sum(Farm.area_vegetacao), 0))
    ).one()
    return [{"label":"Agricultável","value":float(agri)}, {"label":"Vegetação","value":float(veg)}]
