import  mysql.connector 
from prettytable import PrettyTable
import pwinput
import math
import time
mydb = mysql.connector.connect(
    host= "sql12.freesqldatabase.com",
    user="sql12609741",
    password="X6QKXcWMWz",
    database="sql12609741"
)
class Node:
    def __init__(self):
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.laptop = ["Asus","Acer","Lenovo","Xiaomi"]
        self.harga = [8000000,10000000,6000000,4000000]
        self.stok = [10,5,15,20]
        self.sortedharga = []
        self.sortedstok= []
        self.saldoakun = 0
        self.databeli = {
            "namabarang" : [],
            "hargabarang" : [],
            "jumlahbarang" : [],
            "totalharga" : []
        }
    def clear_data(self):
        self.head = None
        self.harga.clear()
        self.stok.clear()

    def append1(self,sortedharga,sortedstok):
        self.head = None
        for i in range(len(sortedharga)):
            self.harga.append(self.sortedharga[i])
        for i in range(len(sortedstok)):
            self.stok.append(self.sortedstok[i])

    def update(self,index,namabaru,hargabaru,stokbaru):
        self.laptop[index-1] = namabaru
        self.harga[index-1] = hargabaru
        self.stok[index-1] = stokbaru

    def jumpSearch(self, arr , x , n ):
        step = math.sqrt(n)
        prev = 0
        while arr[int(min(step, n)-1)] < x:
                    prev = step
                    step += math.sqrt(n)
                    if prev >= n:
                        return -1
        while arr[int(prev)] < x:        
                    prev += 1
                    if prev == min(step, n):
                        return -1
        if arr[int(prev)] == x:
                return int(prev)
        return -1
    def shell_sort(self,lst,index_lst):
        n = len(lst)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = lst[i]
                temp_index = index_lst[i]
                j = i
                while j >= gap and lst[j - gap] > temp:
                    lst[j] = lst[j - gap]
                    index_lst[j] = index_lst[j - gap]
                    j -= gap
                lst[j] = temp
                index_lst[j] = temp_index
            gap //= 2

    def getindex(self, index):
        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_index == index:
                return current_node

            current_node = current_node.next
            current_index += 1
        return -1
    def print1(self):
        if len(self.laptop) == 0 :
            print("Linked list kosong")
        else:
            table = PrettyTable()
            table.field_names = ["No","Nama Laptop","Harga","Stok"]
            x1 = 1
            for c in range(len(self.laptop)):
                table.add_row([x1,self.laptop[c],self.harga[c],self.stok[c]])
                x1 += 1
            print(table)   
    def printsaldo(self):
        print(f"Saldo Anda : {self.saldoakun}") 

link1 = LinkedList()

def create_account(mydb):
    cursor = mydb.cursor()
    # mengambil input dari user
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    akunsaldo = 20000000
    # query untuk menambahkan akun baru ke database
    insert_query = "INSERT INTO user (username, password, saldo) VALUES (%s, %s, %s)"
    account_data = (username,password,akunsaldo)
    cursor.execute(insert_query, account_data)
    mydb.commit()
    print(f"Akun {username} berhasil dibuat!")
    cursor.close()
def user_login():
    username = input("Masukkan username: ")
    password = pwinput.pwinput(prompt="Masukkan password: ")
    # Query untuk memeriksa keberadaan username dan password di tabel user
    query = "SELECT * FROM user WHERE username = %s AND password = %s"
    values = (username, password) 
    cursor = mydb.cursor()
    cursor.execute(query, values)
    user = cursor.fetchone()
    # Jika ditemukan user dengan username dan password yang sesuai
    if user:
        querysaldo = "SELECT saldo FROM user WHERE username = %s and password = %s"
        valuessaldo = (username,password)
        cursor.execute(querysaldo, valuessaldo)
        result = cursor.fetchone()
        link1.saldoakun += result[0]
        print("Login berhasil. Selamat datang, {}!".format(user[1]))
        while True:
            print('''
            Menu Yang Tersedia
            1.Beli Barang
            2.Lihat Barang
            3.Informasi Saldo
            4.Tambah Saldo
            5.Struk Barang
            6.Keluar Menu
            ''')
            inputuser = input('Masukan menu yang diinginkan: ')
            if inputuser == "1":
                while True:
                    link1.print1()
                    inputbarang = int(input("Masukan Nomor Barang: "))
                    inputjumlah = int(input("Masukan Jumlah Barang: "))
                    if inputjumlah > link1.stok[inputbarang-1] or inputjumlah < 1 :
                        print("Input Salah")
                    else:
                        break
                if link1.saldoakun >= link1.harga[inputbarang-1]*inputjumlah:
                    kurangisaldo = link1.saldoakun - link1.harga[inputbarang-1]*inputjumlah
                    link1.saldoakun = kurangisaldo
                    link1.stok[inputbarang-1] = link1.stok[inputbarang-1] - inputjumlah
                    link1.databeli["namabarang"].append(link1.laptop[inputbarang-1])
                    link1.databeli["hargabarang"].append(link1.harga[inputbarang-1])
                    link1.databeli["jumlahbarang"].append(inputjumlah)
                    link1.databeli["totalharga"].append(link1.harga[inputbarang-1]*inputjumlah)
                    print("transaksi berhasil")
                else:
                    print('Saldo Tidak Cukup')
            elif inputuser == "2":
                link1.print1()
            elif inputuser == "3":
                link1.printsaldo()
            elif inputuser == "4":
                while True:
                    tambah = int(input('Masukan Jumlah Saldo Yang Ingin Ditambah: '))
                    if tambah < 1:
                        print("Input Tidak Bisa Minus")
                    else:
                        break
                    link1.saldoakun += tambah
                    print(f'Saldo telah tertambah menjadi: {link1.saldoakun}')
            elif inputuser == "5":
                tabel1 = PrettyTable()
                tabel1.field_names = ["No","Nama Barang","Harga Barang","Jumlah Barang","Total Harga"]
                no=1
                for i in range(len(link1.databeli.get("namabarang"))):
                    tabel1.add_row([no, link1.databeli.get("namabarang")[i],link1.databeli.get("hargabarang")[i],link1.databeli.get("jumlahbarang")[i],link1.databeli.get("totalharga")[i]])
                    no+=1
                print(tabel1)
                print("Total Semua Pembelian Anda : ",sum(link1.databeli.get("totalharga")))
                with open('invoicelaptop.txt', 'w') as w:
                    w.write(str(tabel1))
                    w.write(str("\n"))
                    w.write(str("Total Semua Pembelian Anda : "))
                    w.write(str(sum(link1.databeli.get("totalharga"))))
            elif inputuser == "6":
                 break
            else:
                print("Username dan/atau Password salah")
                time.sleep(2)
# Fungsi login admin
def admin_login():
    username = input("Masukkan username admin: ")
    password = pwinput.pwinput(prompt="Masukkan password admin: ")

    # Query untuk memeriksa keberadaan username dan password di tabel admin
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    values = (username, password)

    cursor = mydb.cursor()
    cursor.execute(query, values)

    admin = cursor.fetchone()

    # Jika ditemukan admin dengan username dan password yang sesuai
    if admin:
        print("Login berhasil. Selamat datang, {}!".format(admin[1]))
        while True:
            print('''
            Menu Yang Tersedia
            1.Tambah Data
            2.Lihat Data
            3.Sorting Data
            4.Searching Data
            5.Hapus Data
            6.Update Data
            7.Keluar Menu
            ''')
            inputadmin = input('Masukan menu yang diinginkan: ')
            if inputadmin == "1":
                            while True:
                                input1 = input("Masukan Nama Laptop: ")
                                if "\t" not in input1:
                                    break
                                else:                            
                                    print("Masukan input dengan benar")
                                input2 = int(input("Masukan harga: "))
                                input3 = int(input("Masukan Stok: "))
                                link1.laptop.append(input1)
                                link1.harga.append(input2)
                                link1.stok.append(input3)
            elif inputadmin == "2":
                link1.print1()
            elif inputadmin == "3":
                index_lst = list(range(len(link1.laptop)))
                link1.shell_sort(link1.laptop,index_lst)
                for i in index_lst:
                    link1.sortedharga.append(link1.harga[i])
                for i in index_lst:
                    link1.sortedstok.append(link1.stok[i])
                link1.clear_data()   
                link1.append1(link1.sortedharga,link1.sortedstok)
            elif inputadmin == "4":
                            link1.print1()
                            inputsearch = input('Masukan nama: ')
                            qq = link1.jumpSearch(link1.laptop,inputsearch,len(link1.laptop))
                            if qq == -1:
                                print('data tidak ada')
                            else:
                                print(f'{inputsearch} ada di index {qq}')
            elif inputadmin == "5":
                while True:
                    link1.print1()
                    inputhapus = int(input("Masukan No Yang Ingin Dihapus: "))
                    if inputhapus > len(link1.laptop-1) or inputhapus < 0:
                            print("input salah")
                    else:
                            break
                link1.laptop.pop[inputhapus-1]
                link1.harga.pop[inputhapus-1]
                link1.stok.pop[inputhapus-1]
            elif inputadmin == "6":
                while True:
                    link1.print1()
                    inputupdate = int(input("Masukan No Yang Ingin Diupdate: "))
                    if inputupdate > len(link1.laptop)-1 or inputupdate < 0:
                        print("input salah")
                    else:
                        break
                namabaru = input('Masukan nama baru: ')
                hargabaru = int(input("Masukan harga baru: "))
                stokbaru = int(input('Masukan stok baru: '))
                link1.update(inputupdate,namabaru,hargabaru,stokbaru)
            elif inputadmin == "7":
                            break
                        else:
                            print("Input Menu Salah")
    else:
        print("Username dan/atau Password salah")
        time.sleep(2)

# Main program
def login():
    while True:
        print("Selamat datang di program login.")
        print("Pilih opsi:")
        print("1. Regis User")
        print("2. Login user")
        print("3. Login admin")
        print("4. Keluar")

        pilihanlogin = input("Masukkan pilihan: ")
        if pilihanlogin == "1":
            create_account(mydb)
        elif pilihanlogin == "2":
            user_login()
        elif pilihanlogin == "3":
            admin_login()
        elif pilihanlogin == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
login()
