from sqlalchemy import text
from app.core.database import engine

def add_resource_url():
    with engine.connect() as conn:
        try:
            conn.execute(text("ALTER TABLE pathway_steps ADD COLUMN resource_url VARCHAR;"))
            conn.commit()
            print("Successfully added resource_url column to pathway_steps.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    add_resource_url()
