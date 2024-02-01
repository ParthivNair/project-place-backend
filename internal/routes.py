from fastapi import APIRouter, Depends
import internal.database.clients
from internal.database.postgres import engine, SessionLocal
import internal.database.clients as client
from pydantic import BaseModel
import structlog
from typing import List, Annotated
from sqlalchemy.orm import Session
import internal.database.models as models

logger = structlog.getLogger()
router = APIRouter()

# postgres_client = client.get_postgres_client()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


models.Base.metadata.create_all(bind=engine)


class UserBase(BaseModel):
    id: int
    username: str


@router.post("/users/")
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(username=user.username, id=user.id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)




# @api_router.get("/items/{item_id}")
# async def get_item(item_id: int):
#     logger.info("read_root request received")
#     result = internal.database.postgres.get_item(item_id)
#     logger.info("read_root request completed")
#     return {"database_result": result}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, query_param: str = None):
#     return {"item_id": item_id, "query_param": query_param}
