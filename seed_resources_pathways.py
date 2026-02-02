import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add current directory to sys.path
sys.path.append(os.getcwd())

from app.core.database import Base, engine
from app.models.user import User
from app.models.resource import Resource, ResourceCategory
from app.models.pathway import Pathway, PathwayStep

def seed_more_data():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        print("--- CONNECTING FOR EXTRA SEEDING ---")
        
        # 1. Get Admin User
        admin = db.query(User).filter(User.email == "admin@devlanka.com").first()
        if not admin:
            print("Admin user not found! Please run the main seed script first.")
            return
        
        admin_id = admin.id
        print(f"Using Admin ID: {admin_id}")

        # 2. Seed Resources
        print("Seeding Resources...")
        resources_data = [
            {
                "title": "MDN Web Docs",
                "description": "The best documentation for Web Development (HTML, CSS, JS).",
                "url": "https://developer.mozilla.org/",
                "image_url": "https://developer.mozilla.org/mdn-social-share.cd6c4a5a.png",
                "category": "Documentation",
                "tags": "web, html, css, js",
                "is_approved": True,
                "added_by_id": admin_id
            },
            {
                "title": "Roadmap.sh",
                "description": "Community driven roadmaps, articles and resources for developers.",
                "url": "https://roadmap.sh/",
                "image_url": "https://roadmap.sh/images/og/default.png",
                "category": "Learning",
                "tags": "roadmap, career, guide",
                "is_approved": True,
                "added_by_id": admin_id
            },
            {
                "title": "FreeCodeCamp",
                "description": "Learn to code for free. Build projects. Earn certifications.",
                "url": "https://www.freecodecamp.org/",
                "image_url": "https://design-style-guide.freecodecamp.org/downloads/fcc_primary_large.png",
                "category": "Courses",
                "tags": "free, coding, tutorials",
                "is_approved": True,
                "added_by_id": admin_id
            },
            {
                "title": "Svelte - Cybernetically enhanced web apps",
                "description": "Svelte shifts that work out of the browser, into a compile step that happens when you build your app.",
                "url": "https://svelte.dev",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Svelte_Logo.svg/1200px-Svelte_Logo.svg.png",
                "category": "Frameworks",
                "tags": "javascript, frontend, svelte",
                "is_approved": True,
                "added_by_id": admin_id
            }
        ]

        for res in resources_data:
            exists = db.query(Resource).filter(Resource.url == res["url"]).first()
            if not exists:
                db.add(Resource(**res))
                print(f"   -> Added Resource: {res['title']}")
        
        # 3. Seed Pathways
        print("Seeding Pathways...")
        pathway_data = {
            "title": "Frontend Developer Career Path",
            "description": "A complete guide to becoming a professional Frontend Developer in 2025.",
            "image_url": "https://media.istockphoto.com/id/1189304032/vector/programming-web-banner.jpg?s=612x612&w=0&k=20&c=N5x7c9iX5dE_Fp-GkS5p6P2g3X9pZ6_Z6p2g3X9pZ6=",
            "difficulty_level": "Beginner",
            "estimated_duration": "6 Months",
            "tags": "frontend, web, career",
            "creator_id": admin_id
        }

        # Check if exists
        pathway = db.query(Pathway).filter(Pathway.title == pathway_data["title"]).first()
        if not pathway:
            pathway = Pathway(**pathway_data)
            db.add(pathway)
            db.flush() # to get ID
            print(f"   -> Created Pathway: {pathway.title}")
            
            # Add Steps
            steps = [
                {"title": "Learn HTML & CSS", "description": "Build the structure and style of web pages.", "order": 1, "content_type": "Article", "content_url": "https://developer.mozilla.org/en-US/docs/Learn/HTML"},
                {"title": "Master JavaScript", "description": "The programming language of the web.", "order": 2, "content_type": "Video", "content_url": "https://www.youtube.com/watch?v=PkZNo7MFNFg"},
                {"title": "Learn React", "description": "The most popular frontend library.", "order": 3, "content_type": "Course", "content_url": "https://react.dev/learn"},
                {"title": "Version Control (Git)", "description": "Manage your code with Git & GitHub.", "order": 4, "content_type": "Tool", "content_url": "https://git-scm.com/doc"}
            ]
            
            for s in steps:
                step = PathwayStep(pathway_id=pathway.id, **s)
                db.add(step)
            print("   -> Added Steps to Pathway.")
        
        db.commit()
        print("--- SEEDING COMPLETE! ---")

    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_more_data()
