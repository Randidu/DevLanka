from app.core.database import SessionLocal
from sqlalchemy import text

def check_data():
    db = SessionLocal()
    try:
        # Check tables existence
        tables = db.execute(text("SELECT name FROM sqlite_master WHERE type='table';")).fetchall()
        print(f"Tables found: {[t[0] for t in tables]}")
        
        # Check counts if tables exist
        if any('news' in t[0] for t in tables):
            news_count = db.execute(text("SELECT COUNT(*) FROM news")).scalar()
            print(f"News Count: {news_count}")
        
        if any('users' in t[0] for t in tables):
            user_count = db.execute(text("SELECT COUNT(*) FROM users")).scalar()
            print(f"User Count: {user_count}")

        if any('resources' in t[0] for t in tables):
            res_count = db.execute(text("SELECT COUNT(*) FROM resources")).scalar()
            print(f"Resource Count: {res_count}")
            
    except Exception as e:
        print(f"Error checking DB: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_data()
