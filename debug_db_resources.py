from app.core.database import SessionLocal
from app import crud

def test():
    db = SessionLocal()
    try:
        print("Testing DB connection...")
        # Check resources table access
        res = crud.resource.get_multi(db)
        print(f"Resources: {res}")
    except Exception as e:
        print(f"Error: {e}")
        # If it fails, we know we need to fix resources table too
    finally:
        db.close()

if __name__ == "__main__":
    test()
