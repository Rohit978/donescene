# ============================================================
#  DoneScene Skills Installer (Windows PowerShell)
# ============================================================
#  Usage:  Right-click -> "Run with PowerShell"
#          or:  powershell -ExecutionPolicy Bypass -File install.ps1
# ============================================================

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  DoneScene Skills Installer" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# --- Resolve paths ---
$ScriptDir   = Split-Path -Parent $MyInvocation.MyCommand.Definition
$SkillsSource = Join-Path $ScriptDir "skills"
$TargetRoot   = Join-Path $env:USERPROFILE ".gemini\antigravity\skills"

if (-not (Test-Path $SkillsSource)) {
    Write-Host "[ERROR] Could not find the 'skills' folder next to this script." -ForegroundColor Red
    Write-Host "        Expected: $SkillsSource" -ForegroundColor Red
    exit 1
}

# --- Create target if needed ---
if (-not (Test-Path $TargetRoot)) {
    Write-Host "[INFO]  Creating Antigravity skills directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $TargetRoot -Force | Out-Null
}

# --- Copy each ds-* skill folder ---
$installed = 0
$skipped   = 0

Get-ChildItem -Path $SkillsSource -Directory -Filter "ds-*" | ForEach-Object {
    $dest = Join-Path $TargetRoot $_.Name
    if (Test-Path $dest) {
        Write-Host "  [SKIP]    $($_.Name) (already exists)" -ForegroundColor DarkGray
        $skipped++
    } else {
        Copy-Item -Path $_.FullName -Destination $dest -Recurse -Force
        Write-Host "  [OK]      $($_.Name)" -ForegroundColor Green
        $installed++
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Done!  Installed: $installed  |  Skipped: $skipped" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Restart Antigravity, then type  /ds  to see all commands." -ForegroundColor Yellow
Write-Host ""
