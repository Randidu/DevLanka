$ErrorActionPreference = "Stop"

Write-Host "🚀 DevLanka - Seed Data to Render Database" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "⚠️  Please make sure you have the 'Internal Database URL' from Render." -ForegroundColor Yellow
Write-Host "⚠️  It starts with 'postgres://'" -ForegroundColor Yellow
Write-Host ""

$Confirm = Read-Host "Do you want to proceed? (y/n)"
if ($Confirm -ne 'y') {
    Write-Host "Aborted."
    exit
}

$RenderDB = Read-Host "Please paste your Render Internal Database URL"

# Fix URL for Python (replace postgres:// with postgresql://)
if ($RenderDB -match "^postgres://") {
    $RenderDB = $RenderDB -replace "^postgres://", "postgresql://"
    Write-Host "✅ URL protocol updated to postgresql://" -ForegroundColor Green
}

# Set environment variable specifically for this session
$env:DATABASE_URL = $RenderDB

Write-Host ""
Write-Host "🌱 Seeding database... This might take a few seconds..." -ForegroundColor Magenta
Write-Host ""

try {
    python seed_db.py
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "🎉 SUCCESS! Data has been seeded to Render!" -ForegroundColor Green
        Write-Host "Login credentials:"
        Write-Host "Email: admin@devlanka.com"
        Write-Host "Pass:  admin123"
    } else {
        Write-Host "❌ Python script failed." -ForegroundColor Red
    }
} catch {
    Write-Host "❌ Error: $_" -ForegroundColor Red
} finally {
    # Cleanup env var just in case
    $env:DATABASE_URL = $null
    Write-Host ""
    Write-Host "Done." -ForegroundColor Gray
}
