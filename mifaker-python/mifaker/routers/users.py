from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException
from mifaker.models.users import User, UserUpdateRequest, Gender, Role

router = APIRouter()

db: List[User] = [
    User(
        id=UUID("5d96e735-2f04-4126-b1da-98833c3138d4"),
        first_name="Jamila",
        last_name="Smith",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("4bfa68ea-5cca-4f66-8507-85fbfac92812"),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


@router.get("/")
def get_all_users():
    return db


@router.post("/")
def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@router.delete("/{user_id}")
def delete_user(user_id: UUID):
    user = next(filter(lambda u: u.id == user_id, db), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.remove(user)
    return {"id": user_id}


@router.put("/{user_id}")
def update_user(user_id: UUID, user: UserUpdateRequest):
    u = next(filter(lambda u: u.id == user_id, db), None)
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")

    # assign value to variable if not none
    u.first_name = user.first_name or u.first_name
    u.last_name = user.last_name or u.last_name
    u.middle_name = user.middle_name or u.middle_name
    u.gender = user.gender or u.gender
