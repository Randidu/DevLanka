import sys
import os
import time

# Add current directory to sys.path
sys.path.append(os.getcwd())

try:
    from app.core.database import Base, engine
    from seed_full_data import seed_full_data
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

def main():
    print("--- CONNECTING TO REMOTE DATABASE ---")
    
    print("1. Creating/Verifying Tables...")
    try:
        # Create tables if they don't exist
        Base.metadata.create_all(bind=engine)
        print("   -> Tables Ready.")
    except Exception as e:
        print(f"   -> Table Creation Failed: {e}")
        return

    print("2. Seeding Data...")
    try:
        # Run the full seeder
        seed_full_data()
        print("   -> Data Seeded Successfully!")
        print("   -> Admin User: admin@devlanka.com")
    except Exception as e:
        print(f"   -> Seeding Failed: {e}")

if __name__ == "__main__":
    main()
