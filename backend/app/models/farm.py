from sqlalchemy import String, ForeignKey, Numeric, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class Farm(Base):
    __tablename__ = "farms"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    producer_id: Mapped[int] = mapped_column(ForeignKey("producers.id", ondelete="CASCADE"), nullable=False)

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    city: Mapped[str] = mapped_column(String(120), nullable=True)
    state: Mapped[str] = mapped_column(String(2), nullable=True)

    area_total: Mapped[float] = mapped_column(Numeric(14, 2), nullable=False)
    area_agricultavel: Mapped[float] = mapped_column(Numeric(14, 2), nullable=False)
    area_vegetacao: Mapped[float] = mapped_column(Numeric(14, 2), nullable=False)

    __table_args__ = (
        CheckConstraint("area_agricultavel + area_vegetacao <= area_total", name="ck_farm_areas_validas"),
    )

    producer: Mapped["Producer"] = relationship(back_populates="farms")
