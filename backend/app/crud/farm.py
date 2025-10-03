from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Farm
from app.schemas.farm import FarmCreate, FarmUpdate

def get(db: Session, farm_id: int) -> Farm | None:
    return db.get(Farm, farm_id)

def list_(db: Session, skip: int = 0, limit: int = 100, producer_id: int | None = None):
    stmt = select(Farm)
    if producer_id is not None:
        stmt = stmt.where(Farm.producer_id == producer_id)
    return db.execute(stmt.offset(skip).limit(limit)).scalars().all()

def create(db: Session, data: FarmCreate) -> Farm:
    obj = Farm(
        producer_id=data.producer_id,
        name=data.name,
        city=data.city,
        state=data.state,
        area_total=data.area_total,
        area_agricultavel=data.area_agricultavel,
        area_vegetacao=data.area_vegetacao,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, obj: Farm, data: FarmUpdate) -> Farm:
    obj.name = data.name
    obj.city = data.city
    obj.state = data.state
    obj.area_total = data.area_total
    obj.area_agricultavel = data.area_agricultavel
    obj.area_vegetacao = data.area_vegetacao
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, obj: Farm) -> None:
    db.delete(obj)
    db.commit()
