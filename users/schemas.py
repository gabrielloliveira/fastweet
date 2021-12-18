from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    uuid: Optional[str] = None
    name: Optional[str] = None
    username: str
    password: str
