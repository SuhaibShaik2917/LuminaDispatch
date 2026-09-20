# 1. Find and kill any process using port 5000
Write-Host "Cleaning up port 5000..." -ForegroundColor Cyan
$process = Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue
if ($process) {
    $pid = $process.OwningProcess
    Stop-Process -Id $pid -Force
    Write-Host "Stopped existing bridge (PID: $pid)." -ForegroundColor Yellow
} else {
    Write-Host "Port 5000 is already clear." -ForegroundColor Gray
}

# 2. Start the bridge server
Write-Host "Launching the updated Bridge Server..." -ForegroundColor Cyan
Start-Process python -ArgumentList "C:\Users\notyo\OneDrive\Desktop\EmailDrafts_Copy\bridge.py"

Write-Host "`n=====================================================" -ForegroundColor Green
Write-Host "🚀 SYSTEM REBOOTED SUCCESSFULLY" -ForegroundColor Green
Write-Host "1. Wait 3 seconds for the server to wake up."
Write-Host "2. Refresh your Outreach Portal webpage."
Write-Host "3. Try sending your email again."
Write-Host "=====================================================" -ForegroundColor Green
pause