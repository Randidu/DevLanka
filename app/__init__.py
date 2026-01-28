from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.core.database import engine, Base
from app.routes import (
    auth_routes, 
    home_routes, 
    news_routes, 
    course_routes, 
    youtube_routes, 
    support_routes,
    resource_routes,
    admin_routes
)

def create_app() -> FastAPI:
    # Create Database Tables
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="Sri Lanka Tech Learning & News Platform")

    # Mount static files
    # Note: current directory structure: app/static. __file__ is app/__init__.py
    app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

    # Include Routers
    app.include_router(auth_routes.router, prefix="/api/auth", tags=["auth"])
    app.include_router(home_routes.router, tags=["home"])
    app.include_router(news_routes.router, prefix="/api/news", tags=["news"])
    app.include_router(course_routes.router, prefix="/api/courses", tags=["courses"])
    app.include_router(youtube_routes.router, prefix="/api/tutorials", tags=["tutorials"])
    app.include_router(support_routes.router, prefix="/api/support", tags=["support"])
    app.include_router(resource_routes.router, prefix="/api/resources", tags=["resources"])
    # app.include_router(admin_routes.router, tags=["admin"])

    return app
