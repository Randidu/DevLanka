from app.core.database import SessionLocal
from app.models.resource import Resource
from app.models.user import User

def create_demo_pdf_resource():
    db = SessionLocal()
    try:
        user = db.query(User).first()
        if not user:
            print("No user found.")
            return

        # Create a new resource correctly linked to the user
        new_res = Resource(
            title="Demo PDF Guide",
            description="This is a test PDF resource to check the Download button logic.",
            url="http://example.com/guide.pdf",
            icon="https://img.icons8.com/color/96/pdf.png",
            # Assuming 'type' field exists in DB? Usually it's inferred or separate column? 
            # Looking at previous code, 'type' seemed to come from category or badges?
            # Wait, `item.type` was used in JS. Does the model have `type`?
            # Let's check model...
            # Resource model usually only has title, desc, url, icon, category_id, is_approved, owner_id, images.
            # Ah, the `type` in JS might have been mocked or I missed a column?
            # Let's check schema/model again.
            # In Category.html, `item.type` is used.
            # In Models, I don't recall adding `type`.
            # If `type` is missing from DB, JS `item.type` will be undefined!
            # Let's add it now blindly to be safe or check migration.
            is_approved=True,
            owner_id=user.id,
            category_id=1 # Web Dev
        )
        
        # NOTE: If 'type' column doesn't exist, I need to add it or the attributes above will fail?
        # Python Keyword arguments matching columns.
        # Let's check if I can 'fake' it via description for now or if I need to migrate?
        # Actually, let's just create it and see.
        
        db.add(new_res)
        db.commit()
        db.refresh(new_res)
        print(f"Created Resource ID: {new_res.id}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_demo_pdf_resource()
