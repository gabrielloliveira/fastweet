from sqlalchemy.orm import Session

from settings import get_db


class BaseManager:
    def __init__(self, model):
        self.model = model

    @staticmethod
    def _db() -> Session:
        return next(get_db())

    def instance(self, data):
        return self.model(**data.dict())

    def _save(self, instance):
        db = self._db()
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance

    def save(self, data):
        instance = self.instance(data)
        return self._save(instance)

    def create(self, data):
        instance = self.instance(data)
        return self._save(instance)

    def filter(self, **kwargs):
        qs = self._db().query(self.model)
        for key, value in kwargs.items():
            qs = qs.filter(getattr(self.model, key) == value)
        return qs.order_by(self.model.id.desc())

    def get(self, **kwargs):
        return self.filter(**kwargs).first()

    def update(self, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        return self._save(instance)

    def delete(self, instance) -> bool:
        db = self._db()
        db.delete(instance)
        db.commit()
        return True
