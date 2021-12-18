from fastapi import FastAPI
from users import models as users_models

app = FastAPI()

users_models.BaseDB.metadata.create_all(bind=users_models.ENGINE)
