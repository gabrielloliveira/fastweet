from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    uuid: Optional[str] = None
    name: Optional[str] = None
    username: str
    password: str


class UserDisplaySchema(BaseModel):
    uuid: Optional[str] = None
    name: Optional[str] = None
    username: str

    class Config:
        orm_mode = True
