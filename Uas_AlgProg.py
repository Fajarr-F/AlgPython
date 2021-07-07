import datetime
from time import process_time_ns

x = datetime.datetime.now()
jwb = "y"

while jwb=="y" or jwb=="Y":
    print("========================================================")
    print("                     input Slip Gaji                  ")
    print("             Tanggal : ",x.strftime("%x"))
    print("========================================================")


    golongan = ['1','2','3']
    gajipokok = ['2500000','4500000','6500000']
    tunjangan = ['1','3','5']

    nama = input("Nama                    =       ")
    g= input("Golongan                =       ")
    gol = int(g)

    if gol == 1 :
        idx = 0
    elif gol == 2:
        idx = 1
    elif gol == 3:
        idx = 2
    else :
        print("Masukkan kembali golongan dengan benar")

    print("1. Laki - Laki")
    print("2. Perempuan")
    jenis_kelamin = input("Jenis kelamin           =      ")
    print ("1. Kawin")
    print ("2. belum")
    status_kawin = input("status Kawin            =      ")
    print("1.  Punya anak")
    print("2. Tidak Punya anak") 
    status_anak = input("Apakah punya anak       =      ")

    #istri
    if jenis_kelamin == "1" :
        jeniskelaminA = "Laki Laki"

        if status_kawin == "1" :
            statuskawinA = "Kawin"
            tunjanganistri = int(gajipokok[idx]) * int(tunjangan[idx]) / 100

            if status_anak == "1" :    
                tunjangananak = int(gajipokok[idx]) * 0.02
            elif status_anak == "2":
                tunjangananak = 0
            else :
                tunjangananak = 0
            
        elif status_kawin == "2" :
            statuskawinB = "Belum Kawin"
            tunjanganistri = 0
        else :
            tunjanganistri = 0

    elif jenis_kelamin== "2":
        jeniskelaminA = "Perempuan"
        if status_kawin == "1" :
            statuskawinA = "Kawin"
            tunjanganistri = 0

            if status_anak == "1" :    
                tunjangananak = int(gajipokok[idx]) * 0.02
            elif status_anak == "2":
                tunjangananak = 0
            else :
                tunjangananak = 0
            
        elif status_kawin == "2" :
            statuskawinA = "Belum Kawin"
            tunjanganistri = 0
        else :
            tunjanganistri = 0
    else :
        print("TIdak Balid")



    #Bruto
    gajibruto = int(gajipokok[idx]) + tunjanganistri + tunjangananak

    #Jabatan
    biayajabatan = int(gajibruto) * 0.05

    #Pensiun
    iuran_pensiun = 15500

    #Organsasi
    iuran_organisasi = 3500

    #Net
    GajiNetto = int(gajibruto) - int(iuran_organisasi) - int(iuran_pensiun)
    


        

        


    print("========================================================")
    print("                         Slip Gaji                  ")
    print("                 Tanggal : ",x.strftime("%x"))
    print("========================================================")
    print("Nama                     " + nama)
    print("Golongan                 " + str(gol))
    print("jenis kelamin            " + jeniskelaminA)
    print("Staus Kawin              " + statuskawinA)
    print("Gaji Pokok               " + gajipokok[idx])
    print("Tunjangan istri          " + str(tunjanganistri))
    print("Tunjangan Anak           " + str(tunjangananak))
    print(">>Gaji bruto             " + str(gajibruto))
    print("========================================================")
    print("Biaya Jabatan            " + str(biayajabatan))
    print("Iuran Pensiun            " + str(iuran_pensiun))
    print("Iuran Organisasi         " + str(iuran_organisasi))
    print(">>Gaji Netto             " + str(GajiNetto))
    jwb = input(">> Mau mengulangi ? y/t = ")
    if jwb=="t" or jwb=="T":
        break
