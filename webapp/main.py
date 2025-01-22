from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from webapp.api.task.router import task_router
from webapp.metrics import metrics
from webapp.middleware.correlation import CorrelationIdMiddleware
from webapp.middleware.logger import LogServerMiddleware
from webapp.middleware.metrics_middleware import MetricsMiddleware


def setup_middleware(app: FastAPI) -> None:
    app.add_middleware(CorrelationIdMiddleware)
    app.add_middleware(LogServerMiddleware)
    app.add_middleware(MetricsMiddleware)

    # CORS Middleware should be the last.
    # See https://github.com/tiangolo/fastapi/issues/1663 .
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],    # CORS разрешено для всех доменов.
        allow_credentials=True, # Разрешает использование cookie в cross-origin запросах
        allow_methods=["*"],    # Разрешает все HTTP методы
        allow_headers=["*"],
    )


def setup_routers(app: FastAPI) -> None:
    app.add_route("/metrics", metrics)

    app.include_router(task_router)


# @asynccontextmanager
# async def lifespan(app: FastAPI) -> AsyncIterator[None]:
#     # setup_logger()
#     print("START APP")
#     yield
#     print("END APP")


def create_app() -> FastAPI:
    # app = FastAPI(docs_url="/swagger", lifespan=lifespan)
    app = FastAPI(docs_url="/swagger",)

    setup_middleware(app)
    setup_routers(app)

    return app
