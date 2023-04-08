# PROJECT AKHIR TOKO LAPTOP
## DESKRIPSI PROGRAM
Program ini merupakan sebuah program tentang sebuah toko laptop yang dapat digunakan oleh user untuk melakukan transaksi antara user dengan penjual serta berguna bagi admin atau penjual untuk melakukan beberapa operasi pada data barang yang ada. Program ini juga memiliki registrasi dan login akun untuk masuk ke dalam menu programnya.
## STRUKTUR PROGRAM
Pada program ini struktur awal komponennya adalah menu login yang berguna sebagai poin entri ke dalam salah satu dari komponen menu utama, yaitu menu admin dan menu user. Kemudian, komponen selanjutnya dari program ini adalah penggunaan encapsulation dari konsep OOP (object-oriented programming) untuk menyimpan data-data barang. Komponen pembantu terdiri dari searching yaitu Jump Search dan sorting yaitu Shell Sort. Konsep OOP juga digunakan untuk menyimpan function constructor dan normal function. Selanjutnya, komponen utama yang digunakan adalah menu user untuk proses transaksi antara penjual dan pembeli dan menu admin untuk proses operasi pada data barang.
## FITUR PROGRAM DAN FUNGSIONALITASNYA
### Menu Login
Pada menu login terdapat empat fitur yaitu;
- Fitur registrasi akun bagi user/pembeli yang berfungsi untuk membuat akun yang akan digunakan user untuk login.
- Fitur login bagi user yang berfungsi untuk masuk ke dalam menu user.
- Fitur login bagi admin yang berfungsi untuk masuk ke dalam menu admin. 
- Fitur keluar yang berfungsi untuk keluar dari menu login dan keluar dari program. 
### Menu Admin
Pada menu admin terdapat tujuh fitur yaitu;
- Fitur tambah data yang berfungsi menambah barang baru ke dalam data barang. 
- Fitur lihat data yang berfungsi untuk melihat data barang yang tersedia. 
- Fitur sorting data yang berfungsi untuk mengurutkan data secara ascending. 
- Fitur searching data (catatan data harus sudah ter-sorting dahulu) yang berfungsi untuk mencari indeks dari data. 
- Fitur hapus data yang berfungsi menghapus data barang yang dipilih. 
- Fitur update data yang berfungsi mengupdate data yang dipilih menjadi data baru.
- Fitur keluar yang berfungsi untuk keluar dari menu admin ke menu login.
### Menu User
Pada menu user terdapat enam fitur yaitu;
- Fitur beli barang yang berfungsi untuk membeli barang.
- Fitur lihat barang yang berfungsi untuk melihat barang yang tersedia.
- Fitur informasi saldo yang berfungsi untuk melihat nominal saldo yang dimiliki.
- Fitur tambah saldo yang berfungsi untuk menambah nominal dari saldo yang dimiliki.
- Fitur struk barang yang berfungsi untuk melihat struk dari barang yang sudah dibeli.
- Fitur keluar yang berfungsi untuk keluar dari menu user ke menu login.
## CARA PENGGUNAAN
### Menu Login
#### Registrasi User
1. Pilih "1" pada input menu login.
2. Masukan username yang di inginkan.
3. Masukan password yang di inginkan.
#### Login User
1. Pilih "2" pada input menu login.
2. Masukan username akun anda.
3. Masukan password akun anda.
(Jika username dan/atau password yang dimasukan salah atau tidak ada maka akan kembali ke menu login)
#### Login Admin
1. Pilih "3" pada input menu login.
2. Masukan username admin.
3. Masukan password admin.
(Jika username dan/atau password yang dimasukan salah atau tidak ada maka akan kembali ke menu login)
#### Keluar Menu Login
Masukan "4" pada input menu maka program akan langsung berhenti.

(Jika menu login yang di input user tidak tersedia maka akan diminta input ulang)
### Menu User
#### Beli Barang
1. Pilih "1" pada input menu user.
2. Masukan nomor barang yang ingin dibeli.
3. Masukan jumlah barang.
(Jika jumlah barang yang dimasukan lebih dari stok yang ada atau memasukan nol maka akan diminta input ulang)
(Jika saldo mencukupi maka saldo dari akun user akan terkurangi dan barang yang dibeli akan masuk ke dalam data beli)
(Jika saldo tidak mencukupi maka user akan kembali ke menu user)
#### Lihat Barang
Masukan "2" pada input menu user maka data barang akan langsung ditampilkan.
#### Informasi Saldo
Masukan "3" pada input menu user maka data saldo dari akun user akan ditampilkan.
#### Tambah Saldo
1. Masukan "4" pada input menu user.
2. Masukan nominal saldo yang di inginkan.
(Jika nominal yang dimasukan kurang dari 1 maka akan diminta input ulang)
#### Struk Barang
Masukan "5" pada input menu user maka user akan melihat tampilan barang yang telah terbeli.
#### Keluar
Masukan "6" pada input menu user maka user akan kembali ke menu login.

(Jika input menu yang dimasukan oleh user tidak tersedia maka akan diminta input ulang)
### Menu Admin
#### Tambah Data
1. Masukan "1" pada input menu admin.
2. Masukan nama laptop.
3. Masukan harga.
4. Masukan stok.
#### Lihat Data 
Masukan "2" pada input menu admin maka admin akan melihat tampilan data barang.
#### Sorting Data
Masukan "3" pada input menu admin maka data barang akan disorting menurut nama barangnya.
#### Searching Data
1. Masukan "4" pada input menu admin.
2. Masukan nama barang yang ingin dicari indeks nya.
(Searching dapat dilakukan dengan catatan barang sudah tersorting)
#### Hapus Data
1. Masukan   "5" pada input menu admin.
2. Masukan nomor barang yang ingin dihapus.
(Jika nomor barang yang dihapus kurang dari 1 atau tidak ada maka akan diminta input ulang)
#### Update Data
1. Masukan "6" pada input menu admin.
2. Masukan nomor barang yang ingin dihapus.
3. Masukan nama barang baru.
4. Masukan harga barang baru.
5. Masukan stok barang baru.
#### Keluar 
Masukan "7" pada input menu admin maka admin akan keluar dari menu admin dan masuk ke menu login.

(Jika admin memasukan menu yang tidak tersedia maka akan diminta input ulang)
