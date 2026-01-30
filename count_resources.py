from app.core.database import SessionLocal
from app.models.resource import Resource

def count_resources():
    db = SessionLocal()
    try:
        count = db.query(Resource).count()
        print(f"Total Resources in DB: {count}")
        all_res = db.query(Resource).all()
        for r in all_res:
             print(f"- {r.title} (Approved: {r.is_approved})")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    count_resources()
