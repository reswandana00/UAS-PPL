# DamnCRUD Test Suite with Pytest

Automated test suite for DamnCRUD application using Selenium WebDriver and Pytest with parallel execution support.

## 📋 Test Cases

1. **TC-005**: Search Contact Functionality
2. **TC-006**: Add New Contact with Valid Data
3. **TC-007**: Form Validation - Empty Fields
4. **TC-008**: Update Existing Contact
5. **TC-009**: Delete Contact

## 🚀 Setup

### Prerequisites

- Python 3.8 or higher
- Firefox browser
- Geckodriver (Firefox WebDriver)
- Docker and Docker Compose (for running the application)

### Installation

1. Install Python dependencies:

```bash
cd DamnCRUD/script
pip install -r requirements.txt
```

2. Start the application:

```bash
cd ../
docker-compose up -d
```

## 🧪 Running Tests

### Run All Tests

```bash
pytest
```

### Run Tests in Parallel

Use `-n auto` to automatically detect the number of CPU cores:

```bash
pytest -n auto
```

Or specify the number of workers:

```bash
pytest -n 4
```

### Run Specific Test Categories

Run only CRUD tests:

```bash
pytest -m crud
```

Run only search tests:

```bash
pytest -m search
```

Run only validation tests:

```bash
pytest -m validation
```

### Run Specific Test File

```bash
pytest test_tc_006_tambah_kontak_valid.py
```

### Generate HTML Report

```bash
pytest --html=report.html --self-contained-html
```

### Run with Verbose Output

```bash
pytest -v
```

### Run with Coverage

```bash
pytest --cov=. --cov-report=html
```

## 📊 Test Reports

After running tests with `--html` flag, open `report.html` in your browser to view detailed test results.

## 🔄 CI/CD Integration

This test suite is configured to run automatically on GitHub Actions when:

- Code is pushed to `main` or `develop` branches
- Pull requests are created targeting `main` or `develop`
- Manually triggered via workflow dispatch

### GitHub Actions Workflow

The workflow:

1. Sets up Python environment
2. Installs Firefox and Geckodriver
3. Starts the application using Docker Compose
4. Runs tests in parallel using pytest-xdist
5. Generates and uploads test reports
6. Captures screenshots on failure

## 📁 Project Structure

```
script/
├── conftest.py                          # Pytest fixtures and configuration
├── pytest.ini                           # Pytest settings
├── requirements.txt                     # Python dependencies
├── test_tc_005_search_kontak.py        # Search functionality tests
├── test_tc_006_tambah_kontak_valid.py  # Add contact tests
├── test_tc_007_validasi_field_kosong.py # Validation tests
├── test_tc_008_update_kontak.py        # Update contact tests
├── test_tc_009_delete_kontak.py        # Delete contact tests
└── README_PYTEST.md                     # This file
```

## 🎯 Test Markers

Tests are categorized using pytest markers:

- `@pytest.mark.search` - Search functionality
- `@pytest.mark.crud` - CRUD operations
- `@pytest.mark.validation` - Form validation

## ⚙️ Configuration

### pytest.ini

Configure test behavior in `pytest.ini`:

- Test discovery patterns
- Markers
- Timeout settings
- Logging configuration

### conftest.py

Shared fixtures:

- `driver` - Fresh Firefox WebDriver instance for each test
- `logged_in_driver` - Pre-authenticated WebDriver
- `base_url` - Application base URL

## 🐛 Debugging

### Run Tests with Print Statements

```bash
pytest -s
```

### Run Specific Test Function

```bash
pytest test_tc_006_tambah_kontak_valid.py::test_tambah_kontak_valid
```

### Show Local Variables on Failure

```bash
pytest -l
```

### Drop into Debugger on Failure

```bash
pytest --pdb
```

## 📝 Notes

- Tests use unique timestamps to avoid data conflicts
- Each test gets a fresh browser instance (function scope)
- Tests can run in parallel without interference
- Screenshots are captured on test failures (in CI)

## 🔧 Troubleshooting

### Tests Failing to Connect

Ensure the application is running:

```bash
docker-compose ps
curl http://localhost:8080/login.php
```

### Geckodriver Issues

Install/update geckodriver:

```bash
# Linux/Mac
brew install geckodriver

# Or download from: https://github.com/mozilla/geckodriver/releases
```

### Port Conflicts

If port 8080 is in use, update `docker-compose.yml` or stop conflicting services.

## 📞 Support

For issues or questions, please create an issue in the repository.
