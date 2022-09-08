import email
from sqlalchemy.orm import Session
from app.entities import UserEntity, ItemEntity
from app.viewmodels  import UserCreate, ItemCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.query(UserEntity).filter(UserEntity.id == user_id).first()

    def get_users(self, skip:int = 0, limit:int = 10):
        return self.db.query(UserEntity).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = UserEntity(
            email=user.email,
            hashed_password=fake_hashed_password,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def create_user_item(self, user_id:int, item: ItemCreate):
        db_item = ItemEntity(**item.dict(), owner_id=user_id)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
