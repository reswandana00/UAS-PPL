"""
Test Case 007: Form Validation - Empty Fields
Validates that the form prevents submission when required fields are empty
"""
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.validation
def test_validasi_field_kosong(logged_in_driver):
    """
    Test form validation when all fields are left empty
    Expected: Form should not submit, validation message should appear
    """
    driver = logged_in_driver
    
    # Click "Add New Contact" button
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Add New Contact"))
    )
    add_button.click()
    print("✓ Halaman tambah kontak dibuka")
    
    # Wait for form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    print("✓ Form tambah kontak tampil")
    
    # Get form fields
    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    phone_field = driver.find_element(By.ID, "phone")
    title_field = driver.find_element(By.ID, "title")
    
    # Clear all fields (ensure they're empty)
    name_field.clear()
    email_field.clear()
    phone_field.clear()
    title_field.clear()
    print("✓ Semua field dibiarkan kosong")
    
    # Capture URL before submission attempt
    url_before = driver.current_url
    
    # Try to submit the form
    save_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    save_button.click()
    print("✓ Klik tombol 'Save'")
    
    time.sleep(2)
    
    # Capture URL after submission attempt
    url_after = driver.current_url
    
    print(f"\nURL sebelum submit: {url_before}")
    print(f"URL setelah submit: {url_after}")
    
    # Assertions
    assert url_before == url_after, "Form submitted despite empty fields"
    print("✓ Form tidak tersubmit, masih di halaman create.php")
    
    # Check for HTML5 validation message
    validation_message = driver.execute_script(
        "return arguments[0].validationMessage;", name_field
    )
    
    assert validation_message != "", "No validation message displayed"
    print(f"✓ Message validasi: '{validation_message}'")
    print("\n✓ PASS: Browser menampilkan validasi HTML5 'Please fill out this field'")