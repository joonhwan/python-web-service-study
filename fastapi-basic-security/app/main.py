from loguru import logger
from pydantic import BaseModel
from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = dict(
    joonhwan=dict(
        username="joonhwan",
        full_name="Joonhwan Lee",
        email="joonhwan@acme.com",
        hashed_password="fakehashed123",
        disabled=False,
    ),
    sinyoung=dict(
        username="sinyoung",
        full_name="Sinyoung Lee",
        email="sinyoung@acme.com",
        hashed_password="fakehashed123",
        disabled=True,
    )
)


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDb(User):
    hashed_password: str


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="joonhwan@acme.com", full_name="Joonhwan Lee", disabled=False
    )


def fake_hash_password(password: str):
    return "fakehashed" + password


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    logger.info(f"/token is called with {form_data.__dict__}")
    found_user = fake_users_db.get(form_data.username)
    if not found_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    user = UserInDb(**found_user)
    hashed_password = fake_hash_password(form_data.password)
    logger.info("hashed_password: {hashed_password}",
                hashed_password=hashed_password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    return dict(
        access_token=f"faketoken.for.{user.username}",
        token_type="bearer",
    )


@app.get("/items/")
async def get_items(current_user: User = Depends(get_current_user)):
    return current_user
