from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class UserSchema(BaseModel):
    uuid = Optional[UUID]
    name: Optional[str] = None
    username: str
    password: str
