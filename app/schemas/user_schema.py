from app.core.validators.password import validate_password_complexity
from pydantic import Field, EmailStr, field_validator
from app.core.enums.roles import Roles
from app.schemas.base_schema import BaseSchema
from typing import Optional


class UserCreate(BaseSchema):
    username: str = Field(..., min_length=5, max_length=40)
    mail: Optional[EmailStr]
    password: str = Field(...)
    is_active: bool = True
    role: Roles = Roles.user

    @field_validator("password")  # password validator like I see on the other web apps
    @classmethod
    def validate_password(cls, password: str) -> str:
        return validate_password_complexity(v=password)


class UserUpdate(BaseSchema):
    username: Optional[str] = Field(default=None)
    mail: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)

    @field_validator("password")  # password validator like I see on the other web apps
    @classmethod
    def validate_password(cls, password: str) -> str:
        return validate_password_complexity(v=password)


class UserResponce(BaseSchema):
    id: int = Field(..., ge=1)
    username: str = Field(..., min_length=5, max_length=40)
    is_active: bool = Field(...)
    role: Roles = Field(...)


# in one day i need to make here filter schema
