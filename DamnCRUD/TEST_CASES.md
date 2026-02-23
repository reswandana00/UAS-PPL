# Test Cases - Functional Testing DamnCRUD

## Test Cases untuk Aplikasi DamnCRUD

| ID TEST CASE | OBJECTIVE | TEST CASE DESCRIPTION | EXPECTED RESULT | ACTUAL RESULT | PASS/FAIL |
|--------------|-----------|----------------------|-----------------|---------------|-----------|
| TC-001 | Cek login dengan username dan password yang benar | 1. Buka halaman login<br>2. Masukkan username: "admin"<br>3. Masukkan password: "nimda666!"<br>4. Klik tombol "OK I'm sign in" | User berhasil login dan diarahkan ke halaman dashboard yang menampilkan daftar kontak | | |
| TC-002 | Cek login dengan username salah | 1. Buka halaman login<br>2. Masukkan username: "userSalah"<br>3. Masukkan password: "nimda666!"<br>4. Klik tombol "OK I'm sign in" | Muncul pesan error "Damn, wrong credentials!!" dan tetap di halaman login | | |
| TC-003 | Cek login dengan password salah | 1. Buka halaman login<br>2. Masukkan username: "admin"<br>3. Masukkan password: "passwordSalah"<br>4. Klik tombol "OK I'm sign in" | Muncul pesan error "Damn, wrong credentials!!" dan tetap di halaman login | | |
| TC-004 | Cek login dengan field kosong | 1. Buka halaman login<br>2. Biarkan username dan password kosong<br>3. Klik tombol "OK I'm sign in" | Browser menampilkan pesan validasi "Please fill out this field" pada field yang kosong | | |
| TC-005 | Cek tampilan dashboard setelah login | 1. Login dengan kredensial yang benar<br>2. Perhatikan halaman dashboard | Halaman dashboard menampilkan:<br>- Sapaan "Howdy, damn admin!"<br>- Menu navigasi<br>- Tabel berisi daftar kontak lengkap | | |
| TC-006 | Cek fitur search/filter pada tabel kontak | 1. Login ke aplikasi<br>2. Di halaman dashboard, ketik kata kunci di search box tabel<br>3. Coba search nama "John" | Tabel menampilkan hasil filter yang sesuai dengan kata kunci pencarian | | |
| TC-007 | Cek pagination pada tabel kontak | 1. Login ke aplikasi<br>2. Di halaman dashboard, lihat opsi "Show entries"<br>3. Klik tombol pagination untuk pindah halaman | Navigasi pagination berfungsi dan data ditampilkan sesuai halaman yang dipilih | | |
| TC-008 | Cek tombol "Add new contact" di menu | 1. Login ke aplikasi<br>2. Klik menu "Add new contact" | Diarahkan ke halaman form tambah kontak baru | | |
| TC-009 | Tambah kontak dengan data lengkap dan valid | 1. Klik "Add new contact"<br>2. Isi Name: "Budi Santoso"<br>3. Isi Email: "budi@email.com"<br>4. Isi Phone: "08123456789"<br>5. Isi Title: "Manager"<br>6. Klik tombol "Save" | Data kontak tersimpan dan muncul di tabel dashboard dengan tanggal created otomatis | | |
| TC-010 | Tambah kontak dengan field kosong | 1. Klik "Add new contact"<br>2. Biarkan semua field kosong<br>3. Klik tombol "Save" | Browser menampilkan validasi "Please fill out this field" dan data tidak tersimpan | | |
| TC-011 | Tambah kontak dengan hanya mengisi sebagian field | 1. Klik "Add new contact"<br>2. Isi hanya Name dan Email<br>3. Kosongkan Phone dan Title<br>4. Klik "Save" | Browser menampilkan validasi pada field yang wajib diisi (required field) | | |
| TC-012 | Cancel saat menambah kontak | 1. Klik "Add new contact"<br>2. Isi beberapa field<br>3. Klik tombol "Cancel" | Kembali ke halaman dashboard tanpa menyimpan data, data tidak bertambah | | |
| TC-013 | Cek tombol Edit pada kontak | 1. Login ke dashboard<br>2. Pilih salah satu kontak<br>3. Klik tombol "edit" berwarna hijau | Diarahkan ke halaman update dengan form terisi data kontak yang dipilih | | |
| TC-014 | Update data kontak dengan data baru | 1. Klik edit pada kontak id tertentu<br>2. Ubah Name menjadi "John Updated"<br>3. Ubah Email menjadi "updated@email.com"<br>4. Klik tombol "Update" | Data kontak berhasil diupdate dan perubahan terlihat di tabel dashboard | | |
| TC-015 | Update kontak dengan mengosongkan field required | 1. Klik edit pada kontak<br>2. Hapus isi field Name (kosongkan)<br>3. Klik "Update" | Validasi muncul menandakan field Name wajib diisi | | |
| TC-016 | Cancel saat update kontak | 1. Klik edit pada kontak<br>2. Ubah beberapa data<br>3. Klik tombol "Cancel" | Kembali ke dashboard dan data tidak berubah (tetap seperti sebelumnya) | | |
| TC-017 | Delete kontak dengan konfirmasi OK | 1. Login ke dashboard<br>2. Pilih kontak yang akan dihapus<br>3. Klik tombol "delete" merah<br>4. Pada dialog konfirmasi "Are you sure?", klik OK | Kontak terhapus dari database dan tidak muncul lagi di tabel dashboard | | |
| TC-018 | Delete kontak dengan konfirmasi Cancel | 1. Login ke dashboard<br>2. Klik tombol "delete" pada kontak<br>3. Pada dialog konfirmasi, klik "Cancel" | Kontak tidak terhapus dan masih tetap ada di tabel dashboard | | |
| TC-019 | Akses halaman profil | 1. Login ke aplikasi<br>2. Klik menu "Profil" | Halaman profil terbuka menampilkan foto profil dan data username | | |
| TC-020 | Upload foto profil dengan format valid (JPG) | 1. Masuk ke halaman Profil<br>2. Klik "Choose File"<br>3. Pilih file gambar berformat .jpg<br>4. Klik tombol "Change" | Foto profil berhasil diupload dan langsung muncul di halaman profil | | |
| TC-021 | Upload foto profil dengan format tidak valid (PNG) | 1. Masuk ke halaman Profil<br>2. Klik "Choose File"<br>3. Pilih file gambar berformat .png<br>4. Klik tombol "Change" | Muncul pesan error "Ekstensi tidak diijinkan. Hanya menerima file JPG/JPEG" dan foto tidak terupload | | |
| TC-022 | Logout dari aplikasi | 1. Login ke aplikasi<br>2. Klik tombol "Sign out" berwarna merah | User berhasil logout dan diarahkan kembali ke halaman login | | |
| TC-023 | Akses halaman dashboard tanpa login | 1. Pastikan belum login (atau sudah logout)<br>2. Ketik URL dashboard langsung di browser: "http://localhost:8080/index.php" | Otomatis dialihkan ke halaman login karena session tidak ada | | |
| TC-024 | Akses halaman create tanpa login | 1. Pastikan belum login<br>2. Akses langsung URL: "http://localhost:8080/create.php" | Otomatis dialihkan ke halaman login (session check berfungsi) | | |
| TC-025 | Cek session tetap aktif saat berpindah halaman | 1. Login ke aplikasi<br>2. Buka halaman Dashboard<br>3. Klik menu Profil<br>4. Klik Dashboard lagi<br>5. Tambah kontak baru | Session tetap aktif, username tetap ditampilkan, dan semua halaman bisa diakses tanpa diminta login ulang | | |

---

**Keterangan:**
- **ID TEST CASE**: Kode unik untuk setiap test case
- **OBJECTIVE**: Tujuan dari test case
- **TEST CASE DESCRIPTION**: Langkah-langkah detail untuk menjalankan test
- **EXPECTED RESULT**: Hasil yang diharapkan dari test
- **ACTUAL RESULT**: Hasil aktual saat test dijalankan (diisi saat testing)
- **PASS/FAIL**: Status keberhasilan test (diisi saat testing)

**Catatan Penggunaan:**
1. Kolom "ACTUAL RESULT" dan "PASS/FAIL" diisi saat melakukan testing
2. Jika hasil aktual sesuai dengan expected result, tulis "PASS", jika tidak tulis "FAIL"
3. Test dilakukan dengan mengakses aplikasi di http://localhost:8080 (sesuai konfigurasi Docker)
