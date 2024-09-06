from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.models.user import User, UserDto
from db.database import get_db
from sqlalchemy.orm import Session
from db.entities import UserEntity

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/", response_model=List[UserDto])
def users(db: Session = Depends(get_db)) -> list[User]:
    db_users = db.query(UserEntity).all()
    return JSONResponse(content=jsonable_encoder(db_users), status_code=200)


@user_router.get("/{id}", response_model=UserDto)
def user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserEntity).filter(UserEntity.id == id).first()
    if not user:
        return JSONResponse(content={"error": "User not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(user), status_code=200)


@user_router.post("/")
def users(user: User, db: Session = Depends(get_db)) -> list:
    try:
        db_user = UserEntity(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return JSONResponse(content=jsonable_encoder(db_user), status_code=201)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@user_router.put("/{id}")
def update_user(id: int, user: User, db: Session = Depends(get_db)) -> dict:
    try:
        db_user = db.query(UserEntity).filter(UserEntity.id == id)
        if not db_user.first():
            return JSONResponse(content={"error": "User not found"}, status_code=404)
        db_user.update(user.model_dump(exclude_unset=True))
        db.commit()
        return JSONResponse(content=jsonable_encoder(db_user.first()), status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@user_router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)) -> dict:
    try:
        user = db.query(UserEntity).filter(UserEntity.id == id).first()
        if not user:
            return JSONResponse(content={"error": "User not found"}, status_code=404)
        db.delete(user)
        db.commit()
        return JSONResponse(content={"message": "User deleted"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
