from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

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
    print("3. Halaman tambah kontak dibuka")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    print("4. Form tambah kontak tampil")
    
    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    phone_field = driver.find_element(By.ID, "phone")
    title_field = driver.find_element(By.ID, "title")
    
    name_field.clear()
    email_field.clear()
    phone_field.clear()
    title_field.clear()
    
    print("5. Semua field dibiarkan kosong")
    
    url_before = driver.current_url
    
    save_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    save_button.click()
    print("6. Klik tombol 'Save'")
    
    time.sleep(2)
    
    url_after = driver.current_url
    
    print(f"\n=== HASIL TEST ===")
    print(f"URL sebelum submit: {url_before}")
    print(f"URL setelah submit: {url_after}")
    
    if url_before == url_after:
        print("\n✓ PASS: Form tidak tersubmit, masih di halaman create.php")
        print("Browser menampilkan validasi HTML5 'Please fill out this field'")
        
        validation_message = driver.execute_script(
            "return arguments[0].validationMessage;", name_field
        )
        
        if validation_message:
            print(f"Message validasi: '{validation_message}'")
        
    else:
        print("\n✗ FAIL: Form tersubmit padahal ada field kosong")
    
    time.sleep(3)
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    
finally:
    driver.quit()
    print("\nBrowser ditutup")
