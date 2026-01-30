from app.core.database import SessionLocal
from app.models.resource import ResourceCategory

def seed_categories():
    db = SessionLocal()
    try:
        categories = [
            {
                "name": "Web Development",
                "slug": "web-dev",
                "icon": "https://img.icons8.com/color/96/source-code.png"
            },
            {
                "name": "Mobile Apps",
                "slug": "mobile-apps",
                "icon": "https://img.icons8.com/color/96/android-os.png"
            },
            {
                "name": "Data Science",
                "slug": "data-science",
                "icon": "https://img.icons8.com/color/96/graph-report.png"
            },
            {
                "name": "Cyber Security",
                "slug": "cyber-security",
                "icon": "https://img.icons8.com/color/96/security-shield-green.png"
            },
            {
                "name": "UI/UX Design",
                "slug": "ui-ux",
                "icon": "https://img.icons8.com/color/96/design.png"
            },
             {
                "name": "DevOps",
                "slug": "devops",
                "icon": "https://img.icons8.com/color/96/cloud-sync--v1.png"
            }
        ]
        
        for cat_data in categories:
            cat = db.query(ResourceCategory).filter_by(slug=cat_data["slug"]).first()
            if not cat:
                cat = ResourceCategory(**cat_data)
                db.add(cat)
                print(f"Created category: {cat.name}")
            else:
                # Update icon if it was old (emoji) or None
                if not cat.icon or not cat.icon.startswith('http'):
                    cat.icon = cat_data["icon"]
                    db.add(cat)
                    print(f"Updated icon for: {cat.name}")

        db.commit()
        print("Categories seeded successfully with real icons.")

    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_categories()
