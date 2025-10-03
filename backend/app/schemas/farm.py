from pydantic import BaseModel, field_validator, model_validator
from decimal import Decimal
from typing import Optional

class FarmBase(BaseModel):
    producer_id: int
    name: str
    city: Optional[str] = None
    state: Optional[str] = None
    area_total: Decimal
    area_agricultavel: Decimal
    area_vegetacao: Decimal

    @field_validator("state")
    @classmethod
    def _uf(cls, v):
        if v is None or v == "":
            return None
        v = v.upper()
        if len(v) != 2:
            raise ValueError("UF deve ter 2 letras.")
        return v

    @model_validator(mode="after")
    def _areas_ok(self):
        if (self.area_agricultavel or 0) + (self.area_vegetacao or 0) > (self.area_total or 0):
            raise ValueError("Soma de áreas agricultável + vegetação não pode exceder área total.")
        return self

class FarmCreate(FarmBase):
    pass

class FarmUpdate(BaseModel):
    name: str
    city: Optional[str] = None
    state: Optional[str] = None
    area_total: Decimal
    area_agricultavel: Decimal
    area_vegetacao: Decimal

    @model_validator(mode="after")
    def _areas_ok(self):
        if (self.area_agricultavel or 0) + (self.area_vegetacao or 0) > (self.area_total or 0):
            raise ValueError("Soma de áreas agricultável + vegetação não pode exceder área total.")
        return self

class FarmRead(BaseModel):
    id: int
    producer_id: int
    name: str
    city: str | None
    state: str | None
    area_total: Decimal
    area_agricultavel: Decimal
    area_vegetacao: Decimal

    class Config:
        from_attributes = True
