from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from mifaker.routers import generate, users

app = FastAPI()

app.include_router(users.router, prefix="/api/v1/users")
app.include_router(generate.router, prefix="/api/v1/generate")


@app.get("/")
async def root():
    return RedirectResponse("/docs")
