from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Season, Crop, FarmCrop
from app.schemas.farm_crop import FarmCropCreate

def _get_or_create_season(db: Session, name: str) -> Season:
    s = db.execute(select(Season).where(Season.name == name)).scalar_one_or_none()
    if s: return s
    s = Season(name=name)
    db.add(s); db.commit(); db.refresh(s)
    return s

def _get_or_create_crop(db: Session, name: str) -> Crop:
    c = db.execute(select(Crop).where(Crop.name == name)).scalar_one_or_none()
    if c: return c
    c = Crop(name=name)
    db.add(c); db.commit(); db.refresh(c)
    return c

def create(db: Session, data: FarmCropCreate) -> FarmCrop:
    s = _get_or_create_season(db, data.season)
    c = _get_or_create_crop(db, data.crop)
    obj = db.execute(
        select(FarmCrop).where(
            FarmCrop.farm_id == data.farm_id,
            FarmCrop.season_id == s.id,
            FarmCrop.crop_id == c.id,
        )
    ).scalar_one_or_none()
    if obj:
        return obj
    obj = FarmCrop(farm_id=data.farm_id, season_id=s.id, crop_id=c.id)
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def list_(db: Session, farm_id: int | None = None, season: str | None = None, crop: str | None = None):
    from sqlalchemy import and_
    stmt = select(FarmCrop, Season.name, Crop.name).join(Season, Season.id==FarmCrop.season_id).join(Crop, Crop.id==FarmCrop.crop_id)
    if farm_id is not None:
        stmt = stmt.where(FarmCrop.farm_id == farm_id)
    if season is not None:
        stmt = stmt.where(Season.name == season)
    if crop is not None:
        stmt = stmt.where(Crop.name == crop)
    rows = db.execute(stmt).all()
    # mapeia para dict simples
    return [{"id": fc.id, "farm_id": fc.farm_id, "season": sname, "crop": cname} for (fc, sname, cname) in rows]
