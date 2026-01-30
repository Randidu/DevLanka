from sqlalchemy import text
from app.core.database import engine

def migrate_type():
    with engine.begin() as conn:
        try:
            print("Adding type and language columns to resources...")
            # Add type column (e.g. PDF, Video, Course)
            conn.execute(text("ALTER TABLE resources ADD COLUMN type VARCHAR(50)"))
            # Add language column (e.g. English, Sinhala)
            conn.execute(text("ALTER TABLE resources ADD COLUMN language VARCHAR(50) DEFAULT 'English'"))
            print("Migration successful: type and language added.")
        except Exception as e:
            print(f"Migration failed (maybe columns exist?): {e}")

if __name__ == "__main__":
    migrate_type()
