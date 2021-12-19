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

    @staticmethod
    def filter(**kwargs) -> UserModel:
        qs = UserManager._db().query(UserModel)
        for key, value in kwargs.items():
            qs = qs.filter(getattr(UserModel, key) == value)
        return qs.order_by(UserModel.id.desc())

    @staticmethod
    def get(**kwargs) -> UserModel:
        return UserManager.filter(**kwargs).first()

    @staticmethod
    def update(user: UserModel, **kwargs) -> UserModel:
        for key, value in kwargs.items():
            if key == "password":
                value = encrypt_password(value)
            setattr(user, key, value)
        return UserManager._save(user)

    @staticmethod
    def delete(user: UserModel) -> bool:
        db = UserManager._db()
        db.delete(user)
        db.commit()
        return True
