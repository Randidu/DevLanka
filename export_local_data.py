import json
import os
import sys
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Ensure app can be imported
sys.path.append(os.getcwd())

from app.models.resource import Resource
from app.models.pathway import Pathway, PathwayStep
# Import other models if needed
from app.models.user import User

# Connect to LOCAL PostgreSQL DB (Default from config.py)
# Trying user provided creds with url encoding: postgres:Rana%402006@localhost/sl_tech_platform
# URL Encoding @ in password as %40
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Rana%402006@localhost:5432/sl_tech_platform"
# If this fails, we might need to ask user for credentials
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def export_data():
    db = SessionLocal()
    data = {}
    
    print(f"Exporting Resources from {SQLALCHEMY_DATABASE_URL}...")
    try:
        resources = db.query(Resource).all()
        data['resources'] = []
        for r in resources:
            db.refresh(r) # Try to ensure loaded
            data['resources'].append({
                'title': r.title,
                'description': r.description,
                'url': r.url,
                'image_url': r.image_url,
                'category': r.category,
                'tags': r.tags,
                'added_by_id': r.added_by_id, 
                'is_approved': r.is_approved
            })
        print(f"Found {len(data['resources'])} Resources.")
    except Exception as e:
        print(f"Error exporting resources: {e}")
        data['resources'] = []

    print("Exporting Pathways...")
    try:
        pathways = db.query(Pathway).all()
        data['pathways'] = []
        for p in pathways:
            steps = []
            try:
                for s in p.steps:
                    steps.append({
                        'title': s.title,
                        'description': s.description,
                        'content_type': s.content_type,
                        'content_url': s.content_url,
                        'order': s.order
                    })
            except:
                pass # Steps might fail if schema mismatch
                
            data['pathways'].append({
                'title': p.title,
                'description': p.description,
                'image_url': p.image_url,
                'difficulty_level': p.difficulty_level,
                'estimated_duration': p.estimated_duration,
                'tags': p.tags,
                'creator_id': p.creator_id,
                'steps': steps
            })
        print(f"Found {len(data['pathways'])} Pathways.")
    except Exception as e:
        print(f"Error exporting pathways: {e}")
        data['pathways'] = []

    with open('local_data_dump.json', 'w') as f:
        json.dump(data, f, default=json_serial, indent=4)
    
    print("Data exported to local_data_dump.json")

if __name__ == "__main__":
    export_data()
