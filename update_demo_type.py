from app.core.database import SessionLocal
from app.models.resource import Resource

def update_demo_type():
    db = SessionLocal()
    try:
        # Find our demo resource
        res = db.query(Resource).filter(Resource.title == "Demo PDF Guide").first()
        if res:
            res.type = "PDF"
            db.commit()
            print("Successfully updated resource type to PDF")
        else:
            print("Demo resource not found!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    update_demo_type()
