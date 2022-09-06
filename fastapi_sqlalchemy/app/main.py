import os
from fastapi import FastAPI, Request, Header
from fastapi.templating import Jinja2Templates

template_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=template_dir)

app = FastAPI()

@app.get("/")
async def home(request: Request, hx_request: str|None = Header(None)):
    films = [
        dict(name="Blade Runner", director="Ridley Scott"),
        dict(name="Endgame", director="Anthony Russo"),
        dict(name="Rocky", director="John G. Avildsen"),
        dict(name="The Matrix", director="The Wachowskis"),
        dict(name="The Terminator", director="James Cameron"),
        dict(name="The Terminator 2: Judgement Day", director="James Cameron"),
        dict(name="The Terminator 3: Rise of the Machines", director="Jonathan Mostow"),
    ]
    context = dict(request=request, films=films)
    if hx_request:
        return templates.TemplateResponse("partials/table.html", context)
    return templates.TemplateResponse("index.html", context)


