from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.producer import ProducerCreate, ProducerUpdate, ProducerRead
from app.crud import producer as crud

router = APIRouter()

@router.post("", response_model=ProducerRead, status_code=status.HTTP_201_CREATED)
def create_producer(payload: ProducerCreate, db: Session = Depends(get_db)):
    if crud.get_by_doc(db, payload.cpf_cnpj):
        raise HTTPException(status_code=409, detail="CPF/CNPJ já cadastrado.")
    try:
        return crud.create(db, payload)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="CPF/CNPJ já cadastrado.")

@router.get("", response_model=list[ProducerRead])
def list_producers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_(db, skip=skip, limit=limit)

@router.get("/{producer_id}", response_model=ProducerRead)
def get_producer(producer_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, producer_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Produtor não encontrado.")
    return obj

@router.put("/{producer_id}", response_model=ProducerRead)
def update_producer(producer_id: int, payload: ProducerUpdate, db: Session = Depends(get_db)):
    obj = crud.get(db, producer_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Produtor não encontrado.")
    return crud.update(db, obj, payload)

@router.delete("/{producer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_producer(producer_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, producer_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Produtor não encontrado.")
    crud.delete(db, obj)
    return None
