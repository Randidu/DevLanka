from sqlalchemy import inspect
from app.core.database import engine

def check_schema():
    inspector = inspect(engine)
    columns = [c['name'] for c in inspector.get_columns('resources')]
    print(f"Columns in 'resources' table: {columns}")
    
    expected = ['owner_id', 'images', 'type', 'language']
    missing = [c for c in expected if c not in columns]
    
    if missing:
        print(f"❌ MISSING COLUMNS: {missing}")
    else:
        print("✅ All columns present.")

if __name__ == "__main__":
    check_schema()
