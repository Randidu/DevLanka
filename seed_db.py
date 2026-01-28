from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base
from app.models.user import User, UserRole
from app.models.news import News
from app.models.course import Course
from app.models.youtube import Tutorial
from app.models.support import SupportTicket, TicketStatus, TicketPriority
from app.models.resource import Resource, ResourceCategory
from app.models.pathway import Pathway, PathwayStep
import app.models # Ensure all models are registered

def seed_db():
    db = SessionLocal()
    try:
        # Create tables
        Base.metadata.create_all(bind=engine)

        # 1. Seed Users
        admin_user = db.query(User).filter(User.email == "admin@devlanka.com").first()
        if not admin_user:
            admin_user = User(
                full_name="Admin User",
                email="admin@devlanka.com",
                hashed_password="hashed_password_here", # In a real app, use pwd_context.hash()
                role=UserRole.ADMIN,
                is_active=True
            )
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user)

        # 2. Seed News
        if not db.query(News).first():
            news_items = [
                News(
                    title="DeepSeek-V3 Released: A New Era of Open-Source AI",
                    slug="deepseek-v3-released",
                    image_url="https://images.unsplash.com/photo-1677442136019-21780ecad995",
                    short_description="DeepSeek releases its most powerful open-source model yet, challenging industry giants.",
                    content="DeepSeek has officially released its V3 model, showing impressive benchmarks across various coding and reasoning tasks...",
                    category="AI",
                    author_id=admin_user.id
                ),
                News(
                    title="React 19 Stable Version is Now Available",
                    slug="react-19-stable",
                    image_url="https://images.unsplash.com/photo-1633356122544-f134324a6cee",
                    short_description="React 19 brings Actions, useOptimistic, and better server component support.",
                    content="The React team has finally released the stable version of React 19...",
                    category="Web",
                    author_id=admin_user.id
                )
            ]
            db.add_all(news_items)

        # 3. Seed Courses
        if not db.query(Course).first():
            courses = [
                Course(
                    title="Mastering Modern Python",
                    description="Deep dive into Python 3.12+, async programming, and decorators.",
                    instructor="Dr. Aruna Perera",
                    duration="15 hours",
                    level="Intermediate",
                    thumbnail="🐍",
                    url="https://example.com/courses/python",
                    price=0.0,
                    is_free=True
                ),
                Course(
                    title="Frontend Mastery with React & Next.js",
                    description="Learn to build high-performance web apps with the latest technologies.",
                    instructor="Sarah Jayawardena",
                    duration="20 hours",
                    level="Advanced",
                    thumbnail="⚛️",
                    url="https://example.com/courses/frontend",
                    price=2500.0,
                    is_free=False
                )
            ]
            db.add_all(courses)

        # 4. Seed Tutorials
        if not db.query(Tutorial).first():
            tutorials = [
                Tutorial(
                    title="Python for Beginners in Sinhala",
                    description="Learn Python from scratch with step-by-step instructions in Sinhala.",
                    video_id="_uQrJ0TkZlc",
                    duration=3600,
                    thumbnail_url="https://i.ytimg.com/vi/_uQrJ0TkZlc/maxresdefault.jpg",
                    channel_title="Lanka Tech Academy",
                    category="Python"
                ),
                Tutorial(
                    title="React Crash Course 2025",
                    description="Build a full-stack application with React and FastAPI.",
                    video_id="SqcY0GlETPk",
                    duration=5400,
                    thumbnail_url="https://i.ytimg.com/vi/SqcY0GlETPk/maxresdefault.jpg",
                    channel_title="Dev Mastery",
                    category="Web"
                )
            ]
            db.add_all(tutorials)

        # 5. Seed Resource Categories & Resources
        if not db.query(ResourceCategory).first():
            web_cat = ResourceCategory(name="Web Development", slug="web-dev")
            mobile_cat = ResourceCategory(name="Mobile Development", slug="mobile-dev")
            db.add_all([web_cat, mobile_cat])
            db.commit()

            resources = [
                Resource(
                    title="HTML/CSS Cheat Sheet",
                    description="Comprehensive guide to all CSS properties and HTML tags.",
                    url="https://example.com/resources/css-cheatsheet.pdf",
                    icon="📄",
                    category_id=web_cat.id
                ),
                Resource(
                    title="Flutter UI Kit",
                    description="Clean architecture UI components for Flutter apps.",
                    url="https://example.com/resources/flutter-ui-kit.zip",
                    icon="📱",
                    category_id=mobile_cat.id
                )
            ]
            db.add_all(resources)

        # 6. Seed Pathways
        if not db.query(Pathway).first():
            web_pathway = Pathway(
                slug="web-development",
                title="Full-Stack Web Development",
                description="The ultimate guide to becoming a master of the web."
            )
            db.add(web_pathway)
            db.commit()

            steps = [
                PathwayStep(
                    pathway_id=web_pathway.id,
                    step_number=1,
                    title="HTML & CSS Basics",
                    description="Learn how to structure and style your websites.",
                    step_type="left",
                    video_id="qz0aGYrrlhU"
                ),
                PathwayStep(
                    pathway_id=web_pathway.id,
                    step_number=2,
                    title="JavaScript Fundamentals",
                    description="Bring interaction to your pages with JS.",
                    step_type="right",
                    video_id="W6NZfCO5SIk"
                )
            ]
            db.add_all(steps)

        # 7. Seed Support Tickets
        if not db.query(SupportTicket).first():
            tickets = [
                SupportTicket(
                    user_id=admin_user.id,
                    subject="Login issue",
                    message="I cannot login with my existing account.",
                    status=TicketStatus.OPEN,
                    priority=TicketPriority.HIGH
                ),
                SupportTicket(
                    user_id=admin_user.id,
                    subject="Course access",
                    message="I bought the course but it's not showing up.",
                    status=TicketStatus.IN_PROGRESS,
                    priority=TicketPriority.MEDIUM
                )
            ]
            db.add_all(tickets)

        db.commit()
        print("Database seeded successfully!")

    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_db()
