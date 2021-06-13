"""
@Author : Mie Ayam The Best
"""
jwb = "y"

while jwb=="y":
    print("CEK NILAI ANGKA")
    print("------------------")
    n = input("Masukkan Nilai = ")
    na = int(n)
    if na>80:
        status = "Baik Sekali"
    elif na>=65:
        status = "Baik"
    elif na>=55:
        status = "Cukup"
    elif na>=40:
        status = "Kurang"
    else:
        status="Kurang Sekali"
    print (status)
    jwb = input(">> Mau mengulangi ? y/t = ")
    if jwb=="t":
        break