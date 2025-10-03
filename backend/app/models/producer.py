from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class Producer(Base):
    __tablename__ = "producers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cpf_cnpj: Mapped[str] = mapped_column(String(14), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)

    farms: Mapped[list["Farm"]] = relationship(back_populates="producer")
