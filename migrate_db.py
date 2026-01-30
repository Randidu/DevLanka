from sqlalchemy import text
from app.core.database import engine

def add_column():
    with engine.connect() as conn:
        try:
            conn.execute(text("ALTER TABLE resources ADD COLUMN is_approved BOOLEAN DEFAULT FALSE;"))
            conn.commit()
            print("Successfully added is_approved column.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    add_column()
