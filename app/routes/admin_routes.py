from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()

templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")

@router.get("/")
async def admin_index(request: Request):
    return templates.TemplateResponse("admin/dashboard.html", {"request": request, "title": "Admin Dashboard"})

@router.get("/dashboard.html")
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("admin/dashboard.html", {"request": request, "title": "Admin Dashboard"})

@router.get("/users.html")
async def manage_users(request: Request):
    return templates.TemplateResponse("admin/users.html", {"request": request, "title": "Manage Users"})

@router.get("/manage_content.html")
async def manage_content(request: Request):
    return templates.TemplateResponse("admin/manage_content.html", {"request": request, "title": "Manage Content"})

@router.get("/tickets.html")
async def support_tickets(request: Request):
    return templates.TemplateResponse("admin/tickets.html", {"request": request, "title": "Support Tickets"})

@router.get("/approvals.html")
async def manage_approvals(request: Request):
    return templates.TemplateResponse("admin/approvals.html", {"request": request, "title": "Pending Approvals"})

@router.get("/admin_pathways.html")
async def manage_pathways(request: Request):
    return templates.TemplateResponse("admin/admin_pathways.html", {"request": request, "title": "Manage Pathways"})

@router.get("/add_pathway.html")
async def add_pathway(request: Request):
    return templates.TemplateResponse("admin/add_pathway.html", {"request": request, "title": "Add New Pathway"})

@router.get("/manage_categories.html")
async def manage_categories(request: Request):
    return templates.TemplateResponse("admin/manage_categories.html", {"request": request, "title": "Manage Categories"})

@router.get("/manage_tutorials.html")
async def manage_tutorials(request: Request):
    return templates.TemplateResponse("admin/manage_tutorials.html", {"request": request, "title": "Manage Tutorials"})

@router.get("/upload.html")
async def upload_content(request: Request):
    return templates.TemplateResponse("admin/upload.html", {"request": request, "title": "Upload Content"})
