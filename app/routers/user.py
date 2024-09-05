from fastapi import APIRouter
from app.models.user import User

user_router = APIRouter(prefix="/users", tags=["Users"])

usersList = []


@user_router.get("/")
def users() -> list[User]:
    return list(usersList)


@user_router.get("/{id}")
def user(id: int) -> User:
    for user in usersList:
        if user["id"] == id:
            return user
    return {"message": "User not found"}


@user_router.post("/")
def users(user: User) -> list[User]:
    user = user.model_dump()
    usersList.append(user)
    return list(usersList)


@user_router.put("/{id}")
def update_user(id: int, user: User) -> list[User]:
    for i, u in enumerate(usersList):
        if usersList[i]["id"] == id:
            usersList[i] = user
            return list(usersList)
    return list(usersList)


@user_router.delete("/{id}")
def delete_user(id: int) -> list[User]:
    for index, user in enumerate(usersList):
        if user["id"] == id:
            usersList.pop(index)
            return list(usersList)
    return list(usersList)
