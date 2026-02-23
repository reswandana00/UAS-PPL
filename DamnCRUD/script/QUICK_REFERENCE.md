# Quick Reference Guide - DamnCRUD Pytest Test Suite

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd DamnCRUD/script
pip install -r requirements.txt
```

### 2. Start Application

```bash
cd ../
docker-compose up -d
```

### 3. Run Tests

```bash
cd script
pytest
```

## 📝 Common Commands

### Basic Test Execution

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest test_tc_006_tambah_kontak_valid.py

# Run specific test function
pytest test_tc_006_tambah_kontak_valid.py::test_tambah_kontak_valid
```

### Parallel Execution

```bash
# Auto-detect CPU cores
pytest -n auto

# Use specific number of workers
pytest -n 4
```

### Category-based Execution

```bash
# Search tests only
pytest -m search

# CRUD tests only
pytest -m crud

# Validation tests only
pytest -m validation
```

### Report Generation

```bash
# Generate HTML report
pytest --html=report.html --self-contained-html

# Generate JUnit XML report
pytest --junitxml=junit.xml

# Both reports
pytest --html=report.html --junitxml=junit.xml
```

### Using Helper Scripts

#### PowerShell (Windows)

```powershell
# Run all tests
.\run_pytest.ps1

# Run in parallel
.\run_pytest.ps1 -Mode parallel

# Run specific category
.\run_pytest.ps1 -Mode crud

# Generate report
.\run_pytest.ps1 -Mode report

# Verbose output
.\run_pytest.ps1 -Verbose
```

#### Python Script

```bash
# Run all tests
python run_pytest.py

# Run in parallel
python run_pytest.py --mode parallel

# Run specific category
python run_pytest.py --mode search

# Generate report
python run_pytest.py --mode report

# With verbose
python run_pytest.py --mode all -v
```

## 🔍 Test Categories

| Marker       | Description                  | Tests                  |
| ------------ | ---------------------------- | ---------------------- |
| `search`     | Search functionality         | TC-005                 |
| `crud`       | Create, Read, Update, Delete | TC-006, TC-008, TC-009 |
| `validation` | Form validation              | TC-007                 |

## 📊 Understanding Test Output

### Success Output

```
test_tc_006_tambah_kontak_valid.py::test_tambah_kontak_valid PASSED [100%]
✓ PASS: Data kontak berhasil tersimpan dan muncul di dashboard
```

### Failure Output

```
test_tc_006_tambah_kontak_valid.py::test_tambah_kontak_valid FAILED [100%]
AssertionError: Data kontak tidak ditemukan di tabel setelah disimpan
📸 Screenshot saved: screenshots/test_tc_006_tambah_kontak_valid_20240223_143022.png
```

## 🐛 Debugging Tips

### Show Print Statements

```bash
pytest -s
```

### Show Local Variables on Failure

```bash
pytest -l
```

### Drop to Debugger on Failure

```bash
pytest --pdb
```

### Run Last Failed Tests

```bash
pytest --lf
```

### Run Failed Tests First

```bash
pytest --ff
```

## 🎯 CI/CD Integration

### GitHub Actions automatically runs when:

- ✅ Push to `main` or `develop` branch
- ✅ Pull Request to `main` or `develop`
- ✅ Manual trigger via Actions tab

### View Results:

1. Go to **Actions** tab in GitHub repository
2. Click on the latest workflow run
3. Download artifacts for detailed reports

## 📁 Generated Files

After running tests, you may see:

- `report.html` - HTML test report
- `junit.xml` - JUnit XML report
- `screenshots/` - Screenshots from failed tests
- `.pytest_cache/` - Pytest cache (gitignored)

## ⚠️ Common Issues

### Issue: "No module named pytest"

**Solution:**

```bash
pip install -r requirements.txt
```

### Issue: "Connection refused to localhost:8080"

**Solution:**

```bash
# Start the application
cd DamnCRUD
docker-compose up -d

# Verify it's running
docker-compose ps
curl http://localhost:8080/login.php
```

### Issue: "Geckodriver not found"

**Solution:**

```bash
# Windows (with Chocolatey)
choco install selenium-gecko-driver

# macOS
brew install geckodriver

# Linux
sudo apt-get install firefox-geckodriver
```

### Issue: Tests fail in parallel

**Solution:**
Each test uses unique timestamps to avoid conflicts. If still failing, run sequentially:

```bash
pytest -n 1
```

## 📞 Need Help?

Check the detailed documentation:

- [README_PYTEST.md](README_PYTEST.md) - Full documentation
- [GitHub Workflow](.github/workflows/test.yml) - CI/CD configuration
- [Pytest Docs](https://docs.pytest.org/) - Official Pytest documentation

---

**Happy Testing! 🎉**
