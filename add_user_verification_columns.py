from app.core.database import engine
from sqlalchemy import text

def migrate():
    with engine.connect() as conn:
        try:
            conn.execute(text("ALTER TABLE users ADD COLUMN verification_code VARCHAR"))
            print("Added verification_code column")
        except Exception as e:
            print(f"Error adding verification_code column (might already exist): {e}")
        
        try:
            conn.execute(text("ALTER TABLE users ADD COLUMN is_verified BOOLEAN DEFAULT FALSE"))
            print("Added is_verified column")
        except Exception as e:
             print(f"Error adding is_verified column (might already exist): {e}")
        
        conn.commit()

if __name__ == "__main__":
    migrate()
