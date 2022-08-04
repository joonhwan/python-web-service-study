from logging import getLogger
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jewel_app.db import get_session
from jewel_app.models.user import User
from jewel_app.viewmodels.users import CurrentUser, UserLogin

logger = getLogger(__name__)

router = APIRouter()

# oatuh2_scheme 은 "Bearer {token}" 을 반환하는 callable 객체(~ 함수)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"api/v1/users/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    return CurrentUser(id=1, username="joonhwan")

# @router.get("/{user_id}")
# def get_user(user_id: int, response: Response, session = Depends(get_session)):
#     user = session.get(User, user_id)
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     return user


@router.get("/me")
async def get_users(user: User = Depends(get_current_user)):
    return user


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    logger.info(f"🔒 User logging in : {form_data}")
    return {"access_token": "fake-token"}
