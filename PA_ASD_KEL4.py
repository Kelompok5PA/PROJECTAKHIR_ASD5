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