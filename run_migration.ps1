$ErrorActionPreference = "Stop"

Write-Host "--- DevLanka Database Migrator ---" -ForegroundColor Cyan
Write-Host "This script will copy ALL data from your Local DB to Render DB."
Write-Host "WARNING: All existing data on Render will be replaced." -ForegroundColor Yellow

$url = Read-Host "Enter your Render Database External URL"

if ([string]::IsNullOrWhiteSpace($url)) {
    Write-Host "URL cannot be empty." -ForegroundColor Red
    exit
}

# Set environment variable temporarily just in case, though script passes it as arg
$env:DATABASE_URL_RENDER = $url

python migrate_data.py $url

Write-Host "Done! Press Enter to exit..."
Read-Host
