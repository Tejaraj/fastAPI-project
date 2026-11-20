from fastapi import FastAPI, Request
from snippets import posts
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        request, 
        "home.html", 
        {"posts": posts, "title": "Home"},)


@app.get("/api/posts")
def get_posts():
    return posts