from app.core.database import SessionLocal
from sqlalchemy import text

def fix_news_authors():
    db = SessionLocal()
    try:
        print("Fixing news authors...")
        # Update all news with NULL author_id to 1 (Admin/First User)
        db.execute(text("UPDATE news SET author_id = 1 WHERE author_id IS NULL"))
        db.commit()
        print("Updated NULL authors to 1.")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    fix_news_authors()
