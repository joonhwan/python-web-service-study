import os
from fastapi import FastAPI, Request, Header, Depends
from fastapi.templating import Jinja2Templates
from app.repositories import MovieRepository
from app.db.func import init_db
from app.utils.seed import seed_movie_entities

template_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=template_dir)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    init_db()
    seed_movie_entities()

@app.get("/")
async def home(
    request: Request,
    hx_request: str | None = Header(None),
    movie_repository: MovieRepository = Depends(MovieRepository.inject),
):
    films = movie_repository.get_movies()
    context = dict(request=request, films=films)
    if hx_request:
        return templates.TemplateResponse("partials/table.html", context)
    return templates.TemplateResponse("index.html", context)
