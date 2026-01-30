# DevLanka Database Backup Script (Windows)
# Run this in PowerShell or Git Bash

Write-Host "🔄 Starting database backup..." -ForegroundColor Cyan

# Configuration
$LOCAL_DB = "sl_tech_platform"
$LOCAL_USER = "postgres"
$TIMESTAMP = Get-Date -Format "yyyyMMdd_HHmmss"
$BACKUP_FILE = "devlanka_backup_$TIMESTAMP.sql"

# Create backup
Write-Host "📦 Creating backup: $BACKUP_FILE" -ForegroundColor Yellow

# Set password environment variable (use your password)
$env:PGPASSWORD = "Rana@2006"

# Run pg_dump
pg_dump -U $LOCAL_USER -d $LOCAL_DB > $BACKUP_FILE

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Backup created successfully: $BACKUP_FILE" -ForegroundColor Green
    Write-Host ""
    Write-Host "📤 To restore to Render database, run:" -ForegroundColor Cyan
    Write-Host "psql <RENDER_DATABASE_URL> < $BACKUP_FILE" -ForegroundColor White
    Write-Host ""
    Write-Host "Example:" -ForegroundColor Yellow
    Write-Host "psql postgresql://user:pass@host.render.com/db < $BACKUP_FILE" -ForegroundColor White
} else {
    Write-Host "❌ Backup failed!" -ForegroundColor Red
    exit 1
}

# Clear password
$env:PGPASSWORD = ""
