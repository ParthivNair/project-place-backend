from fastapi import APIRouter
import internal.database.clients
import internal.database.postgres
import structlog

logger = structlog.getLogger()
api_router = APIRouter(prefix="/api/v1")

postgres_client = internal.database.clients.get_postgres_client()


@api_router.get("")
async def get_item():
    logger.info("read_root request received")
    result = internal.database.postgres.get_item(postgres_client)
    logger.info("read_root request completed")
    return {"database_result": result}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, query_param: str = None):
#     return {"item_id": item_id, "query_param": query_param}
