from logging import getLogger, basicConfig
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from jewel_app.db import init_db
from jewel_app.routers import gems
from jewel_app.routers import users

# basicConfig(level="INFO", format="%(asctime)s %(message)s")
logger = getLogger(__name__)

app = FastAPI()

app.include_router(prefix="/api/v1/gems", router=gems.router)
app.include_router(prefix="/api/v1/users", router=users.router)

@app.on_event("startup")
def startup():
    logger.info("😃 Starting up the application")
    init_db()


@app.get("/")
def root():
    return RedirectResponse("/docs")

