from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home - DevLanka Hub"})

@router.get("/news")
async def news_page(request: Request):
    return templates.TemplateResponse("news.html", {"request": request, "title": "Tech News"})

@router.get("/courses")
async def courses_page(request: Request):
    return templates.TemplateResponse("courses.html", {"request": request, "title": "Courses"})

@router.get("/tutorials")
async def tutorials_page(request: Request):
    return templates.TemplateResponse("tutorials.html", {"request": request, "title": "YouTube Tutorials"})

@router.get("/support")
async def support_page(request: Request):
    return templates.TemplateResponse("support.html", {"request": request, "title": "Support"})

@router.get("/profile")
async def profile_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request, "title": "My Profile"})

@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Login"})

@router.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "title": "Register"})

@router.get("/learning-path")
async def learning_path_page(request: Request):
    return templates.TemplateResponse("learning-path.html", {"request": request, "title": "Learning Pathways"})

@router.get("/pathways")
async def pathways_page(request: Request):
    return templates.TemplateResponse("pathways.html", {"request": request, "title": "Pathways"})

@router.get("/category")
async def category_page(request: Request):
    return templates.TemplateResponse("category.html", {"request": request, "title": "Resource Category"})
