from internal import routes
import structlog
from uvicorn import Server, Config
import fastapi
from internal import routes

app = fastapi.FastAPI()
app.include_router(routes.router)


if __name__ == "__main__":
    logger = structlog.get_logger()
    logger.warning("application started")
    server = Server(Config(app))
    server.run()
    logger.warning("application shutdown")
