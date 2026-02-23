from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.maximize_window()

new_contact = {
    "name": "Test User Selenium",
    "email": "selenium@test.com",
    "phone": "08123456789",
    "title": "QA Tester"
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
    
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Add New Contact"))
    )
    add_button.click()
    print("3. Klik tombol 'Add New Contact'")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    print("4. Form tambah kontak terbuka")
    
    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    phone_field = driver.find_element(By.ID, "phone")
    title_field = driver.find_element(By.ID, "title")
    
    name_field.send_keys(new_contact["name"])
    email_field.send_keys(new_contact["email"])
    phone_field.send_keys(new_contact["phone"])
    title_field.send_keys(new_contact["title"])
    
    print(f"5. Data kontak diisi:")
    print(f"   - Name: {new_contact['name']}")
    print(f"   - Email: {new_contact['email']}")
    print(f"   - Phone: {new_contact['phone']}")
    print(f"   - Title: {new_contact['title']}")
    
    save_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    save_button.click()
    print("6. Klik tombol 'Save'")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "employee"))
    )
    print("7. Redirect ke dashboard berhasil")
    
    time.sleep(2)
    
    search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys(new_contact["name"])
    time.sleep(2)
    
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#employee tbody tr")
    
    print(f"\n=== HASIL TEST ===")
    
    data_found = False
    for row in table_rows:
        if row.is_displayed() and new_contact["name"] in row.text:
            data_found = True
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 1:
                print(f"Data baru ditemukan di tabel:")
                print(f"  - Name: {cells[1].text}")
                print(f"  - Email: {cells[2].text}")
                print(f"  - Phone: {cells[3].text}")
                print(f"  - Title: {cells[4].text}")
            break
    
    if data_found:
        print("\n✓ PASS: Data kontak berhasil tersimpan dan muncul di dashboard")
    else:
        print("\n✗ FAIL: Data kontak tidak ditemukan di tabel")
    
    time.sleep(3)
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    
finally:
    driver.quit()
    print("\nBrowser ditutup")
