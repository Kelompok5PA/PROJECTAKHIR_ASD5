import  mysql.connector 
from prettytable import PrettyTable
import pwinput
import math
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