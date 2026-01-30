from sqlalchemy import text
from app.core.database import engine

def add_columns():
    with engine.connect() as conn:
        try:
            conn.execute(text("ALTER TABLE pathways ADD COLUMN icon VARCHAR;"))
            conn.commit()
            print("Successfully added icon column.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    add_columns()
