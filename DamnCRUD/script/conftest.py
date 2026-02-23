"""
Pytest configuration and fixtures for DamnCRUD test suite
"""
import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    """
    Initialize Firefox WebDriver for each test
    Automatically cleans up after test completion
    """
    firefox_options = Options()
    # Enable headless mode in CI/CD environments
    if os.getenv('CI') or os.getenv('GITHUB_ACTIONS'):
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver
    
    # Teardown: close browser after test
    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """
    Fixture that provides an already logged-in driver
    Reusable for tests that require authentication
    """
    driver.get("http://localhost:8080/login.php")
    
    username_input = driver.find_element(By.ID, "inputUsername")
    password_input = driver.find_element(By.ID, "inputPassword")
    
    username_input.send_keys("admin")
    password_input.send_keys("nimda666!")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    # Wait for dashboard to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "employee"))
    )
    
    return driver


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application"""
    return "http://localhost:8080"


def pytest_configure(config):
    """Add custom markers"""
    config.addinivalue_line("markers", "search: tests related to search functionality")
    config.addinivalue_line("markers", "crud: tests related to create, read, update, delete operations")
    config.addinivalue_line("markers", "validation: tests related to form validation")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure
    """
    outcome = yield
    rep = outcome.get_result()
    
    # Only capture screenshot on test failure during call phase
    if rep.when == "call" and rep.failed:
        driver = None
        
        # Try to get the driver from test fixtures
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
        elif "logged_in_driver" in item.funcargs:
            driver = item.funcargs["logged_in_driver"]
        
        if driver:
            # Create screenshots directory if it doesn't exist
            screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            
            # Generate screenshot filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.nodeid.replace("::", "_").replace("/", "_")
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
            
            try:
                driver.save_screenshot(screenshot_path)
                print(f"\n📸 Screenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"\n❌ Failed to capture screenshot: {e}")

