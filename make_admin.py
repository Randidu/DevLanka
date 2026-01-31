import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import User

def make_admin(remote_url, email):
    print(f"Connecting to {remote_url}...")
    try:
        engine = create_engine(remote_url)
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    print(f"Finding user {email}...")
    user = session.query(User).filter(User.email == email).first()
    if not user:
        print(f"User with email {email} not found.")
        return

    print(f"current role: {user.role}")
    user.role = "admin"
    session.commit()
    print(f"Success! User {email} is now an Admin.")
    session.close()

if __name__ == "__main__":
    print("--- Make User Admin ---")
    url = input("Enter Render (External) Database URL: ").strip()
    email = input("Enter Email to promote to Admin: ").strip()
    if url and email:
        make_admin(url, email)
    else:
        print("Missing info.")
