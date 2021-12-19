from fastapi import APIRouter, status, Response
from sqlalchemy.exc import IntegrityError

from users.managers import UserManager
from users.schemas import UserSchema, UserDisplaySchema

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
)


@router.post("/")
def create_user(user: UserSchema, response: Response):
    try:
        user = UserManager().create(data=user)
        response.status_code = status.HTTP_201_CREATED
        return UserDisplaySchema(**user.__dict__)
    except IntegrityError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Username already exists."}
