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
    totaldiskon = 1500000
    TotalAwal = x * harga
  
    
    if TotalAwal > totaldiskon:
        Total = TotalAwal - TotalAwal * 15 / 100
    else:
        Total = TotalAwal
    print (Total)
    jwb = input(">> Mau mengulangi ? y/t = ")
    if jwb=="t":
        break