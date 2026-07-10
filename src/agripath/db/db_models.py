import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from agripath.db.database import Base


class ProductORM(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    events: Mapped[list["EventORM"]] = relationship(back_populates="product")


class EventORM(Base):
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=True)
    event_type: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(255))
    registered_by: Mapped[str] = mapped_column(String(100))
    registry_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    product: Mapped["ProductORM"] = relationship(back_populates="events")
