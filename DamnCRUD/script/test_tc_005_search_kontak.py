"""
Test Case 005: Search Contact Functionality
Validates that the search feature correctly filters contacts
"""
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.search
def test_search_kontak_by_name(logged_in_driver):
    """
    Test searching contacts by name keyword
    Expected: Table should filter and display only matching contacts
    """
    driver = logged_in_driver
    
    # Verify dashboard loaded
    assert driver.find_element(By.ID, "employee").is_displayed(), "Dashboard table not displayed"
    print("✓ Tabel kontak berhasil ditampilkan")
    
    # Locate search box
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
    )
    print("✓ Search box ditemukan")
    
    # Perform search
    search_keyword = "Joe"
    search_box.clear()
    search_box.send_keys(search_keyword)
    print(f"✓ Keyword '{search_keyword}' diinput")
    
    time.sleep(2)  # Wait for DataTable to filter
    
    # Get filtered results
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#employee tbody tr")
    visible_rows = [row for row in table_rows if row.is_displayed() and "No matching records found" not in row.text]
    
    print(f"\nJumlah data yang ditampilkan: {len(visible_rows)}")
    
    # Assertions
    assert len(visible_rows) > 0, "No data found matching the search keyword"
    
    # Verify all visible rows contain the keyword
    found_names = []
    for row in visible_rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) > 1:
            name = cells[1].text
            found_names.append(name)
            assert search_keyword.lower() in row.text.lower(), f"Row does not contain keyword '{search_keyword}': {name}"
    
    print(f"Data yang ditemukan: {', '.join(found_names)}")
    print(f"\n✓ PASS: Data tabel terfilter sesuai keyword '{search_keyword}'")


@pytest.mark.search
def test_search_no_results(logged_in_driver):
    """
    Test searching with a keyword that returns no results
    Expected: Table should display "No matching records found"
    """
    driver = logged_in_driver
    
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
    )
    
    # Search for non-existent contact
    search_keyword = "NonExistentContact12345"
    search_box.clear()
    search_box.send_keys(search_keyword)
    
    time.sleep(2)
    
    # Check for "No matching records found" message
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#employee tbody tr")
    
    # Should have no visible data rows
    visible_data_rows = [row for row in table_rows if row.is_displayed() and "No matching records found" not in row.text]
    
    assert len(visible_data_rows) == 0, "Unexpected data found for non-existent search keyword"
    print(f"✓ PASS: No matching records found for '{search_keyword}'")
