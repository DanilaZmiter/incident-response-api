import uvicorn


from fastapi import FastAPI
from database.database import dbhelper
from database.base import BaseModel


async def lifespan(app: FastAPI):
    async with dbhelper.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
        yield
        await dbhelper.engine.dispose()


app = FastAPI()


@app.get("/")
async def root():
    return {"name": "Root View"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
