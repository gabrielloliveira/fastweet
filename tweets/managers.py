import uuid
from datetime import datetime

from core.managers import BaseManager
from tweets.models import TweetModel


class TweetManager(BaseManager):
    def __init__(self):
        super().__init__(model=TweetModel)

    def create(self, data):
        data.created_at = datetime.now()
        data.updated_at = datetime.now()
        data.uuid = str(uuid.uuid4())
        return super(TweetManager, self).create(data)

    def update(self, instance, **kwargs):
        instance.updated_at = datetime.now()
        return super(TweetManager, self).update(instance, **kwargs)
