from fastapi import FastAPI
from users import models as users_models
from tweets import models as tweets_models
from users import routers as users_routers

app = FastAPI()
app.include_router(users_routers.router)

users_models.BaseDB.metadata.create_all(bind=users_models.ENGINE)
tweets_models.BaseDB.metadata.create_all(bind=tweets_models.ENGINE)
