from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
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
    print("3. Dashboard tampil")
    
    time.sleep(2)
    
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, "a.btn-danger[href*='delete.php']")
    
    if not delete_buttons:
        print("\n✗ FAIL: Tidak ada kontak yang bisa dihapus")
    else:
        last_delete_button = delete_buttons[-1]
        parent_row = driver.execute_script("return arguments[0].closest('tr');", last_delete_button)
        cells = parent_row.find_elements(By.TAG_NAME, "td")
        
        contact_id = cells[0].text
        contact_name = cells[1].text
        contact_email = cells[2].text
        
        print(f"4. Kontak yang akan dihapus:")
        print(f"   - ID: {contact_id}")
        print(f"   - Name: {contact_name}")
        print(f"   - Email: {contact_email}")
        
        last_delete_button.click()
        print("5. Klik tombol 'Delete'")
        
        time.sleep(1)
        
        try:
            alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"6. Dialog konfirmasi muncul: '{alert_text}'")
            alert.accept()
            print("7. Klik OK pada dialog konfirmasi")
        except:
            print("6. Dialog konfirmasi tidak muncul (langsung redirect)")
        
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "employee"))
        )
        print("8. Tabel berhasil refresh")
        
        search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
        search_box.send_keys(contact_name)
        time.sleep(2)
        
        print(f"\n=== HASIL TEST ===")
        
        table_rows = driver.find_elements(By.CSS_SELECTOR, "#employee tbody tr")
        data_found = False
        
        for row in table_rows:
            if row.is_displayed():
                if "No matching records found" in row.text:
                    print("Data tidak ditemukan di tabel (sudah terhapus)")
                    break
                    
                if contact_name in row.text and contact_id in row.text:
                    data_found = True
                    break
        
        if not data_found:
            print(f"Kontak '{contact_name}' tidak ditemukan lagi di tabel")
            print("\n✓ PASS: Kontak berhasil dihapus dari database")
        else:
            print(f"Kontak '{contact_name}' masih ada di tabel")
            print("\n✗ FAIL: Kontak gagal dihapus")
    
    time.sleep(3)
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\nBrowser ditutup")
