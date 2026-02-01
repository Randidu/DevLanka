
from sqlalchemy import create_engine, text
from app.config import settings

def create_comments_table():
    engine = create_engine(settings.DATABASE_URL)
    with engine.connect() as conn:
        print("Creating comments table...")
        try:
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS comments (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    author_id INTEGER REFERENCES users(id),
                    news_id INTEGER REFERENCES news(id)
                );
            """))
            conn.commit()
            print("comments table created.")
        except Exception as e:
            print(f"Error creating comments table: {e}")

if __name__ == "__main__":
    create_comments_table()
