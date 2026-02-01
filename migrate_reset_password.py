
from sqlalchemy import create_engine, text
from app.config import settings

def add_reset_columns():
    engine = create_engine(settings.DATABASE_URL)
    with engine.connect() as conn:
        print("Checking/Adding reset_token column...")
        try:
            conn.execute(text("ALTER TABLE users ADD COLUMN reset_token VARCHAR;"))
            conn.commit()
            print("reset_token column added.")
        except Exception as e:
            print(f"reset_token column might already exist: {e}")

        print("Checking/Adding reset_token_expires column...")
        try:
            conn.execute(text("ALTER TABLE users ADD COLUMN reset_token_expires TIMESTAMP WITHOUT TIME ZONE;"))
            conn.commit()
            print("reset_token_expires column added.")
        except Exception as e:
            print(f"reset_token_expires column might already exist: {e}")

if __name__ == "__main__":
    add_reset_columns()
