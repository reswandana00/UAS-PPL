"""
Test Case 009: Delete Contact
Validates that contacts can be successfully deleted
"""
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.crud
def test_delete_kontak(logged_in_driver):
    """
    Test deleting a contact
    Expected: Contact should be removed from database and not appear in table
    """
    driver = logged_in_driver
    
    print("✓ Dashboard tampil")
    time.sleep(2)
    
    # Find all delete buttons
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, "a.btn-danger[href*='delete.php']")
    
    assert len(delete_buttons) > 0, "No contacts available to delete"
    
    # Select the last delete button
    last_delete_button = delete_buttons[-1]
    parent_row = driver.execute_script("return arguments[0].closest('tr');", last_delete_button)
    cells = parent_row.find_elements(By.TAG_NAME, "td")
    
    contact_id = cells[0].text
    contact_name = cells[1].text
    contact_email = cells[2].text
    
    print(f"✓ Kontak yang akan dihapus:")
    print(f"  - ID: {contact_id}")
    print(f"  - Name: {contact_name}")
    print(f"  - Email: {contact_email}")
    
    # Click delete button
    last_delete_button.click()
    print("✓ Klik tombol 'Delete'")
    
    time.sleep(1)
    
    # Handle JavaScript confirm dialog
    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        print(f"✓ Dialog konfirmasi muncul: '{alert_text}'")
        alert.accept()
        print("✓ Klik OK pada dialog konfirmasi")
    except:
        print("✓ Dialog konfirmasi tidak muncul (langsung redirect)")
    
    time.sleep(2)
    
    # Wait for table to refresh
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "employee"))
    )
    print("✓ Tabel berhasil refresh")
    
    # Search for the deleted contact
    search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys(contact_name)
    time.sleep(2)
    
    # Verify contact is no longer in table
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#employee tbody tr")
    data_found = False
    
    for row in table_rows:
        if row.is_displayed():
            if "No matching records found" in row.text:
                print("✓ Data tidak ditemukan di tabel (sudah terhapus)")
                break
            
            if contact_name in row.text and contact_id in row.text:
                data_found = True
                break
    
    assert not data_found, f"Contact '{contact_name}' still exists in table after deletion"
    print(f"✓ Kontak '{contact_name}' tidak ditemukan lagi di tabel")
    print("\n✓ PASS: Kontak berhasil dihapus dari database")