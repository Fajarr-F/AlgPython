"""
@Author : Mie Ayam The Best
"""
jwb = "y"

while jwb=="y":
    print("CEK KELULUSAN")
    print("------------------")
    n = input("Masukkan Nilai = ")
    if int(n)>60:
        status = "Lulus"
    else:
        status="Ulang"
    print (status)
    jwb = input(">> Mau mengulangi ? y/t = ")
    if jwb=="t":
        break
