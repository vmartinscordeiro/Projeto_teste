from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Producer
from app.schemas.producer import ProducerCreate, ProducerUpdate

def get(db: Session, producer_id: int) -> Producer | None:
    return db.get(Producer, producer_id)

def get_by_doc(db: Session, cpf_cnpj: str) -> Producer | None:
    return db.execute(select(Producer).where(Producer.cpf_cnpj == cpf_cnpj)).scalar_one_or_none()

def list_(db: Session, skip: int = 0, limit: int = 100):
    return db.execute(select(Producer).offset(skip).limit(limit)).scalars().all()

def create(db: Session, data: ProducerCreate) -> Producer:
    obj = Producer(cpf_cnpj=data.cpf_cnpj, name=data.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, obj: Producer, data: ProducerUpdate) -> Producer:
    obj.name = data.name
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, obj: Producer) -> None:
    db.delete(obj)
    db.commit()
