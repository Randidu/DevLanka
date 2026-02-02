import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.getcwd())

from app.models.user import User, UserRole

# IMPORTANT: Ensure this matches the REMOTE DB URL
REMOTE_DB_URL = os.environ.get("DATABASE_URL")

def promote_to_admin(email):
    if not REMOTE_DB_URL:
        print("Error: DATABASE_URL not set.")
        return

    print(f"Connecting to DB to promote {email}...")
    engine = create_engine(REMOTE_DB_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            print(f"User not found: {email}")
            print("Please make sure you have registered first.")
            return

        print(f"User found: {user.full_name} (ID: {user.id})")
        
        # Promote to Admin
        user.role = UserRole.ADMIN
        user.is_active = True
        
        db.commit()
        print(f"SUCCESS! User {email} is now an ADMIN.")

    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    target_email = "randidudamith368@gmail.com"
    promote_to_admin(target_email)
