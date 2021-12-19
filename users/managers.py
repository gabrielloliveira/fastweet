import uuid

from core.managers import BaseManager
from users.models import UserModel
from users.utils import encrypt_password


class UserManager(BaseManager):
    def __init__(self):
        super().__init__(model=UserModel)

    def create(self, data):
        data.password = encrypt_password(data.password)
        data.uuid = str(uuid.uuid4())
        return self.save(data)

    def update(self, user, **kwargs):
        for key, value in kwargs.items():
            if key == "password":
                value = encrypt_password(value)
            setattr(user, key, value)
        return self._save(user)
