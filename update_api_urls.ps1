# PowerShell script to update all localhost API URLs to Render URL

$renderUrl = "https://devlanka-hub.onrender.com"
$templatesPath = "c:\Users\randi\OneDrive\Desktop\DevLanka\app\templates"

# Find all HTML files
$htmlFiles = Get-ChildItem -Path $templatesPath -Filter "*.html" -Recurse

Write-Host "Found $($htmlFiles.Count) HTML files" -ForegroundColor Cyan

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw
    $originalContent = $content
    
    # Replace all localhost URLs
    $content = $content -replace 'http://127\.0\.0\.1:8000', $renderUrl
    $content = $content -replace 'http://localhost:8000', $renderUrl
    
    # Save if changed
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        Write-Host "✓ Updated: $($file.Name)" -ForegroundColor Green
    } else {
        Write-Host "- Skipped: $($file.Name) (no changes)" -ForegroundColor Gray
    }
}

Write-Host "`nAll files updated successfully!" -ForegroundColor Green
Write-Host "New API URL: $renderUrl" -ForegroundColor Yellow
