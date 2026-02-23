# GitHub Actions CI/CD Setup for DamnCRUD

## Overview

This document describes the GitHub Actions CI/CD pipeline configuration for automated testing of the DamnCRUD application.

## Workflow File

**Location:** `.github/workflows/test.yml`

## Trigger Events

The workflow automatically runs on:

1. **Push events** to:
   - `main` branch
   - `develop` branch

2. **Pull Request events** targeting:
   - `main` branch
   - `develop` branch

3. **Manual dispatch** via GitHub Actions UI

## Workflow Jobs

### Job 1: Test Execution

**Environment:** `ubuntu-latest`

#### Services

- **MySQL 8.0**
  - Database: `damncrud`
  - Port: 3306
  - Health checks enabled

#### Steps

1. **Checkout Code**
   - Uses: `actions/checkout@v4`
   - Fetches the repository code

2. **Setup Python**
   - Uses: `actions/setup-python@v5`
   - Python Version: 3.11
   - Caching: pip dependencies

3. **Install System Dependencies**
   - Firefox browser
   - Geckodriver (Firefox WebDriver)

4. **Install Python Dependencies**
   - Upgrades pip
   - Installs from `requirements.txt`

5. **Start Application**
   - Uses Docker Compose
   - Waits 15 seconds for startup
   - Validates application responsiveness

6. **Run Tests**
   - Parallel execution: `pytest -n auto`
   - Generates HTML report
   - Generates JUnit XML report
   - Verbose output

7. **Upload Test Results** (Always runs)
   - Uploads HTML and JUnit reports
   - Retention: 30 days

8. **Upload Screenshots** (On failure)
   - Captures failure screenshots
   - Retention: 7 days

9. **Display Logs** (On failure)
   - Shows Docker Compose logs

10. **Cleanup** (Always runs)
    - Stops Docker containers
    - Removes volumes

### Job 2: Test Summary

**Depends on:** Test job  
**Runs:** Always (even if tests fail)

#### Steps

1. **Download Test Results**
   - Retrieves artifacts from test job

2. **Publish Test Results**
   - Uses: `EnricoMi/publish-unit-test-result-action@v2`
   - Creates test summary in PR
   - Adds check status

## Artifacts

### Test Results

- **Name:** `test-results`
- **Contents:**
  - `report.html` - HTML test report
  - `junit.xml` - JUnit XML report
- **Retention:** 30 days

### Failure Screenshots

- **Name:** `failure-screenshots`
- **Contents:** Screenshots from failed tests
- **Retention:** 7 days
- **Condition:** Only on test failures

## Environment Variables

| Variable         | Value  | Description                |
| ---------------- | ------ | -------------------------- |
| `PYTHON_VERSION` | `3.11` | Python version for testing |

## Parallel Execution

Tests run in parallel using `pytest-xdist`:

- Workers: Auto (based on CPU cores)
- Isolation: Each test gets fresh browser instance
- Conflict prevention: Unique timestamps in test data

## Viewing Results

### In GitHub UI

1. Navigate to **Actions** tab
2. Select the workflow run
3. View job logs and test summary
4. Download artifacts if needed

### In Pull Requests

- Test results automatically posted as PR comment
- Check status shows pass/fail
- Detailed results in workflow run

## Adding Status Badge

Add to your README.md:

```markdown
![Tests](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/test.yml/badge.svg)
```

Replace `YOUR_USERNAME` and `YOUR_REPO` with actual values.

## Local vs CI Differences

| Aspect   | Local           | CI                 |
| -------- | --------------- | ------------------ |
| Browser  | Visible Firefox | Headless Firefox   |
| Database | Local Docker    | GitHub Services    |
| Cleanup  | Manual          | Automatic          |
| Reports  | Local files     | Uploaded artifacts |

## Customization

### Change Python Version

Edit in `.github/workflows/test.yml`:

```yaml
env:
  PYTHON_VERSION: "3.12" # Change version here
```

### Change Test Execution

Modify pytest command:

```yaml
- name: Run tests in parallel with Pytest
  run: |
    pytest -n 4 \  # Fixed 4 workers instead of auto
      --html=report.html \
      --self-contained-html
```

### Add More Triggers

Add to `on:` section:

```yaml
on:
  push:
    branches: [main, develop, feature/*] # Add feature branches
  schedule:
    - cron: "0 2 * * *" # Daily at 2 AM UTC
```

## Troubleshooting

### Tests Fail Only in CI

1. Check for timing issues (add waits)
2. Verify environment differences
3. Review Docker logs in failed run
4. Check screenshot artifacts

### Workflow Doesn't Trigger

1. Verify workflow file is in `.github/workflows/`
2. Check branch names match triggers
3. Ensure workflow file is valid YAML
4. Check repository Actions settings

### Artifacts Not Uploading

1. Verify paths are correct
2. Check files exist after test run
3. Review upload action logs

## Security Considerations

- Secrets: Use GitHub Secrets for sensitive data
- Permissions: Workflow has read/write access
- Dependencies: Pinned versions in `requirements.txt`

## Performance Optimization

Current optimizations:

- ✅ Parallel test execution
- ✅ Pip caching
- ✅ Artifact compression
- ✅ Conditional steps (screenshots only on failure)

Potential improvements:

- 🔧 Docker layer caching
- 🔧 Browser binary caching
- 🔧 Sharded test execution

## Monitoring

Track workflow performance:

- Execution time per job
- Test success rate
- Artifact sizes
- Resource usage

GitHub provides analytics in:

- **Actions** → **Workflows** → Select workflow → **Usage**

## Next Steps

1. ✅ Setup workflow (completed)
2. 🔄 Push to repository
3. 🔍 Verify first run
4. 📊 Review test results
5. 🎯 Add status badge to README

## Support

For issues:

1. Check workflow logs
2. Review test output
3. Download and inspect artifacts
4. Check GitHub Actions documentation

---

**Last Updated:** 2024-02-23  
**Workflow Version:** 1.0
