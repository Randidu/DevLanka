from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
from app.models.resource import Resource, ResourceCategory

def seed_data():
    db = SessionLocal()
    try:
        # Check/Create Categories
        categories = [
            {"name": "Web Development", "slug": "web-dev", "icon": "🌐"},
            {"name": "Mobile Apps", "slug": "mobile-apps", "icon": "📱"},
            {"name": "Data Science", "slug": "data-science", "icon": "📊"},
            {"name": "Cyber Security", "slug": "cyber-security", "icon": "🔒"}
        ]
        
        cat_map = {}
        for cat_data in categories:
            cat = db.query(ResourceCategory).filter_by(slug=cat_data["slug"]).first()
            if not cat:
                cat = ResourceCategory(**cat_data)
                db.add(cat)
                db.commit()
                db.refresh(cat)
            cat_map[cat.slug] = cat.id

        # Create Resources
        resources = [
            {
                "title": "Complete Python Roadmap 2025",
                "description": "A comprehensive guide to mastering Python from scratch to advanced level.",
                "url": "https://roadmap.sh/python",
                "icon": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
                "category_id": cat_map.get("web-dev", 1), # Fallback
                "is_approved": True
            },
            {
                "title": "React.js Cheatsheet",
                "description": "Quick reference for React hooks, components, and lifecycle methods.",
                "url": "https://react.dev/",
                "icon": "https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg",
                "category_id": cat_map.get("web-dev", 1),
                "is_approved": True
            },
            {
                "title": "Flutter Component Library",
                "description": "Pre-built widgets for fast mobile app development.",
                "url": "https://flutter.dev",
                "icon": "https://storage.googleapis.com/cms-storage-bucket/0dbfcc7a59cd1cf16282.png",
                "category_id": cat_map.get("mobile-apps", 2),
                "is_approved": False # Pending approval demo
            },
             {
                "title": "Dark Mode UI Kit",
                "description": "High quality UI kit for designing modern dashboards.",
                "url": "https://figma.com",
                "icon": "https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg",
                "category_id": cat_map.get("web-dev", 1),
                "is_approved": True
            }
        ]

        count = 0
        for res_data in resources:
            exists = db.query(Resource).filter_by(title=res_data["title"]).first()
            if not exists:
                res = Resource(**res_data)
                db.add(res)
                count += 1
        
        db.commit()
        print(f"Successfully added {count} new resources.")
    
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
