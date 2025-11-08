#!/usr/bin/env pwsh
# Script to generate Basic Auth header for MCP SSE connection
# Usage: .\generate-auth-header.ps1 -Username "admin" -Password "YourPassword"

param(
    [Parameter(Mandatory=$true)]
    [string]$Username,

    [Parameter(Mandatory=$true)]
    [string]$Password
)

Write-Host "Generating Basic Auth header..." -ForegroundColor Cyan
Write-Host ""

$credentials = "${Username}:${Password}"
$bytes = [System.Text.Encoding]::UTF8.GetBytes($credentials)
$base64 = [Convert]::ToBase64String($bytes)
$authHeader = "Basic $base64"

Write-Host "✅ Generated Authorization header:" -ForegroundColor Green
Write-Host $authHeader -ForegroundColor Yellow
Write-Host ""

Write-Host "Add this to your mcp.json configuration:" -ForegroundColor Cyan
Write-Host @"
{
  "servers": {
    "plane": {
      "url": "https://your-server-url:9000/sse",
      "headers": {
        "Authorization": "$authHeader"
      }
    }
  }
}
"@ -ForegroundColor White
