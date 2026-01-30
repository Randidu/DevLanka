from app.core.database import SessionLocal
from app.models.user import User, UserRole
from app.models.news import News
from app.models.course import Course
from app.models.youtube import Tutorial
from app.core.security import get_password_hash
from datetime import datetime

def seed_full_data():
    db = SessionLocal()
    try:
        print("Starting data seeding...")

        # 1. Seed Admin User
        admin_email = "admin@devlanka.com"
        admin = db.query(User).filter(User.email == admin_email).first()
        if not admin:
            admin = User(
                full_name="Admin User",
                email=admin_email,
                hashed_password=get_password_hash("admin123"),
                is_active=True,
                role=UserRole.ADMIN,
                avatar="https://ui-avatars.com/api/?name=Admin+User&background=3b82f6&color=fff"
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
            print(f"Created Admin: {admin.email}")
        else:
            print("Admin already exists.")

        # 2. Seed News
        news_items = [
            {
                "title": "Sri Lanka's First AI Innovation Hub Launches in Colombo",
                "slug": "sl-ai-hub-launch",
                "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995",
                "short_description": "A major milestone for the local tech industry as the new AI center opens its doors.",
                "content": "<p>Colombo witnesses a technological leap with the inauguration of the AI Innovation Hub...</p>",
                "category": "AI News",
                "author_id": admin.id
            },
            {
                "title": "Top 10 Web Development Trends for 2025",
                "slug": "web-dev-trends-2025",
                "image_url": "https://images.unsplash.com/photo-1498050108023-c5249f4df085",
                "short_description": "From WebAssembly to Edge Computing, here's what to expect in the web world.",
                "content": "<p>As we move into 2025, the web development landscape is shifting rapidly...</p>",
                "category": "Web Development",
                "author_id": admin.id
            },
            {
                "title": "Flutter vs React Native: The Battle Continues",
                "slug": "flutter-vs-react-native-2025",
                "image_url": "https://images.unsplash.com/photo-1551650975-87deedd944c3",
                "short_description": "Which framework should you choose for your next mobile app project?",
                "content": "<p>Choosing between Flutter and React Native remains a tough decision for developers...</p>",
                "category": "Mobile Dev",
                "author_id": admin.id
            }
        ]

        for item in news_items:
            existing = db.query(News).filter(News.slug == item["slug"]).first()
            if not existing:
                db.add(News(**item))
                print(f"Added News: {item['title']}")

        # 3. Seed Courses
        courses = [
            {
                "title": "Full Stack Web Development Bootcamp",
                "description": "Master HTML, CSS, JavaScript, React, and Node.js in this comprehensive course.",
                "instructor": "Dr. Angela Yu",
                "duration": "50 Hours",
                "level": "Beginner to Pro",
                "thumbnail": "https://img-c.udemycdn.com/course/750x422/1565838_e54e_18.jpg",
                "url": "https://www.udemy.com/course/the-complete-web-development-bootcamp/",
                "price": 29.99,
                "is_free": False
            },
            {
                "title": "Python for Data Science and Machine Learning",
                "description": "Learn how to use NumPy, Pandas, Seaborn, Matplotlib, and Scikit-Learn.",
                "instructor": "Jose Portilla",
                "duration": "25 Hours",
                "level": "Intermediate",
                "thumbnail": "https://img-c.udemycdn.com/course/750x422/903744_8eb2.jpg",
                "url": "https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/",
                "price": 0.0,
                "is_free": True
            },
            {
                "title": "The Complete Flutter Development Bootcamp with Dart",
                "description": "Officially created in collaboration with the Google Flutter team.",
                "instructor": "Dr. Angela Yu",
                "duration": "28 Hours",
                "level": "Beginner",
                "thumbnail": "https://img-c.udemycdn.com/course/750x422/2259120_305f_6.jpg",
                "url": "https://www.udemy.com/course/flutter-bootcamp-with-dart/",
                "price": 19.99,
                "is_free": False
            }
        ]

        for course in courses:
            existing = db.query(Course).filter(Course.title == course["title"]).first()
            if not existing:
                db.add(Course(**course))
                print(f"Added Course: {course['title']}")

        # 4. Seed Tutorials
        tutorials = [
            {
                "title": "Python Tutorial for Beginners - Full Course",
                "description": "Learn Python programming in this full tutorial course for beginners.",
                "video_id": "_uQrJ0TkZlc",
                "duration": 22000,
                "thumbnail_url": "https://i.ytimg.com/vi/_uQrJ0TkZlc/maxresdefault.jpg",
                "channel_title": "Programming with Mosh",
                "view_count": 35000000,
                "category": "Python"
            },
            {
                "title": "React Course - Beginner's Guide to React & Redux",
                "description": "A full course to learn React.js from scratch.",
                "video_id": "bMknfKXIFA8",
                "duration": 36000,
                "thumbnail_url": "https://i.ytimg.com/vi/bMknfKXIFA8/maxresdefault.jpg",
                "channel_title": "freeCodeCamp.org",
                "view_count": 5000000,
                "category": "Web"
            },
            {
                "title": "Flutter Tutorial for Beginners",
                "description": "Build iOS and Android Apps with Google's Flutter & Dart.",
                "video_id": "PL4cUxeGkcC9jLYyp2Aoh6hcWuxFDX6PBJ", # Playlist ID actually, but using a single video ID for demo
                "video_id": "1xipg02Wu8s",
                "duration": 1800,
                "thumbnail_url": "https://i.ytimg.com/vi/1xipg02Wu8s/maxresdefault.jpg",
                "channel_title": "The Net Ninja",
                "view_count": 800000,
                "category": "Mobile"
            }
        ]

        for tut in tutorials:
            existing = db.query(Tutorial).filter(Tutorial.video_id == tut["video_id"]).first()
            if not existing:
                db.add(Tutorial(**tut))
                print(f"Added Tutorial: {tut['title']}")

        db.commit()
        print("Data seeding completed successfully!")

    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_full_data()
