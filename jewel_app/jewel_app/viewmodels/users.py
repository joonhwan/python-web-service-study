from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class CurrentUser(BaseModel):
    username: str
    id: int