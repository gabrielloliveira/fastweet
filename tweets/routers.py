from typing import List

from fastapi import APIRouter, Response, status

from tweets.managers import TweetManager
from tweets.schemas import TweetSchema, TweetSchemaDisplay

router = APIRouter(prefix="/api/tweets", tags=["tweets"])


@router.get(
    "/", response_model=List[TweetSchemaDisplay], status_code=status.HTTP_200_OK
)
def list_tweets():
    return TweetManager().filter(user_id=1).all()


@router.post("/")
def create(tweet: TweetSchema, response: Response):
    try:
        tweet = TweetManager().create(tweet)
        response.status_code = status.HTTP_201_CREATED
        return TweetSchemaDisplay(**tweet.__dict__)
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": str(e)}
