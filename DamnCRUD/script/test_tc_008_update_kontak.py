"""
Test Case 008: Update Existing Contact
Validates that existing contacts can be successfully updated
"""
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.crud
def test_update_kontak(logged_in_driver):
    """
    Test updating an existing contact
    Expected: Contact data should be updated and changes reflected in table
    """
    driver = logged_in_driver
    
    print("✓ Dashboard tampil")
    time.sleep(2)
    
    # Find the first edit button
    first_edit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn-success[href*='update.php']"))
    )
    
    # Get parent row to extract original data
    parent_row = driver.execute_script("return arguments[0].closest('tr');", first_edit_button)
    cells = parent_row.find_elements(By.TAG_NAME, "td")
    
    original_id = cells[0].text
    original_name = cells[1].text
    original_email = cells[2].text
    
    print(f"✓ Kontak yang akan diupdate:")
    print(f"  - ID: {original_id}")
    print(f"  - Name: {original_name}")
    print(f"  - Email: {original_email}")
    
    # Click edit button
    first_edit_button.click()
    print("✓ Klik tombol 'Edit'")
    
    # Wait for update form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    print("✓ Halaman update terbuka")
    
    # Update data - append timestamp to ensure uniqueness
    timestamp = int(time.time())
    updated_data = {
        "name": f"Updated User {timestamp}",
        "email": f"updated{timestamp}@example.com"
    }
    
    # Modify name and email
    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    
    name_field.clear()
    name_field.send_keys(updated_data["name"])
    
    email_field.clear()
    email_field.send_keys(updated_data["email"])
    
    print(f"✓ Data diubah menjadi:")
    print(f"  - Name: {updated_data['name']}")
    print(f"  - Email: {updated_data['email']}")
    
    # Submit update
    update_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    update_button.click()
    print("✓ Klik tombol 'Update'")
    
    # Wait for redirect to dashboard
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "employee"))
    )
    print("✓ Redirect ke dashboard berhasil")
    
    time.sleep(2)
    
    # Search for updated contact
    search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys(updated_data["name"])
    time.sleep(2)
    
    # Verify updated data in table
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#employee tbody tr")
    data_found = False
    
    for row in table_rows:
        if row.is_displayed() and updated_data["name"] in row.text:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 2:
                updated_name = cells[1].text
                updated_email = cells[2].text
                
                print(f"\n✓ Data setelah update:")
                print(f"  - Name: {updated_name}")
                print(f"  - Email: {updated_email}")
                
                # Assertions
                assert updated_name == updated_data["name"], "Name not updated correctly"
                assert updated_email == updated_data["email"], "Email not updated correctly"
                data_found = True
                break
    
    assert data_found, "Updated data not found in table"
    print("\n✓ PASS: Data berhasil diupdate dan perubahan terlihat di tabel")
