# Import modul random
import random
# Import modul membership yang dibuat
import membership
# Import json untuk membaca database
import json
# Import tabulate
from tabulate import tabulate
# Import transaction yang dibuat
from transaction import *
# Import seluruh komponen di membership
from membership import *


#Mendefinisikan Transaksi yang dilakukan oleh Member dan Masyarakat Umum
"""
Fungsi ini mendefinisikan Transaksi yang dilakukan oleh Member terdaftar.
inputan dalam bentuk [INT] dalam range yang diperintahkan

"""
def Transaksi_member():
    # Member
    transaksi_123 = Mem_transaction(username)
    try:
        while True:

            # Mendefinisikan menu yang tersedia
            tampilan_menu = [
                ["1", "Masukkan barang baru"],
                ["2", "Ubah barang di Keranjang"],
                ["3", "Hapus salah satu barang di Keranjang"],
                ["4", "Kosongkan Keranjang"],
                ["5", "Cek barang dalam Keranjang"],
                ["6", "Total belanjaan"],
                ["7", "Keluar"]
            ]

            # Headers tabel
            headers = ["No", "Deskripsi"]

            # Menggunakan 'fancy_grid' style
            table_style = "fancy_grid"

            # Print tabel
            print("""
            \n|==================================================================|
            \n|=============================Zura Shop============================|
            \n|==================================================================|
            """)
            print(tabulate(tampilan_menu, headers=headers, tablefmt=table_style))


            menu = int(input("Menu yang dituju: "))

            # Menambahkan barang ke keranjang
            if menu == 1:
                transaksi_123.Add_items()
            # Mengubah Jumlah Barang di Keranjang
            elif menu == 2:
                transaksi_123.Update_items()
            # Menghapus Salah satu barang di keranjang
            elif menu == 3:
                transaksi_123.Delete_items()
            # Mengosongkan Keranjang
            elif menu == 4:
                transaksi_123.Reset_items()
            # Mengecek Keranjang
            elif menu == 5:
                transaksi_123.Check_order()    
            # Total harga yang harus dibayar
            elif menu == 6:
                transaksi_123.Total_order()
            # keluar
            elif menu == 7:
                print (f"""Terima kasih Member {username} telah berbelanja di Zura Shop.
                \nGunakan QRIS atau EDC untuk melakukan pembayaran anda.
                \nID Transaksi Anda adalah {trans_id}
                \nID Transaksi Anda dibutuhkan ketika melakukan pembayaran.""")

                for id_barang, nama_barang, qty, harga_barang, total_price in transaksi_123.order.values():
                    penjualan [trans_id] = [[trans_id], [username], [[id_barang]], [[nama_barang]], [[qty]], [[harga_barang]], [[total_price]]]
                
                return penjualan
    except ValueError:
        print ("Inputan anda di luar Menu yang disediakan. Silahkan ulang kembali")

        
"""
Fungsi ini mendefinisikan Transaksi yang dilakukan oleh Masyarakat umum.
inputan dalam bentuk [INT] dalam range yang diperintahkan

"""
def Transaksi_umum():
    # Masyarakat Umum
    transaksi_123 = Pub_transaction()
    try:
        while True:

            # Mendefinisikan menu yang tersedia
            tampilan_menu = [
                ["1", "Masukkan barang baru"],
                ["2", "Ubah barang di Keranjang"],
                ["3", "Hapus salah satu barang di Keranjang"],
                ["4", "Kosongkan Keranjang"],
                ["5", "Cek barang dalam Keranjang"],
                ["6", "Total belanjaan"],
                ["7", "Keluar"]
            ]

            # Headers tabel
            headers = ["No", "Deskripsi"]
            
            # menggunakan 'fancy_grid' style
            table_style = "fancy_grid"

            # Print tabel
            print("""
            \n|==================================================================|
            \n|=============================Zura Shop============================|
            \n|==================================================================|
            """)
            print(tabulate(tampilan_menu, headers=headers, tablefmt=table_style))


            menu = int(input("Menu yang dituju: "))

            # Menambahkan barang ke keranjang
            if menu == 1:
                transaksi_123.Add_items()
            # Mengubah Jumlah Barang di Keranjang
            elif menu == 2:
                transaksi_123.Update_items()
            # Menghapus Salah satu barang di keranjang
            elif menu == 3:
                transaksi_123.Delete_items()
            # Mengosongkan Keranjang
            elif menu == 4:
                transaksi_123.Reset_items()
            # Mengecek Keranjang
            elif menu == 5:
                transaksi_123.Check_order()    
            # Total harga yang harus dibayar
            elif menu == 6:
                transaksi_123.Total_order()
            # keluar
            elif menu == 7:
                print (f"""Terima kasih telah berbelanja di Zura Shop.
                \nGunakan QRIS atau EDC untuk melakukan pembayaran anda.
                \nID Transaksi Anda adalah {trans_id}
                \nID Transaksi Anda dibutuhkan ketika melakukan pembayaran.""")

                for id_barang, nama_barang, qty, harga_barang, total_price in transaksi_123.order.values():
                    penjualan [trans_id] = [[trans_id], [[id_barang]], [[nama_barang]], [[qty]], [[harga_barang]], [[total_price]]]
                    break
                return penjualan
    except ValueError:
        print ("Inputan anda di luar Menu yang disediakan. Silahkan ulang kembali")


print("""
\n|==================================================================|
\n|==================================================================|
\n|==========================Selamat Datang==========================|
\n|================================di================================|
\n|=============================Zura Shop============================|
\n|==================================================================|
\n|==================================================================|
""")

# Membuka database member yang tersedia
with open('database_member.json') as f:
    database = json.load(f)
# Membuat variable kosong untuk Username    
username = ()
# Membuat Self atas Modul membership Class Member
daftar = membership.Member()
# Membuat parameter untuk mengisi ya atau tidak
y_or_n = ("Silahkan mengisi dengan huruf (y) atau (n)")
# Membuat variable kosong format Dict untuk menyimpan data penjualan pembeli
penjualan = {}

# Mengecek pembeli adalah member atau bukan
check_member = input("Apakah Anda adalah member? (y/n) : ")
"""
Fungsi ini akan mendefinisikan 8 digit ID Transaksi yang dibuat secara Acak.
Digit pertama diambil dari huruf alfabet.
Digit kedua hingga kedelapan diambil dari angka.
"""
def generate_transaction_id():
    # Daftar semua huruf alfabet
    letters = "abcdefghijklmnopqrstuvwxyz"
    # Memilih huruf acak untuk kode pertama
    first_letter = random.choice(letters)
    # Menghasilkan angka acak sepanjang 7 digit
    numbers = random.randint(1000000, 9999999)
    # Menggabungkan huruf dan angka untuk menghasilkan ID transaksi
    transaction_id = first_letter + str(numbers)
    return transaction_id

# Mengecek Member jika jawaban iya

while check_member not in ['y', 'n']:
    print("Silahkan masukkan huruf y atau n")
    check_member = input("Apakah Anda adalah member? (y/n) : ")
trans_id = generate_transaction_id()
if check_member == "y":
    # Mengisi inputan Username untuk member
    username = input("Silahkan input Username anda: ").lower()
    # Mengecek inputan username dibandingkan dengan database yang tersedia
    if username in database["username"]:
        # Mencari index dari username yang telah diinput
        index = database["username"].index(username)
        print (f'Selamat datang {database["nama"][index]}\nSelamat Berbelanja!')
        Transaksi_member()
    # Jika username tidak tersedia dalam database
    else:
        print("Username belum terdaftar")
        # Memberikan pilihan kepada User untuk mendaftarkan diri sebagai member
        pendaftaran= input(f'Apakah anda ingin melakukan pendaftaran Member? (y/n): ')
        while pendaftaran not in ['y', 'n']:
            print ("Silahkan masukkan huruf y atau n")
            pendaftaran= input(f'Apakah anda ingin melakukan pendaftaran Member? (y/n): ')
        # Jika menginput y maka akan menuju ke Class Add_member pada modul membership
        if pendaftaran == 'y':
            daftar.Add_member()
            Transaksi_member()
        # Jika menginput n maka akan menuju ke menu berikutnya
        elif pendaftaran == 'n':
            print(f'\n ID Transaksi anda adalah {trans_id}')
            print ("Anda akan kembali ke menu berikutnya")
            Transaksi_umum()
                               

# Mengecek member jika bukan member dan tidak akan melakukan pendaftaran
elif check_member =="n": 
    tr = generate_transaction_id()
    print(f'ID Transaksi anda adalah {trans_id}')
    Transaksi_umum()