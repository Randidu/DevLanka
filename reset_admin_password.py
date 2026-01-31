from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

def reset_password():
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == "admin@devlanka.com").first()
        if user:
            print(f"User found: {user.email}")
            # Generate new hash using the app's current security config
            new_password = "admin123"
            new_hash = get_password_hash(new_password)
            
            user.hashed_password = new_hash
            db.commit()
            print(f"Password reset successfully for {user.email}")
            print(f"New Password: {new_password}")
        else:
            print("Admin user not found!")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    reset_password()
