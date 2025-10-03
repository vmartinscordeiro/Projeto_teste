from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.farm import FarmCreate, FarmUpdate, FarmRead
from app.crud import farm as crud

router = APIRouter()

@router.post("", response_model=FarmRead, status_code=status.HTTP_201_CREATED)
def create_farm(payload: FarmCreate, db: Session = Depends(get_db)):
    return crud.create(db, payload)

@router.get("", response_model=list[FarmRead])
def list_farms(skip: int = 0, limit: int = 100, producer_id: int | None = None, db: Session = Depends(get_db)):
    return crud.list_(db, skip=skip, limit=limit, producer_id=producer_id)

@router.get("/{farm_id}", response_model=FarmRead)
def get_farm(farm_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, farm_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Fazenda não encontrada.")
    return obj

@router.put("/{farm_id}", response_model=FarmRead)
def update_farm(farm_id: int, payload: FarmUpdate, db: Session = Depends(get_db)):
    obj = crud.get(db, farm_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Fazenda não encontrada.")
    return crud.update(db, obj, payload)

@router.delete("/{farm_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_farm(farm_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, farm_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Fazenda não encontrada.")
    crud.delete(db, obj)
    return None
