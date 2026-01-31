import sys
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.models import User, News, Course, Tutorial, SupportTicket, Resource, ResourceCategory, Pathway, PathwayStep
from app.core.database import Base

def migrate(remote_url):
    print(f"Connecting to LOCAL DB: {settings.DATABASE_URL}")
    local_engine = create_engine(settings.DATABASE_URL)
    LocalSession = sessionmaker(bind=local_engine)
    local_session = LocalSession()

    print(f"Connecting to REMOTE DB: {remote_url}")
    remote_engine = create_engine(remote_url)
    RemoteSession = sessionmaker(bind=remote_engine)
    remote_session = RemoteSession()

    # Verify connection
    try:
        local_session.execute(text("SELECT 1"))
        remote_session.execute(text("SELECT 1"))
        print("Connections verified.")
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    print("--- CLEARING REMOTE DATABASE ---")
    # Drop all and recreate to ensure clean slate
    print("Dropping tables...")
    Base.metadata.drop_all(bind=remote_engine)
    print("Creating tables...")
    Base.metadata.create_all(bind=remote_engine)
    print("Remote tables recreated.")

    # Data Transfer Order (Parents first to satisfy Foreign Keys)
    transfer_order = [
         User, ResourceCategory, Pathway, Course, Tutorial,
         News, SupportTicket, Resource, PathwayStep
    ]

    print("--- TRANSFERRING DATA ---")
    try:
        for model in transfer_order:
            model_name = model.__name__
            print(f"Migrating {model_name}...", end=" ")
            
            objects = local_session.query(model).all()
            count = len(objects)
            
            # We must expunge objects from local session to add to remote
            for obj in objects:
                local_session.expunge(obj)
                remote_session.merge(obj)
            
            # Flush after each model to ensure IDs are available for next
            remote_session.flush()
            print(f"({count} records)")

        remote_session.commit()
        print("\n--- MIGRATION SUCCESSFUL! ---")
        print("Your local data has been fully transferred to Render.")
        
    except Exception as e:
        print(f"\nMigration failed: {e}")
        remote_session.rollback()
    finally:
        local_session.close()
        remote_session.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        remote = sys.argv[1]
    else:
        print("\nNOTE: You can find your Render Database URL in the Render Dashboard -> Database -> Internal URL (or External if running from PC)")
        remote = input("Enter Render (External) Database URL: ").strip()
    
    if not remote.startswith("postgres"):
        print("Invalid URL. It must start with postgresql://")
    else:
        migrate(remote)
