print("==============================================")
print(" KANTIN UNIV. TEKNOLOGI INFORMASI ")
print("==============================================")
print("Menu Makanan")
print("a. Nasi Goreng               15.000")
print("b. Lontong Goreng            14.900")
print("c. Bakso Goreng              12.900")
print("d. Rujak Goreng              13.000")
print("e. Rujak Bakso               15.000")
print("f. Rujak Bakso Pecel         17.000")
print("==============================================")
print("Menu Minuman")
print("a. Teh Dingin/Hangat/panas   2.500")
print("b. Kopi Dingin               5.000")
print("c. Kopi Teh Panas            6.500")
print("d. Coca Cola Dingin          3.500")
print("e. Coca Cola Panas           5.000")
print("==============================================")
print(" ")

#1. Menyiapkan Variabel
kode=['a','b','c','d','e','f','g','h','i','j','k']
namaMakanan_Minuman=['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel',
            'Teh Dingin/Hangat/panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
harga=['15000','14900','12900','13000','15000','17000',
        '2500','5000','6500','3500','5000']

#2.Input Barang
pilihan = input(">> Masukkan Kode Makanan atau minuman    = ")
#3. INPUT QTY
qty     = input(">> Masukkan Jumlah Pesanan  = ")
 
    

#4. HITUNG BAYAR
##cek nama barang dan ambil harga satuan
i = 0
while i<len(namaMakanan_Minuman):
        #jika value pada list kode[i] == pilihan
            if kode[i] == pilihan:
            #ambil nama barang
                nm_brg = namaMakanan_Minuman[i]

            #ambil harga satuan
                hrgsat = harga[i]
            
        #jika tidak cocok, lanjut ke i berikutnya
                i+=1
            
            
            tot_byr = int(hrgsat) * int(qty)
        

        #5. TAMPILKAN 
print(">>> NAMA BARANG      : " + nm_brg)
print(">>> HARGA BARANG     : Rp." + str(hrgsat))
print(">>> JUMLAH BARANG    : " + qty)
print(("-------------------------------"))
print(">>> TOTAL BAYAR      : Rp." + str(tot_byr))
uang = input(">>> UANG             : Rp.")
x = int(uang)
kembalian = x - tot_byr
print("Kembalian            : Rp."+ str(kembalian))
