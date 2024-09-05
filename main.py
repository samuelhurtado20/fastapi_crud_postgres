from fastapi import FastAPI
from app.routers.user import user_router


app = FastAPI()
app.include_router(user_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
