from app.core.database import SessionLocal
from app.models.resource import Resource
from app.models.user import User

def seed_images():
    db = SessionLocal()
    try:
        # Get the first user
        user = db.query(User).first()
        if not user:
            print("No users found to assign ownership.")
            return

        # Get first resource
        resource = db.query(Resource).first()
        if resource:
            # Assign owner
            resource.owner_id = user.id
            
            # Add some dummy template images
            images = [
                "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1504639725590-34d0984388bd?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1555099962-4199c345e5dd?auto=format&fit=crop&w=1200&q=80"
            ]
            # Store as simple comma separated for my simple frontend logic
            # OR JSON string if I used JSON.parse in frontend.
            # My frontend code tries JSON.parse then split(','). 
            # Let's use JSON format string.
            import json
            resource.images = json.dumps(images)
            
            db.commit()
            print(f"Updated resource '{resource.title}' with 3 images and owner '{user.full_name}'")
        else:
            print("No resources found.")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_images()
