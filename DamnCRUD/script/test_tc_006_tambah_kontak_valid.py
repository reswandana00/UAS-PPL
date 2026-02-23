"""
Test Case 006: Add New Contact with Valid Data
Validates that new contacts can be successfully created
"""
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.crud
def test_tambah_kontak_valid(logged_in_driver):
    """
    Test adding a new contact with valid data
    Expected: Contact should be saved and appear in the dashboard table
    """
    driver = logged_in_driver
    
    # Test data - using timestamp to ensure unique data
    timestamp = int(time.time())
    new_contact = {
        "name": f"Test User Pytest {timestamp}",
        "email": f"pytest{timestamp}@test.com",
        "phone": "08123456789",
        "title": "QA Automation Tester"
    }
    
    # Click "Add New Contact" button
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Add New Contact"))
    )
    add_button.click()
    print("✓ Klik tombol 'Add New Contact'")
    
    # Wait for form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    print("✓ Form tambah kontak terbuka")
    
    # Fill in the form
    driver.find_element(By.ID, "name").send_keys(new_contact["name"])
    driver.find_element(By.ID, "email").send_keys(new_contact["email"])
    driver.find_element(By.ID, "phone").send_keys(new_contact["phone"])
    driver.find_element(By.ID, "title").send_keys(new_contact["title"])
    
    print(f"✓ Data kontak diisi:")
    print(f"  - Name: {new_contact['name']}")
    print(f"  - Email: {new_contact['email']}")
    print(f"  - Phone: {new_contact['phone']}")
    print(f"  - Title: {new_contact['title']}")
    
    # Submit form
    save_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    save_button.click()
    print("✓ Klik tombol 'Save'")
    
    # Wait for redirect to dashboard
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "employee"))
    )
    print("✓ Redirect ke dashboard berhasil")
    
    time.sleep(2)
    
    # Search for the newly created contact
    search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys(new_contact["name"])
    time.sleep(2)
    
    # Verify the contact appears in the table
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#employee tbody tr")
    
    data_found = False
    for row in table_rows:
        if row.is_displayed() and new_contact["name"] in row.text:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 1:
                assert cells[1].text == new_contact["name"], "Name mismatch"
                assert cells[2].text == new_contact["email"], "Email mismatch"
                assert cells[3].text == new_contact["phone"], "Phone mismatch"
                assert cells[4].text == new_contact["title"], "Title mismatch"
                data_found = True
                print(f"\n✓ Data baru ditemukan di tabel:")
                print(f"  - Name: {cells[1].text}")
                print(f"  - Email: {cells[2].text}")
                print(f"  - Phone: {cells[3].text}")
                print(f"  - Title: {cells[4].text}")
                break
    
    assert data_found, "Data kontak tidak ditemukan di tabel setelah disimpan"
    print("\n✓ PASS: Data kontak berhasil tersimpan dan muncul di dashboard")
