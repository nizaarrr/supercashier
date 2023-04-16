
# Zura Shop - Super Cashier

Pacmann Python Project


### Requirements / Objectives

Project Super Cashier adalah sebuah sistem kasir yang dirancang untuk membantu pengelolaan transaksi keuangan pada sebuah bisnis. Sistem ini dilengkapi dengan berbagai modul yang dapat digunakan untuk mempermudah proses transaksi.

Terdapat 3 modul yang wajib tersedia dalam Project Super Cashier antara lain:
#### Modul Transaksi
Modul `transaction.py` digunakan untuk mempetakan transaksi yang dilakukan oleh customer.
Modul ini digunakan sebagai dasar barang yang dijual

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

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


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

#### Modul Transaksi_member()
Fungsi ini mendefinisikan Transaksi yang dilakukan oleh Member terdaftar.
inputan dalam bentuk [INT] dalam range yang diperintahkan
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
```
## Hasil Test Case
## Conclusion/Future Work

- List barang bisa dikembangkan dengan memanfaatkan barcode reader untuk memudahkan pengguna;
- List barang yang dijual masih terbatas karena masih menggunakan Dictionary dalam modul transaction.py. Pengembangan dengan database akan memudahkan dan bisa mengembangkan ragam modul turunan lain;
- Hasil penjualan belum dibuat dalam database, dan masih dapat dikembangkan lebih baik lagi untuk kepentingan pengembangan perusahaan;
- Jika memilih *non-member* akan langsung menuju ke modul transaksi. Kedepannya ketika memilih *non-member* akan diberikan opsi untuk mendaftar member;

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Running Tests

To run tests, run the following command

```bash
  npm run test
```


## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```


## FAQ

#### Question 1

Answer 1

#### Question 2

Answer 2

