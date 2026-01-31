import sys
from sqlalchemy import create_engine, text

def fix_sequences(db_url):
    print(f"Connecting to DB...")
    engine = create_engine(db_url)
    
    # List of tables to fix
    tables = [
        'users', 
        'news', 
        'courses', 
        'tutorials', 
        'resources', 
        'resource_categories', 
        'pathways', 
        'pathway_steps', 
        'support_tickets'
    ]

    with engine.connect() as conn:
        print("Fixing sequences...")
        for t in tables:
            try:
                # Construct SQL to reset sequence to max(id)
                # This works for standard Postgres serial columns
                sql = text(f"SELECT setval(pg_get_serial_sequence('{t}', 'id'), COALESCE(MAX(id), 0) + 1, false) FROM {t};")
                conn.execute(sql)
                print(f"  ✓ Fixed {t}")
            except Exception as e:
                print(f"  ⚠ Could not fix {t} (might not have serial id or empty): {e}")
        
        conn.commit()
    print("Done!")

if __name__ == "__main__":
    print("--- Fix Database Sequences ---")
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter Render (External) Database URL: ").strip()
    
    if url:
        fix_sequences(url)
