
# Zura Shop - Super Cashier

Pacmann Python Project


### Requirements / Objectives

Project Super Cashier adalah sebuah sistem kasir yang dirancang untuk membantu pengelolaan transaksi keuangan pada sebuah bisnis. Sistem ini dilengkapi dengan berbagai modul yang dapat digunakan untuk mempermudah proses transaksi.

Terdapat 3 modul yang wajib tersedia dalam Project Super Cashier antara lain:
#### Modul Transaksi
Modul `transaction.py` digunakan untuk mempetakan transaksi yang dilakukan oleh customer.
Modul ini digunakan sebagai dasar barang yang dijual
Terdapat beberapa menu utama yang diperlukan:
1. Masukkan barang baru;
2. Ubah barang di Keranjang;
3. Hapus salah satu barang di Keranjang;
4. Kosongkan Keranjang;
5. Cek barang dalam Keranjang;
6. Total belanjaan; dan
7. Keluar.

``` python
"""
Daftar barang yang dijual dalam Toko disimpan dalam bentuk Dictionary.
Key merupakan (kode produk) dan memiliki value yang terdiri dari:
-Kode Produk (contoh: 101)
-Nama Produk (contoh: 'Ayam Goreng')
-Harga Produk (contoh: '20_000')
"""
dict_order = {
    101 : [101, "Ayam Goreng", 20_000],
    102 : [102, "Tahu Crispy", 10_000],
    103 : [103, "Tempe" , 5_000],
    104 : [104, "Pasta Gigi", 15_000],
    105 : [105, "Es Krim", 17_000]
} 
```
Modul transaksi ini terdiri atas `class Pub_transaction` (transaksi dari masyarakat umum) dan `class Mem_transaction` (transaksi dari member toko)

#### Modul Membership
Modul saat ini baru `membership.py` digunakan untuk menambahkan member baru yang disimpan dalam database `database_member.json`.

#### Modul Utama
Modul utama ditulis dalam `main.py` yang digunakan untuk menjalankan serangakaian perintah dalam `python`.
    
## Flowchart

![Flowchart Supercashier drawio](https://user-images.githubusercontent.com/130571422/232326147-17dbc02d-361f-4add-a20a-4eef37da13e5.svg)


## Penjelasan Code
### main.py
Dalam modul ini berisikan serangkaian perintah yang akan dijalankan oleh Pembeli.
#### Modul Import
``` python
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
```

#### Modul Transaksi_member() / Transaksi_umum
Fungsi ini mendefinisikan Transaksi yang dilakukan oleh Member terdaftar / Masyarakat Umum.
inputan dalam bentuk [INT] dalam range yang diperintahkan. Fungsi ini akan memudahkan dalam pemanggilan modul apabila diperlukan.
```python
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
```
fungsi looping dijalankan `True` dengan menginput data anga 1-7. jika diluar angka itu akan loop di daftar menu dan jika mengisi format `str` maka modul akan berhenti dengan Error Exception.

#### generate_transaction_id()
Fungsi ini akan mendefinisikan 8 digit ID Transaksi yang dibuat secara Acak.
Digit pertama diambil dari huruf alfabet.
Digit kedua hingga kedelapan diambil dari angka.
```python
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
```

#### looping check_member 
looping ini menjadi modul perintah utama yang dijalankan diikuti modul Transaksi Umum dan Transaksi Member

```python
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
    trans_id = generate_transaction_id()
    print(f'ID Transaksi anda adalah {trans_id}')
    Transaksi_umum()
```

### membership.py
Fokus utama modul saat ini adalah untuk menginput member yang baru terdaftar dalam database
#### Modul Import
```python
# Memasukkan modul re untuk memastikan isian hanya huruf dan angka
import re
# Memasukkan modul json untuk memproses database dengan format .json
import json
```
#### Membaca Database dari file 
```python
with open('database_member.json') as f:
    database = json.load(f)
```
Dalam code ini file database_member akan dipanggil pada variabel `database`

#### Modul Add_member dalam class Member
```python
class Member:
    def __init__(self):
        pass
    """ Subclass yang berfungsi menambahkan member baru dalam database"""
    def Add_member(self):
        try:
            # Memasukan username, lower digunakan untuk mengurangi kesalahan inputan user
            username = input("Masukkan username: ").lower()
            # Perintah jika username sudah ada pada database
            if username in database["username"]:
                # User harus mencari username lain
                print("Username sudah terdaftar, Masukkan username lain")
                return
            else:
                # Jika username tersedia, maka akan mengecek inputan agar hanya terdiri atas huruf dan angka
                if re.match("^[a-zA-Z0-9]*$", username):
                    print("Username valid")
                else:
                    print("Username tidak valid, isian hanya menggunakan huruf dan angka")
                    return
            # Variabel yang mendefinisikan nama
            name = input("Masukkan Nama Lengkap Anda: ")
            # Variabel yang mendefinisikan nomor telpon yang diinput dalam bentuk string agar dapat dicek
            telp = str(input("Masukkan Nomor Telp Anda: "))
            # Mengecek nomor telpon agar inputan hanya terdiri dari angka dalam range 9-14
            if re.match("^[0-9]{9,14}$", telp):
                print("Nomor Telpon valid")

                print(f'\n\nSelamat datang {name}\nAnda telah terdaftar sebagai Member Zura Shop \nUsername anda : {username}\n*Harap mencatat dan mengingat username anda untuk promo menarik dari kami*')
                # Menambahkan data baru ke dalam database
                database["username"].append(username)
                database["nama"].append(name)
                database["nomor_telp"].append(telp)
                # Menyimpan database
                with open('database_member.json', 'w') as f:
                    json.dump(database, f)
            else:
                print("Nomor Telpon tidak valid")

        except ValueError:
            print("Isian Nomor Telpon Menggunakan Angka")
```

### transaction.py
Modul ini menjalankan serangkaian perintah dari transaksi yang diberikan
#### modul import
```python
from tabulate import tabulate
```
Modul ini hanya mengimport tabulate untuk kepentingan pembuatan table yang rapih
#### variabels
Merupakan Daftar barang yang dijual dalam Toko disimpan dalam bentuk Dictionary.
Key merupakan (kode produk) dan memiliki value yang terdiri dari:
-Kode Produk (contoh: 101)
-Nama Produk (contoh: 'Ayam Goreng')
-Harga Produk (contoh: '20_000')
```python
dict_order = {
    101 : [101, "Ayam Goreng", 20_000],
    102 : [102, "Tahu Crispy", 10_000],
    103 : [103, "Tempe" , 5_000],
    104 : [104, "Pasta Gigi", 15_000],
    105 : [105, "Es Krim", 17_000]
}
```
#### Modul Pub_transaction / Mem_transaction
Hal yang membedakan inputan kedua modul ini, terdapat variabel `username` dan `self.add_discount`. Variabel add_discount ditambahkan untuk benefit diskon tambahan yang diterima oleh Member.
```python
class Pub_transaction:
    def __init__(self):
        self.order = {
```
```python
class Mem_transaction:
    def __init__(self, username):
        self.order = {}
        self.username = username
        self.add_discount = 5
    
```
##### Add_items()
```python
"""Modul untuk menambahkan jumlah barang dari kode product yang diinput"""
    def Add_items(self):

        
        try:
            print("=========Daftar Barang yang Tersedia=========")
            # Isian table dari dict_order dalam looping
            table = [value for key, value in dict_order.items()]
            # Header dari table
            header = ['Kode Produk', 'Nama Barang', 'Harga Barang']
            # Jenis tabel yang digunakan
            table_style = "fancy_grid"
            # Menampilkan table data dari Daftar Barang yang dijual di toko
            print(tabulate(table, header, tablefmt=table_style))
            # Menginput kode produk yang tersedia
            product_code = int(input("Silahkan ketik Kode Produk dari Barang yang ingin ditambahkan: "))
            """Menampilkan perintah jika product_code ada dalam tabel atau tidak"""
            # Jika Kode Produk sudah ada dalam Daftar Keranjang
            if product_code in self.order.keys() :
                # Menampilkan barang sudah ada di keranjang
                print('Barang sudah ada di Keranjang, Silahkan pilih menu "Perbaharui Jumlah"')
            else:
                # Jika Kode Produk Tersedia
                # Memasukkan Kode Produk pada id_barang    
                id_barang = dict_order[product_code][0]
                # Memasukkan Nama Barang pada id_barang
                nama_barang = dict_order[product_code][1]
                # Memasukkan Harga Barang pada nama_barang
                harga_barang = dict_order[product_code][2]
                # Menampilkan barang yang akan ditambahkan
                print(f'Barang yang akan anda tambahkan adalah {nama_barang}')
                # Isian User untuk jumlah barang yang diinput dalam [INT]
                qty = int(input("\nSilahkan masukkan jumlah barang yang diinginkan: "))
                # Rumus untuk total harga (jumlah barang) * (harga barang)
                total_harga = qty * harga_barang
                # Jika jumlah inputan jumlah barang kurang dari 1
                if qty < 1:
                    print ("Minimal pembelian 1(satu) barang")

                else:
                    # Menampilkan nama barang, jumlah barang, dan total harga barang
                    print (f'Anda telah menambahkan {nama_barang} sejumlah {qty} pcs dengan total harga Rp. {total_harga} ke Keranjang')
                    # Memasukkan barang yang dinput dalam Dictionary dari self.order
                    self.order[id_barang] = [id_barang, nama_barang, qty, harga_barang, total_harga]
                    # Menampilkan daftar keranjang untuk kepentingan crosscheck user
                    print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
                    table = [value for key, value in self.order.items()]
                    header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
                    table_style = "fancy_grid"
                    print(tabulate(table, header, tablefmt=table_style))

        # Menampilkan pemberitahuan jika ValueError    
        except ValueError:
            print ("Masukkan Value dalam bentuk Angka (int)")
        # Menampilkan pemberitahuan jika KeyError
        except KeyError:
            print ("Masukkan Kode Produk Sesuai List yang disediakan")
```
##### Update_items()
Fungsi banyak yang mirip dengan Add_items
```python
    """Modul untuk mengubah jumlah barang dari kode product yang diinput"""
    def Update_items(self):
        try:
            # Menampilkan Daftar Keranjang untuk kepentingan Crosscheck User
            print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
            table = [value for key, value in self.order.items()]
            header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
            table_style = "fancy_grid"
            print(tabulate(table, header, tablefmt=table_style))
            # Memasukkan kode barang yang akan diubah
            product_code = int(input("Silahkan ketik Kode Produk dari Jumlah Barang yang ingin diubah: "))
            id_barang = self.order[product_code][0]
            nama_barang = self.order[product_code][1]
            harga_barang = self.order[product_code][3]
            print(f'Barang yang akan anda Ubah adalah {nama_barang}')
            qty = int(input("Silahkan masukkan jumlah barang yang baru: "))
            total_harga = qty * harga_barang
            # Jika barang yang diubah bernilai kurang dari 1
            if qty < 1:
                print ("Minimal pembelian 1(satu) barang")

            else:
                # Jika berhasil mengubah jumlah barang
                print (f'Anda telah mengubah {nama_barang} menjadi sejumlah {qty} pcs dengan total harga Rp. {total_harga} ke Keranjang')
                self.order[id_barang] = [id_barang, nama_barang, qty, harga_barang, total_harga]
                print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
                table = [value for key, value in self.order.items()]
                header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
                table_style = "fancy_grid"
                print(tabulate(table, header, tablefmt=table_style))
            
        except ValueError:
            print ("Masukkan Value dalam bentuk Angka (int)")
        
        except KeyError:
            print ("Masukkan Kode Produk Sesuai List yang disediakan")

```

##### Delete_items()
```python
    """Modul untuk menghapus jumlah barang dari kode product yang diinput"""
    def Delete_items(self):
        # Menampilkan Daftar Keranjang untuk kepentingan Crosscheck User
        print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
        table = [value for key, value in self.order.items()]
        header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
        table_style = "fancy_grid"
        print(tabulate(table, header, tablefmt=table_style))
        # Menginput kode barang yang akan dihapuskan
        product_code = int(input("Silahkan ketik Kode Produk yang ingin dihapus: "))
        product_code = 102
        if product_code in self.order.keys():
            print (f'Anda berhasil menghapus barang {self.order[product_code][1]}')
            self.order.pop(product_code)
            print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
            table = [value for key, value in self.order.items()]
            header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
            table_style = "fancy_grid"
            print(tabulate(table, header, tablefmt=table_style))
 
        # Jika kode tidak ada dalam Daftar Keranjang   
        else:
            print ("Kode produk tidak ada dalam Daftar Keranjang")

```
##### Reset_items()
```python
    """Modul untuk menghapus seluruh barang yang ada di Daftar Keranjang"""
    def Reset_items(self):
        # Variabel inputan untuk mengecek apakah user yakin akan menghapus seluruhnya
        sure = input("Apakah anda yakin akan menghapus seluruh Barang di Daftar Keranjang? (y/n): ")
        # Jika yakin
        if sure == 'y':
            print ('Daftar Keranjang telah Kosong')
            # Fungsi yang dijalankan untuk menghapus dictionary self.order
            self.order.clear()
        # Jika tidak
        elif sure == 'n':
            print ('Kembali ke Menu Awal')
        # Jika inputan selain y atau n
        else:
            print ('Isikan huruf (y) atau (n)')
```

##### Check_order()
```python
    """Modul untuk mengecek Daftar Keranjang"""
    def Check_order(self):
        print ("===Daftar Keranjang===")
        table = [value for key, value in self.order.items()]
        header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
        table_style = "fancy_grid"
        print(tabulate(table, header, tablefmt=ta
```

##### Total Order()
Terdapat sedikit perbedaan penerapan pada Total_order `Pub_transaction` dan `Mem_transaction`
###### Untuk Pub_transaction:
```python
"""Modul untuk mengecek Total jumlah belanjaan"""
    def Total_order(self):
        # Set variabel diskon menjadi 0
        discount = 0
        # Set jumlah harga menjadi 0
        jumlah_harga = 0
        # Looping dari Dictionary self.order
        for id_barang, nama_barang, qty, harga_barang, total_price in self.order.values():
            # Menjumlahkan total harga
            jumlah_harga += total_price

        # Kondisi tambahan untuk Diskon yang diberikan        
        if jumlah_harga > 200_000 and jumlah_harga <= 300_000:
            discount = 5
        elif jumlah_harga > 300_000 and jumlah_harga <= 500_000:
            discount = 8
        elif jumlah_harga > 500_000:
            discount = 10

        # Harga akhir dari belanjaan    
        harga_akhir = (1-discount/100)*jumlah_harga
        # Kondisi tambahan jika tidak ada diskon
        if discount == 0:
            print (f'Total harga belanjaan Anda adalah Rp. {harga_akhir}')
        else:
            print (f'Selamat, anda mendapatkan Diskon sebesar {discount}% \nTotal harga belanjaan Anda adalah Rp. {harga_akhir}')
```

###### Untuk Mem_transaction
```python
    """Modul untuk mengecek Total jumlah belanjaan bagi Member"""
    def Total_order(self):
        # Set variabel diskon menjadi 0
        discount = 0
        # Set jumlah harga menjadi 0
        jumlah_harga = 0
        # Looping dari Dictionary self.order
        for id_barang, nama_barang, qty, harga_barang, total_price in self.order.values():
            jumlah_harga += total_price
        # Kondisi tambahan untuk Diskon yang diberikan 
        if jumlah_harga > 200_000 and jumlah_harga <= 300_000:
            discount = 5
        elif jumlah_harga > 300_000 and jumlah_harga <= 500_000:
            discount = 8
        elif jumlah_harga > 500_000:
            discount = 10
        # Harga akhir dari belanjaan. Diskon member merupakan kondisi Diskon setelah barang terkena Diskon belanjaan umum.   
        harga_akhir = (1-self.add_discount/100)*((1-discount/100)*jumlah_harga)
        # Kondisi tambahan jika tidak ada diskon
        if discount == 0:
            print (f'Selamat anda mendapatkan Promo Diskon Member sebesar {self.add_discount}% \nTotal harga belanjaan Anda adalah Rp. {harga_akhir}')
        else:
            print (f'Selamat, anda mendapatkan Diskon sebesar {discount}% dan tambahan Promo Diskon Member sebesar {self.add_discount}% \nTotal harga belanjaan Anda adalah Rp. {harga_akhir}')
```

Perbedaannya ada pada harga akhir. Untuk member akan mendapatkan potongan tambahan.
## Hasil Test Case
Test case menggunakan modul Transaksi_umum
### Test case 1
Menambahkan 2 item
![Screenshot (8)](https://user-images.githubusercontent.com/130571422/232325137-401a0055-1688-49f5-9b4a-59389c80dc09.png)
### Test case 2
Menghapus salah satu item (pasta gigi)
![Screenshot (9)](https://user-images.githubusercontent.com/130571422/232325181-cdb59983-b032-468a-adb1-0a11c3bf8599.png)
### Test case 3
Menghapus seluruh daftar belanja
![Screenshot (9)](https://user-images.githubusercontent.com/130571422/232325181-cdb59983-b032-468a-adb1-0a11c3bf8599.png)
### Test case 4
Menjumlahkan seluruh item yang dibeli setelah diskon
![Screenshot (11)](https://user-images.githubusercontent.com/130571422/232325231-3361882e-4a63-445e-bbf8-24c6a6330fb8.png)


## Conclusion/Future Work

- List barang bisa dikembangkan dengan memanfaatkan barcode reader untuk memudahkan pengguna;
- List barang yang dijual masih terbatas karena masih menggunakan Dictionary dalam modul transaction.py. Pengembangan dengan database akan memudahkan dan bisa mengembangkan ragam modul turunan lain;
- Hasil penjualan belum dibuat dalam database, dan masih dapat dikembangkan lebih baik lagi untuk kepentingan pengembangan perusahaan;
- Jika memilih *non-member* akan langsung menuju ke modul transaksi. Kedepannya ketika memilih *non-member* akan diberikan opsi untuk mendaftar member;
