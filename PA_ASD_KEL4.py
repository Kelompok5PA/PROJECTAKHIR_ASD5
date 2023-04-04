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