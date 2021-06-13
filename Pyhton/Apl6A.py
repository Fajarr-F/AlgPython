"""
@Author : Mie Ayam The Best
"""
jwb = "y"

while jwb=="y":
    print("------------------")
    print("Menghitung total transaksi pembelian Printer Epson T20")
    print("------------------")
    n = input("Masukkan Banyaknya print = ")
    x= int(n)
    harga = 660000
    TotalAwal = x * harga
    print (TotalAwal)
    
    jwb = input(">> Mau mengulangi ? y/t = ")
    if jwb=="t":
        break