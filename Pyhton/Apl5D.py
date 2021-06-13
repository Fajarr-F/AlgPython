"""
@Author : Mie Ayam The Best
"""
jwb = "y"

while jwb=="y":
    print("------------------")
    print("CEK Nilai Mahasiswa")
    print("------------------")
    n = input("Masukkan Nilai = ")
    x= int(n)
    if x>=91 & x<=100:
        status = "A"
    elif x>=81 & x<91:
        status = "B"
    elif x>=71 & x<81:
        status = "C"
    else:
        status="D"
    print (status)
    jwb = input(">> Mau mengulangi ? y/t = ")
    if jwb=="t":
        break