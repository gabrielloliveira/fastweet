import uuid

from sqlalchemy.orm import Session

from users.models import UserModel
from users.schemas import UserSchema
from users.utils import encrypt_password


class UserManager:
    @staticmethod
    def _db() -> Session:
        return Session()

    @staticmethod
    def _model(data: UserSchema) -> UserModel:
        return UserModel(data)

    @staticmethod
    def get_unique_uuid() -> uuid.uuid4:
        return uuid.uuid4()

    def _save(self, user: UserModel) -> UserModel:
        self._db().add(user)
        self._db().commit()
        self._db().refresh(user)
        return user

    def create_user(self, data: UserSchema) -> UserModel:
        data.password = encrypt_password(data.password)
        data.uuid = self.get_unique_uuid
        user = self._model(data)
        return self._save(user)
