from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.core.database import engine, Base
import app.models # Register models

# Import Routes
from app.routes import (
    auth_routes, 
    news_routes, 
    course_routes, 
    youtube_routes, 
    support_routes,
    pathway_routes,
    resource_routes,
    admin_routes,
    upload_routes
)

# Create Database Tables
print("--- STARTING DB CREATION ---")
try:
    Base.metadata.create_all(bind=engine)
    print("--- DB CREATION COMPLETE ---")
except Exception as e:
    print(f"--- DB CREATION FAILED: {e} ---")

app = FastAPI(title="Sri Lanka Tech Learning & News Platform")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins for dev
    allow_origin_regex="https?://.*", # Allow all localhost ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

# Templates
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

# Include Routers
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(news_routes.router, prefix="/api/news", tags=["news"])
app.include_router(course_routes.router, prefix="/api/courses", tags=["courses"])
app.include_router(youtube_routes.router, prefix="/api/tutorials", tags=["tutorials"])
app.include_router(support_routes.router, prefix="/api/support", tags=["support"])
app.include_router(pathway_routes.router, prefix="/api/pathways", tags=["pathways"])
app.include_router(resource_routes.router, prefix="/api/resources", tags=["resources"])
app.include_router(upload_routes.router, prefix="/api/upload", tags=["upload"])
app.include_router(admin_routes.router, prefix="/admin", tags=["admin"])

# --- UI Routes ---

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home - SL Tech Platform"})

@app.get("/news")
async def news_page(request: Request):
    return templates.TemplateResponse("news.html", {"request": request, "title": "Tech News"})

@app.get("/courses")
async def courses_page(request: Request):
    return templates.TemplateResponse("courses.html", {"request": request, "title": "Online Courses"})

@app.get("/tutorials")
async def tutorials_page(request: Request):
    return templates.TemplateResponse("tutorials.html", {"request": request, "title": "YouTube Tutorials"})

@app.get("/support")
async def support_page(request: Request):
    return templates.TemplateResponse("support.html", {"request": request, "title": "Support"})

@app.get("/profile")
async def profile_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request, "title": "My Profile"})

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Login"})

@app.get("/login.html")
async def login_html_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Login"})

@app.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "title": "Register"})

@app.get("/register.html")
async def register_html_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "title": "Register"})

@app.get("/learning-path")
async def learning_path_page(request: Request):
    return templates.TemplateResponse("learning-path.html", {"request": request, "title": "Learning Pathways"})

@app.get("/category")
async def category_page(request: Request):
    return templates.TemplateResponse("category.html", {"request": request, "title": "Resources"})

@app.get("/resource-detail")
async def resource_detail_page(request: Request):
    return templates.TemplateResponse("resource_detail.html", {"request": request, "title": "Resource Details"})

@app.get("/resource_detail.html")
async def resource_detail_html_page(request: Request):
    return templates.TemplateResponse("resource_detail.html", {"request": request, "title": "Resource Details"})

@app.get("/pathways")
async def pathways_page(request: Request):
    return templates.TemplateResponse("pathways.html", {"request": request, "title": "Pathways"})

# Admin routes
@app.get("/admin/dashboard")
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("admin/dashboard.html", {"request": request, "title": "Admin Dashboard"})

@app.get("/admin/manage_content")
async def admin_manage_content(request: Request):
    return templates.TemplateResponse("admin/manage_content.html", {"request": request, "title": "Manage Content"})

@app.get("/admin/manage_categories")
async def admin_manage_categories(request: Request):
    return templates.TemplateResponse("admin/manage_categories.html", {"request": request, "title": "Manage Categories"})

@app.get("/admin/manage_tutorials")
async def admin_manage_tutorials(request: Request):
    return templates.TemplateResponse("admin/manage_tutorials.html", {"request": request, "title": "Manage Tutorials"})

@app.get("/admin/admin_pathways")
async def admin_pathways(request: Request):
    return templates.TemplateResponse("admin/admin_pathways.html", {"request": request, "title": "Manage Pathways"})
