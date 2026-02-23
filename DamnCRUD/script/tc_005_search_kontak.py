from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
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
    print("3. Tabel kontak berhasil ditampilkan")
    
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
    )
    print("4. Search box ditemukan")
    
    search_box.clear()
    search_box.send_keys("Joe ")
    print("5. Keyword 'Joe ' diinput")
    
    time.sleep(2)
    
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#employee tbody tr")
    visible_rows = [row for row in table_rows if row.is_displayed() and "No matching records found" not in row.text]
    
    print(f"\n=== HASIL TEST ===")
    print(f"Jumlah data yang ditampilkan: {len(visible_rows)}")
    
    if visible_rows:
        print("\nData yang ditemukan:")
        for i, row in enumerate(visible_rows, 1):
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 1:
                name = cells[1].text
                print(f"  {i}. {name}")
                
        all_contain_joe = all("Joe " in row.text.lower() for row in visible_rows)
        
        if all_contain_joe:
            print("\n✓ PASS: Data tabel terfilter sesuai keyword 'Joe '")
        else:
            print("\n✗ FAIL: Ada data yang tidak mengandung keyword 'Joe '")
    else:
        print("\n✗ FAIL: Tidak ada data yang ditemukan")
    
    time.sleep(3)
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    
finally:
    driver.quit()
    print("\nBrowser ditutup")
