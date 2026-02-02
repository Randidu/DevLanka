import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.getcwd())

from app.models.user import User, UserRole
from app.core.security import get_password_hash

# IMPORTANT: Ensure this matches the REMOTE DB URL
REMOTE_DB_URL = os.environ.get("DATABASE_URL")

def reset_password(email, new_password):
    if not REMOTE_DB_URL:
        print("Error: DATABASE_URL not set.")
        return

    print(f"Connecting to DB to reset password for {email}...")
    engine = create_engine(REMOTE_DB_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            print(f"User not found: {email}")
            # Optional: Create user if not exists?
            # For now, let's assume user exists from the dump
            return

        print(f"User found: {user.full_name} (ID: {user.id})")
        
        # Update Password
        user.hashed_password = get_password_hash(new_password)
        # Ensure they are Admin
        user.role = UserRole.ADMIN
        user.is_active = True
        
        db.commit()
        print(f"SUCCESS! Password for {email} has been reset to '{new_password}'.")
        print("You can now login with this password.")

    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    target_email = "randidudamsith55@gmail.com" # Corrected spelling based on logs
    target_password = "admin123"
    reset_password(target_email, target_password)
