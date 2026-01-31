$ErrorActionPreference = "Stop"

Write-Host "🔐 DevLanka - Reset Admin Password on Render" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Enter 'y' to reset 'admin@devlanka.com' password to 'admin123'"

$Confirm = Read-Host "Proceed? (y/n)"
if ($Confirm -ne 'y') { exit }

$RenderDB = Read-Host "Paste Render External Database URL"
if ($RenderDB -match "^postgres://") {
    $RenderDB = $RenderDB -replace "^postgres://", "postgresql://"
}

$env:DATABASE_URL = $RenderDB

Write-Host "Resetting..." -ForegroundColor Magenta
try {
    python reset_admin_password.py
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Password Reset Complete!" -ForegroundColor Green
    }
} catch {
    Write-Host "❌ Error: $_" -ForegroundColor Red
} finally {
    $env:DATABASE_URL = $null
}
