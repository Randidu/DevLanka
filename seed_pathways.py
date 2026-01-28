"""
Seed script to populate the database with sample pathways and steps.
Run this once to initialize your database with learning pathways.
"""
from app.core.database import SessionLocal
from app.crud import pathway as pathway_crud
from app.schemas.pathway import PathwayCreate, PathwayStepCreate


def seed_pathways():
    db = SessionLocal()
    
    try:
        # Check if pathways already exist
        existing = pathway_crud.get_multi(db, limit=1)
        if len(existing) > 0:
            print("✓ Database already has pathways. Skipping seed.")
            return
        
        print("Seeding pathways...")
        
        # Web Development Pathway
        web_pathway = PathwayCreate(
            slug="web-development",
            title="Web Development",
            description="Master Frontend & Backend. Learn HTML, CSS, JS, React, Node.js and more.",
            steps=[
                PathwayStepCreate(
                    step_number=1,
                    title="HTML & CSS Fundamentals",
                    description="Learn the building blocks of the web: HTML for structure and CSS for styling. Master semantic HTML, CSS layouts, flexbox, and grid.",
                    step_type="left",
                    video_id="G3e-cpL7ofc"
                ),
                PathwayStepCreate(
                    step_number=2,
                    title="JavaScript Basics",
                    description="Understand the programming language of the web. Learn variables, functions, arrays, objects, and DOM manipulation.",
                    step_type="right",
                    video_id="W6NZfCO5SIk"
                ),
                PathwayStepCreate(
                    step_number=3,
                    title="Modern JavaScript (ES6+)",
                    description="Master modern JavaScript features like arrow functions, destructuring, spread operator, async/await, and modules.",
                    step_type="left",
                    video_id="NCwa_xi0Uuc"
                ),
                PathwayStepCreate(
                    step_number=4,
                    title="React Framework",
                    description="Build dynamic user interfaces with React. Learn components, props, state, hooks, and the React ecosystem.",
                    step_type="right",
                    video_id="w7ejDZ8SWv8"
                ),
                PathwayStepCreate(
                    step_number=5,
                    title="Backend with Node.js",
                    description="Create server-side applications with Node.js and Express. Learn REST APIs, databases, authentication, and deployment.",
                    step_type="left",
                    video_id="Oe421EPjeBE"
                )
            ]
        )
        pathway_crud.create(db, obj_in=web_pathway)
        print("✓ Created: Web Development pathway")
        
        # Python Pathway
        python_pathway = PathwayCreate(
            slug="python",
            title="Python Developer",
            description="From syntax to Data Science and AI. The complete Python journey.",
            steps=[
                PathwayStepCreate(
                    step_number=1,
                    title="Python Basics",
                    description="Learn Python syntax, variables, data types, operators, and control flow.",
                    step_type="left",
                    video_id="_uQrJ0TkZlc"
                ),
                PathwayStepCreate(
                    step_number=2,
                    title="Object-Oriented Programming",
                    description="Master OOP concepts: classes, objects, inheritance, polymorphism, and encapsulation.",
                    step_type="right",
                    video_id="Ej_02ICOIgs"
                ),
                PathwayStepCreate(
                    step_number=3,
                    title="Python for Data Science",
                    description="Use NumPy, Pandas, and Matplotlib for data analysis and visualization.",
                    step_type="left",
                    video_id="LHBE6Q9XlzI"
                ),
                PathwayStepCreate(
                    step_number=4,
                    title="Machine Learning with Python",
                    description="Build ML models using scikit-learn. Learn regression, classification, and neural networks.",
                    step_type="right",
                    video_id="7eh4d6sabA0"
                )
            ]
        )
        pathway_crud.create(db, obj_in=python_pathway)
        print("✓ Created: Python Developer pathway")
        
        # Mobile Development Pathway
        mobile_pathway = PathwayCreate(
            slug="mobile",
            title="Mobile App Development",
            description="Build iOS and Android apps. Learn Flutter, React Native, or native development.",
            steps=[
                PathwayStepCreate(
                    step_number=1,
                    title="Mobile Development Basics",
                    description="Understand mobile app architecture, UI/UX principles, and platform differences.",
                    step_type="left",
                    video_id="VPvVD8t02U8"
                ),
                PathwayStepCreate(
                    step_number=2,
                    title="Flutter Fundamentals",
                    description="Learn Dart and Flutter to build cross-platform mobile apps with beautiful UIs.",
                    step_type="right",
                    video_id="1ukSR1GRtMU"
                ),
                PathwayStepCreate(
                    step_number=3,
                    title="State Management",
                    description="Master state management in Flutter using Provider, Riverpod, or Bloc.",
                    step_type="left",
                    video_id="cGGOSQpG75k"
                ),
                PathwayStepCreate(
                    step_number=4,
                    title="Backend Integration",
                    description="Connect your app to REST APIs, Firebase, and cloud databases.",
                    step_type="right",
                    video_id="G1L6Z3xwLMY"
                ),
                PathwayStepCreate(
                    step_number=5,
                    title="Publishing Apps",
                    description="Learn to deploy apps to Google Play Store and Apple App Store.",
                    step_type="left",
                    video_id="akFF1uJWZck"
                )
            ]
        )
        pathway_crud.create(db, obj_in=mobile_pathway)
        print("✓ Created: Mobile App Development pathway")
        
        print("\n✅ All pathways seeded successfully!")
        
    except Exception as e:
        print(f"❌ Error seeding pathways: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_pathways()
