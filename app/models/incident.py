from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String, DateTime, Enum
from database.base import BaseModel
from enums.status import Status
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import UserModel


class IncidentModel(BaseModel):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(40), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    resolved_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    status: Mapped[Status] = mapped_column(Enum(Status), nullable=False)
    user: Mapped["UserModel"] = relationship(back_populates="incidents")
