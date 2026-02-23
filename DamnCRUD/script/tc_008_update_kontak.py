from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

updated_data = {
    "name": "John Updated",
    "email": "john.updated@example.com"
}

try:
    driver.get("http://localhost:8080/login.php")
    print("1. Halaman login dibuka")
    
    username_input = driver.find_element(By.ID, "inputUsername")
    password_input = driver.find_element(By.ID, "inputPassword")
    
    username_input.send_keys("admin")
    password_input.send_keys("nimda666!")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("2. Login berhasil")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "employee"))
    )
    print("3. Dashboard tampil")
    
    time.sleep(2)
    
    first_edit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn-success[href*='update.php?id=1']"))
    )
    
    parent_row = driver.execute_script("return arguments[0].closest('tr');", first_edit_button)
    cells = parent_row.find_elements(By.TAG_NAME, "td")
    original_id = cells[0].text
    original_name = cells[1].text
    original_email = cells[2].text
    
    print(f"4. Kontak yang akan diupdate:")
    print(f"   - ID: {original_id}")
    print(f"   - Name: {original_name}")
    print(f"   - Email: {original_email}")
    
    first_edit_button.click()
    print("5. Klik tombol 'Edit'")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    print("6. Halaman update terbuka")
    
    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    
    name_field.clear()
    name_field.send_keys(updated_data["name"])
    
    email_field.clear()
    email_field.send_keys(updated_data["email"])
    
    print(f"7. Data diubah menjadi:")
    print(f"   - Name: {updated_data['name']}")
    print(f"   - Email: {updated_data['email']}")
    
    update_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    update_button.click()
    print("8. Klik tombol 'Update'")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "employee"))
    )
    print("9. Redirect ke dashboard berhasil")
    
    time.sleep(2)
    
    search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys(updated_data["name"])
    time.sleep(2)
    
    print(f"\n=== HASIL TEST ===")
    
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#employee tbody tr")
    data_found = False
    
    for row in table_rows:
        if row.is_displayed() and updated_data["name"] in row.text:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 2:
                updated_name = cells[1].text
                updated_email = cells[2].text
                
                print(f"Data setelah update:")
                print(f"  - Name: {updated_name}")
                print(f"  - Email: {updated_email}")
                
                if updated_name == updated_data["name"] and updated_email == updated_data["email"]:
                    data_found = True
                    print("\n✓ PASS: Data berhasil diupdate dan perubahan terlihat di tabel")
                else:
                    print("\n✗ FAIL: Data tidak sesuai dengan yang diinput")
            break
    
    if not data_found:
        print("\n✗ FAIL: Data yang diupdate tidak ditemukan")
    
    time.sleep(3)
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    
finally:
    driver.quit()
    print("\nBrowser ditutup")
