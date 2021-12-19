from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from users.schemas import UserDisplaySchema


class TweetSchema(BaseModel):
    uuid: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    text: str
    user_id: int


class TweetSchemaDisplay(BaseModel):
    uuid: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    text: str
    user: UserDisplaySchema

    class Config:
        orm_mode = True
