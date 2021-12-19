from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from settings import BaseDB, engine
from users.models import UserModel

ENGINE = engine


class TweetModel(BaseDB):
    __tablename__ = "tweet"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36), unique=True, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    text = Column(String(280))
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(UserModel, backref="tweets", lazy="subquery")
