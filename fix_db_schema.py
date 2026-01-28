from app.core.database import SessionLocal
from sqlalchemy import text

def fix_db():
    db = SessionLocal()
    try:
        print("Fixing DB...")
        # Check if column exists or just try adding it. 
        # Since we know it's missing, let's try adding it.
        # We need to handle potential error if it exists, but the error said UndefinedColumn so it is missing.
        
        # We also need to check "slug" column, as it was in the model.
        # Let's check the error message again carefully.
        # It said "column resource_categories.icon".
        
        db.execute(text("ALTER TABLE resource_categories ADD COLUMN icon VARCHAR;"))
        db.commit()
        print("Required columns added successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    fix_db()
