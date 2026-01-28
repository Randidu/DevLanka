from app.core.database import SessionLocal
from app import crud

def test():
    db = SessionLocal()
    try:
        print("Testing DB connection...")
        cats = crud.resource_category.get_multi(db)
        print(f"Categories: {cats}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test()
