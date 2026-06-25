from app.core.entities.base import BaseEntity
from dataclasses import dataclass
from app.core.enums.roles import Roles

@dataclass
class UserEntity(BaseEntity):
    id: int
    username: str
    mail: str
    hashed_password: str
    is_active: bool
    role: Roles
    