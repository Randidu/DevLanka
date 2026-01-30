# Seed Data to Render Database
# Run this script to populate your Render PostgreSQL database

Write-Host "🚀 Starting Render Database Seeding..." -ForegroundColor Cyan
Write-Host ""

# Step 1: Backup current .env
Write-Host "📦 Backing up current .env file..." -ForegroundColor Yellow
if (Test-Path .env) {
    Copy-Item .env .env.backup
    Write-Host "✅ Backup created: .env.backup" -ForegroundColor Green
}

# Step 2: Use Render database
Write-Host ""
Write-Host "🔄 Switching to Render database..." -ForegroundColor Yellow
Copy-Item .env.render .env
Write-Host "✅ Now using Render database" -ForegroundColor Green

# Step 3: Run migrations
Write-Host ""
Write-Host "🔨 Running database migrations..." -ForegroundColor Yellow
python migrate_db.py
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Migrations completed" -ForegroundColor Green
} else {
    Write-Host "❌ Migration failed!" -ForegroundColor Red
    Copy-Item .env.backup .env
    exit 1
}

# Step 4: Seed categories
Write-Host ""
Write-Host "📚 Seeding categories..." -ForegroundColor Yellow
python seed_categories.py
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Categories seeded" -ForegroundColor Green
} else {
    Write-Host "⚠️ Categories seeding had issues (might already exist)" -ForegroundColor Yellow
}

# Step 5: Seed pathways
Write-Host ""
Write-Host "🗺️ Seeding pathways..." -ForegroundColor Yellow
python seed_pathways.py
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Pathways seeded" -ForegroundColor Green
} else {
    Write-Host "⚠️ Pathways seeding had issues (might already exist)" -ForegroundColor Yellow
}

# Step 6: Seed other data (if exists)
if (Test-Path seed_data.py) {
    Write-Host ""
    Write-Host "📊 Seeding additional data..." -ForegroundColor Yellow
    python seed_data.py
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Additional data seeded" -ForegroundColor Green
    } else {
        Write-Host "⚠️ Additional data seeding had issues" -ForegroundColor Yellow
    }
}

# Step 7: Restore local .env
Write-Host ""
Write-Host "🔄 Restoring local database configuration..." -ForegroundColor Yellow
Copy-Item .env.backup .env
Remove-Item .env.backup
Write-Host "✅ Local configuration restored" -ForegroundColor Green

Write-Host ""
Write-Host "🎉 Database seeding completed!" -ForegroundColor Green
Write-Host ""
Write-Host "Your Render database now has:" -ForegroundColor Cyan
Write-Host "  ✅ Categories" -ForegroundColor White
Write-Host "  ✅ Pathways" -ForegroundColor White
Write-Host "  ✅ Resources" -ForegroundColor White
Write-Host ""
Write-Host "Visit your deployed site to see the data!" -ForegroundColor Yellow
Write-Host "https://devlanka-hub.onrender.com" -ForegroundColor Cyan
