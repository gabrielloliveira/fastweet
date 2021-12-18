import uuid

from sqlalchemy.orm import Session

from settings import get_db
from users.models import UserModel
from users.schemas import UserSchema
from users.utils import encrypt_password


class UserManager:
    @staticmethod
    def _db() -> Session:
        return next(get_db())

    @staticmethod
    def _model(data: UserSchema) -> UserModel:
        return UserModel(**data.dict())

    @staticmethod
    def get_unique_uuid() -> str:
        return str(uuid.uuid4())

    @staticmethod
    def _save(user: UserModel) -> UserModel:
        db = UserManager._db()
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def create_user(data: UserSchema) -> UserModel:
        data.password = encrypt_password(data.password)
        data.uuid = UserManager.get_unique_uuid()
        user = UserManager._model(data)
        return UserManager._save(user)
