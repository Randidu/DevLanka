from app.core.database import SessionLocal
from app.models.resource import Resource

def approve_all():
    db = SessionLocal()
    try:
        resources = db.query(Resource).filter(Resource.is_approved == False).all()
        print(f"Found {len(resources)} unapproved resources.")
        for r in resources:
            r.is_approved = True
            print(f"Approving: {r.title}")
        
        db.commit()
        print("All resources approved.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    approve_all()
