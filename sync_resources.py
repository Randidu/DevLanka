import sys
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

sys.path.append(os.getcwd())

from app.models.resource import Resource
from app.models.user import User

# Configuration
LOCAL_DB_URL = "postgresql://postgres:Rana%402006@localhost:5432/sl_tech_platform"
# We will use env var or prompt for REMOTE_DB_URL if not set
REMOTE_DB_URL = os.environ.get("DATABASE_URL")

def sync_resources():
    if not REMOTE_DB_URL:
        print("Please set DATABASE_URL environment variable for remote DB")
        return

    print("Connecting to LOCAL DB...")
    local_engine = create_engine(LOCAL_DB_URL)
    LocalSession = sessionmaker(bind=local_engine)
    local_session = LocalSession()

    print("Connecting to REMOTE DB...")
    remote_engine = create_engine(REMOTE_DB_URL)
    RemoteSession = sessionmaker(bind=remote_engine)
    remote_session = RemoteSession()

    try:
        # Get Admin User from Remote to assign as owner
        admin = remote_session.query(User).filter(User.email == "admin@devlanka.com").first()
        if not admin:
            # Fallback to any user
            admin = remote_session.query(User).first()
        
        if not admin:
            print("No users found in remote DB to assign resources to!")
            return
        
        admin_id = admin.id
        print(f"Assigning resources to User ID: {admin_id}")

        # Fetch Local Resources
        local_resources = local_session.query(Resource).all()
        print(f"Found {len(local_resources)} resources in Local DB.")

        count = 0
        for r in local_resources:
            # Check if resource exists in remote (by URL or Title)
            exists = remote_session.query(Resource).filter(
                (Resource.url == r.url) | (Resource.title == r.title)
            ).first()

            if not exists:
                new_resource = Resource(
                    title=r.title,
                    description=r.description,
                    url=r.url,
                    image_url=r.image_url,
                    category=r.category,
                    tags=r.tags,
                    is_approved=r.is_approved,
                    added_by_id=admin_id  # Assign to admin to avoid FK errors
                )
                remote_session.add(new_resource)
                count += 1
                print(f" -> Migrating: {r.title}")
            else:
                print(f" -> Skipped (Exists): {r.title}")
        
        remote_session.commit()
        print(f"Successfully migrated {count} new resources.")

    except Exception as e:
        print(f"Error: {e}")
        remote_session.rollback()
    finally:
        local_session.close()
        remote_session.close()

if __name__ == "__main__":
    sync_resources()
