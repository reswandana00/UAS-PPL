# DamnCRUD Test Runner - PowerShell Script
# Run Selenium tests using Pytest

param(
    [Parameter(Position = 0)]
    [ValidateSet("all", "parallel", "search", "crud", "validation", "report")]
    [string]$Mode = "all",
    
    [Parameter()]
    [int]$Workers = 0,
    
    [Parameter()]
    [switch]$Verbose
)

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "   DamnCRUD Test Suite - Pytest Execution" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Base pytest command
$pytest_args = @()

if ($Verbose) {
    $pytest_args += "-v"
}

# Execute based on mode
switch ($Mode) {
    "all" {
        Write-Host "📋 Running all tests..." -ForegroundColor Yellow
        pytest @pytest_args
    }
    "parallel" {
        $worker_count = if ($Workers -eq 0) { "auto" } else { $Workers }
        Write-Host "📋 Running tests in parallel with $worker_count workers..." -ForegroundColor Yellow
        pytest -n $worker_count @pytest_args
    }
    "search" {
        Write-Host "📋 Running search tests only..." -ForegroundColor Yellow
        pytest -m search @pytest_args
    }
    "crud" {
        Write-Host "📋 Running CRUD tests only..." -ForegroundColor Yellow
        pytest -m crud @pytest_args
    }
    "validation" {
        Write-Host "📋 Running validation tests only..." -ForegroundColor Yellow
        pytest -m validation @pytest_args
    }
    "report" {
        Write-Host "📋 Running tests with HTML report generation..." -ForegroundColor Yellow
        pytest -n auto --html=report.html --self-contained-html @pytest_args
        if ($LASTEXITCODE -eq 0) {
            Write-Host ""
            Write-Host "✅ Test report generated: report.html" -ForegroundColor Green
        }
    }
}

Write-Host ""
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Tests completed successfully!" -ForegroundColor Green
}
else {
    Write-Host "❌ Some tests failed. Check output above for details." -ForegroundColor Red
}
Write-Host ""

exit $LASTEXITCODE
