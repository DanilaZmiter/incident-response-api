from app.models.user import UserModel
from app.core.entities.user_entity import UserEntity

# here its need to import of schema but noew it doesnt exist


class UserMapper:

    @staticmethod
    def to_domain(user_model: UserModel) -> UserEntity:
        return UserEntity(
            id=user_model.id,
            username=user_model.username,
            mail=user_model.mail,
            hashed_password=user_model.hashed_password,
            is_active=user_model.is_active,
            role=user_model.role,
        )

    @staticmethod
    def to_orm(user_entity: UserEntity) -> "UserModel":
        return UserModel(
            id=user_entity.id,
            username=user_entity.username,
            mail=user_entity.mail,
            hashed_password=user_entity.hashed_password,
            is_active=user_entity.is_active,
            role=user_entity.role,
        )

    @staticmethod
    def to_dto(
        user_entity: UserEntity,
    ):  # shall be UserSchema in future, dto = Pydantic schema
        pass
