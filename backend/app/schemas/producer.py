from pydantic import BaseModel, field_validator
from app.utils.validators import normalize_cpf_cnpj

class ProducerBase(BaseModel):
    cpf_cnpj: str
    name: str

    @field_validator("cpf_cnpj")
    @classmethod
    def _cpf_cnpj_ok(cls, v: str) -> str:
        return normalize_cpf_cnpj(v)

class ProducerCreate(ProducerBase):
    pass

class ProducerUpdate(BaseModel):
    name: str

class ProducerRead(BaseModel):
    id: int
    cpf_cnpj: str
    name: str

    class Config:
        from_attributes = True
