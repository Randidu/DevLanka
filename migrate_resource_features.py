from sqlalchemy import text
from app.core.database import engine

def migrate():
    with engine.begin() as conn:
        try:
            # 1. Add owner_id column
            print("Adding owner_id column to resources...")
            conn.execute(text("ALTER TABLE resources ADD COLUMN owner_id INTEGER REFERENCES users(id)"))
            
            # 2. Add images column (storing as JSON string or comma-separated)
            print("Adding images column to resources...")
            conn.execute(text("ALTER TABLE resources ADD COLUMN images TEXT"))

            print("Migration successful columns added.")
        except Exception as e:
            print(f"Migration failed (maybe columns exist?): {e}")

if __name__ == "__main__":
    migrate()
