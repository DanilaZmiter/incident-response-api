from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import BaseModel
from sqlalchemy import String, Enum, Boolean
from app.enums.roles import Roles
from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.incident import IncidentModel


class UserModel(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    mail: Mapped[str] = mapped_column(String(40), nullable=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    role: Mapped[Roles] = mapped_column(Enum(Roles), nullable=False)

    # like class attr, to store(see) list of incidents that have user \(\downarrow \)
    incidents: Mapped[List["IncidentModel"]] = relationship(back_populates="user")
