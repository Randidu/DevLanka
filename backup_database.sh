#!/bin/bash
# DevLanka Database Backup Script
# Run this on your LOCAL machine

echo "🔄 Starting database backup..."

# Configuration
LOCAL_DB="sl_tech_platform"
LOCAL_USER="postgres"
BACKUP_FILE="devlanka_backup_$(date +%Y%m%d_%H%M%S).sql"

# Create backup
echo "📦 Creating backup: $BACKUP_FILE"
pg_dump -U $LOCAL_USER -d $LOCAL_DB > $BACKUP_FILE

if [ $? -eq 0 ]; then
    echo "✅ Backup created successfully: $BACKUP_FILE"
    echo ""
    echo "📤 To restore to Render database, run:"
    echo "psql <RENDER_DATABASE_URL> < $BACKUP_FILE"
    echo ""
    echo "Example:"
    echo "psql postgresql://user:pass@host.render.com/db < $BACKUP_FILE"
else
    echo "❌ Backup failed!"
    exit 1
fi
