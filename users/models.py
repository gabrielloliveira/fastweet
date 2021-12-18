from sqlalchemy import Integer, Column, String

from settings import BaseDB, engine

ENGINE = engine


class UserModel(BaseDB):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36), unique=True, index=True)
    name = Column(String(50), nullable=True)
    username = Column(String(120), unique=True, nullable=False)
    password = Column(String, nullable=False)
