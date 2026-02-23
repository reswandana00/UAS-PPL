# Selenium Automation Test Scripts

Script automation testing untuk aplikasi DamnCRUD menggunakan Selenium WebDriver dengan Firefox.

## Prasyarat

1. **Python 3.7+** sudah terinstall
2. **Mozilla Firefox** browser terinstall
3. **GeckoDriver** - akan otomatis diinstall oleh webdriver-manager
4. **Aplikasi DamnCRUD** berjalan di http://localhost:8080

## Instalasi

Install dependencies Python:

```bash
pip install -r requirements.txt
```

## Daftar Test Scripts

| File                              | Test Case | Deskripsi                              |
| --------------------------------- | --------- | -------------------------------------- |
| `tc_005_search_kontak.py`         | TC-005    | Search kontak dengan keyword "John"    |
| `tc_006_tambah_kontak_valid.py`   | TC-006    | Tambah kontak dengan data valid        |
| `tc_007_validasi_field_kosong.py` | TC-007    | Validasi field kosong saat submit form |
| `tc_008_update_kontak.py`         | TC-008    | Update data kontak yang sudah ada      |
| `tc_009_delete_kontak.py`         | TC-009    | Delete kontak dari database            |

## Cara Menjalankan

### Menjalankan satu test case:

```bash
python tc_005_search_kontak.py
```

### Menjalankan semua test secara berurutan:

```bash
python tc_005_search_kontak.py
python tc_006_tambah_kontak_valid.py
python tc_007_validasi_field_kosong.py
python tc_008_update_kontak.py
python tc_009_delete_kontak.py
```

### Atau dengan PowerShell:

```powershell
Get-ChildItem -Filter tc_*.py | ForEach-Object { python $_.Name }
```

### Dengan runner script:

```bash
python run_all_tests.py
```

## Hasil Output

Setiap script akan menampilkan:

- Langkah-langkah yang dieksekusi
- Status PASS/FAIL
- Detail hasil test

Contoh output:

```
1. Halaman login dibuka
2. Login berhasil
3. Tabel kontak berhasil ditampilkan
4. Search box ditemukan
5. Keyword 'John' diinput

=== HASIL TEST ===
Jumlah data yang ditampilkan: 2

Data yang ditemukan:
  1. John Does
  2. Joe McKinney

✓ PASS: Data tabel terfilter sesuai keyword 'John'

Browser ditutup
```

## Catatan

- Pastikan aplikasi DamnCRUD sudah running di http://localhost:8080
- Browser Firefox akan otomatis dibuka dan ditutup oleh script
- Kredensial login default: `admin` / `nimda666!`
- Script akan menampilkan hasil PASS/FAIL di akhir eksekusi

## Troubleshooting

### GeckoDriver error

Jika muncul error terkait GeckoDriver:

```bash
pip install --upgrade webdriver-manager
```

### Connection refused

Pastikan aplikasi DamnCRUD sudah running:

```bash
docker-compose up -d
```

### Element not found

Tambahkan waktu tunggu lebih lama atau cek selector element.
