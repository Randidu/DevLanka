
from sqlalchemy import create_engine, text
from app.config import settings

def migrate_news_likes():
    engine = create_engine(settings.DATABASE_URL)
    with engine.connect() as conn:
        print("Adding likes column to news table...")
        try:
            conn.execute(text("ALTER TABLE news ADD COLUMN IF NOT EXISTS likes INTEGER DEFAULT 0;"))
            conn.commit()
            print("Successfully added likes column.")
        except Exception as e:
            print(f"Error adding column: {e}")

if __name__ == "__main__":
    migrate_news_likes()
