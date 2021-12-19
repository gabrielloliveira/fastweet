from datetime import datetime

from pydantic import BaseModel

from users.schemas import UserSchema


class TweetSchema(BaseModel):
    uuid: str
    created_at: datetime
    updated_at: datetime
    text: str
    user: UserSchema
