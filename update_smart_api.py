# Python script to add smart API detection to all HTML files

import os
import re

# Smart API detection code
SMART_API_DETECTION = """        // Smart API URL Detection
        let API_BASE = '';
        const hostname = window.location.hostname;
        const isLocalhost = hostname === '127.0.0.1' || hostname === 'localhost';
        
        if (isLocalhost) {
            // Running locally - use local backend
            API_BASE = 'http://127.0.0.1:8000/api';
            console.log("🔧 Development Mode: using local backend at " + API_BASE);
        } else if (hostname.includes('onrender.com')) {
            // Running on Render - use relative paths
            API_BASE = '/api';
            console.log("🚀 Production Mode (Render): using relative paths");
        } else {
            // Fallback to Render for any other domain
            API_BASE = 'https://devlanka-hub.onrender.com/api';
            console.log("☁️ Fallback: using Render backend at " + API_BASE);
        }"""

SMART_AUTH_DETECTION = """        // Smart API URL Detection
        let AUTH_BASE = '';
        const hostname = window.location.hostname;
        const isLocalhost = hostname === '127.0.0.1' || hostname === 'localhost';
        
        if (isLocalhost) {
            AUTH_BASE = 'http://127.0.0.1:8000';
            console.log("🔧 Development Mode: using local backend");
        } else if (hostname.includes('onrender.com')) {
            AUTH_BASE = '';
            console.log("🚀 Production Mode (Render)");
        } else {
            AUTH_BASE = 'https://devlanka-hub.onrender.com';
            console.log("☁️ Fallback: using Render backend");
        }"""

templates_dir = r'c:\Users\randi\OneDrive\Desktop\DevLanka\app\templates'

# Files that need API_BASE (with /api suffix)
api_files = [
    'pathways.html',
    'learning-path.html',
    'courses.html',
    'create_news.html',
    'news.html',
    'category.html',
    'tutorials.html',
    'trending_detail.html',
    'support.html',
    'resource_detail.html',
    'admin/approvals.html',
    'admin/admin_pathways.html',
    'admin/manage_content.html',
    'admin/manage_categories.html',
    'admin/manage_tutorials.html',
]

# Files that need AUTH_BASE (without /api suffix)
auth_files = [
    'register.html',
    'profile.html',
]

def update_file(filepath, detection_code, pattern):
    """Update a single file with smart API detection"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the API_BASE declaration
        updated = re.sub(pattern, detection_code, content, count=1)
        
        if updated != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"✅ Updated: {os.path.basename(filepath)}")
            return True
        else:
            print(f"⚠️  No change: {os.path.basename(filepath)}")
            return False
    except Exception as e:
        print(f"❌ Error updating {filepath}: {e}")
        return False

# Pattern to match API_BASE declarations
api_pattern = r"const API_BASE = 'https://devlanka-hub\.onrender\.com/api';"

# Pattern to match AUTH_BASE or API_BASE for auth files
auth_pattern = r"(const|let) API_BASE = 'https://devlanka-hub\.onrender\.com';"

print("🚀 Starting smart API detection update...\n")

# Update API files
print("📝 Updating API files...")
for file in api_files:
    filepath = os.path.join(templates_dir, file)
    if os.path.exists(filepath):
        update_file(filepath, SMART_API_DETECTION, api_pattern)
    else:
        print(f"⚠️  File not found: {file}")

print("\n📝 Updating Auth files...")
for file in auth_files:
    filepath = os.path.join(templates_dir, file)
    if os.path.exists(filepath):
        # For profile.html, we need to handle it specially
        update_file(filepath, SMART_AUTH_DETECTION.replace('AUTH_BASE', 'API_BASE'), auth_pattern)
    else:
        print(f"⚠️  File not found: {file}")

print("\n✅ All files updated successfully!")
print("\n🎯 Next steps:")
print("1. Refresh your browser at http://localhost:3000/")
print("2. Check console for '🔧 Development Mode' message")
print("3. Verify data loads correctly")
