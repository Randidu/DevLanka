from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.pathway import Pathway, PathwayStep

def seed_pathways():
    db = SessionLocal()
    try:
        # Check if python pathway exists
        existing = db.query(Pathway).filter_by(slug="python-mastery").first()
        if existing:
            print("Python pathway already exists.")
        else:
            python_path = Pathway(
                title="Python Mastery 2025",
                slug="python-mastery",
                description="From absolute beginner to advanced Python developer.",
                icon="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
            )
            db.add(python_path)
            db.commit()
            db.refresh(python_path)
            
            steps = [
                {
                    "step_number": 1,
                    "title": "Introduction to Python",
                    "description": "Learn the basics: Variables, Loops, and Functions.",
                    "video_id": "_uQrJ0TkZlc", # Mosh Python
                    "resource_url": "https://docs.python.org/3/tutorial/index.html",
                    "step_type": "left"
                },
                {
                    "step_number": 2,
                    "title": "Object Oriented Programming",
                    "description": "Deep dive into Classes, Objects, Inheritance, and Polymorphism.",
                    "video_id": "JeznW_7DlB0",
                    "resource_url": "https://realpython.com/python3-object-oriented-programming/",
                    "step_type": "right"
                },
                {
                    "step_number": 3,
                    "title": "Data Structures & Algorithms",
                    "description": "Master Lists, Sets, Dictionaries, and Algorithms.",
                    "video_id": "pkYVOmU3MgA",
                    "resource_url": "https://www.geeksforgeeks.org/python-data-structures/",
                    "step_type": "left"
                },
                {
                    "step_number": 4,
                    "title": "Web Development with Django",
                    "description": "Build robust web applications using the Django framework.",
                    "video_id": "F5mRW0jo-U4",
                    "resource_url": "https://docs.djangoproject.com/en/5.0/",
                    "step_type": "right"
                }
            ]
            
            for s in steps:
                step = PathwayStep(pathway_id=python_path.id, **s)
                db.add(step)
            
            db.commit()
            print("Created Python Mastery Pathway")

        # Check if Flutter pathway exists
        existing_flutter = db.query(Pathway).filter_by(slug="flutter-dev").first()
        if existing_flutter:
             print("Flutter pathway already exists.")
        else:
            flutter_path = Pathway(
                title="Flutter App Development",
                slug="flutter-dev",
                description="Build beautiful native apps for iOS and Android.",
                icon="https://storage.googleapis.com/cms-storage-bucket/0dbfcc7a59cd1cf16282.png"
            )
            db.add(flutter_path)
            db.commit()
            db.refresh(flutter_path)
            
            steps = [
                {
                    "step_number": 1,
                    "title": "Dart Fundamentals",
                    "description": "Learn the language behind Flutter.",
                    "video_id": "Ej_Pcr4uC2Q",
                    "resource_url": "https://dart.dev/guides",
                    "step_type": "left"
                },
                {
                    "step_number": 2,
                    "title": "Flutter Basics & Widgets",
                    "description": "Understand the Widget tree and basic UI components.",
                    "video_id": "1xipg02Wu8s", 
                    "resource_url": "https://docs.flutter.dev/ui/widgets",
                    "step_type": "right"
                },
                 {
                    "step_number": 3,
                    "title": "State Management (Provider)",
                    "description": "Managing app state efficiently.",
                    "video_id": "Last_Video_ID", 
                    "resource_url": "https://docs.flutter.dev/data-and-backend/state-mgmt/simple",
                    "step_type": "left"
                }
            ]
             
            for s in steps:
                step = PathwayStep(pathway_id=flutter_path.id, **s)
                db.add(step)
            
            db.commit()
            print("Created Flutter Pathway")
            
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_pathways()
