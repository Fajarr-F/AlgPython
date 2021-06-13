"""
@Author : Mie Ayam The Best
"""
jwb = "y"

while jwb=="y":
    print("CEK GOLONGAN USIA")
    print("------------------")
    n = input("Masukkan Umur = ")
    u = int(n)
    if u>60:
        status = "Lansia"
    elif u>=35:
        status = "Dewasa"
    elif u>=18:
        status = "Pemuda"
    elif u>=15:
        status = "Remaja"
    else:
        status="Anak"
    print (status)
    jwb = input(">> Mau mengulangi ? y/t = ")
    if jwb=="t":
        break