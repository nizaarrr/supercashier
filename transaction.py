# Mengimport tabulate untuk membuat table
from tabulate import tabulate

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
    105 : [105, "Mainan Mobil", 200_000],
    106 : [106, "Mi Instan", 3_000]
} 

"""Modul ini mendefinisikan Transaksi yang dilakukan oleh Masyarakat Umum"""
class Pub_transaction:
    def __init__(self):
        self.order = {}
        
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
                    header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
                    table_style = "fancy_grid"
                    print(tabulate(table, header, tablefmt=table_style))

        # Menampilkan pemberitahuan jika ValueError    
        except ValueError:
            print ("Masukkan Value dalam bentuk Angka (int)")
        # Menampilkan pemberitahuan jika KeyError
        except KeyError:
            print ("Masukkan Kode Produk Sesuai List yang disediakan")
        
    """Modul untuk mengubah jumlah barang dari kode product yang diinput"""
    def Update_items(self):
        try:
            # Menampilkan Daftar Keranjang untuk kepentingan Crosscheck User
            print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
            table = [value for key, value in self.order.items()]
            header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
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
                header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
                table_style = "fancy_grid"
                print(tabulate(table, header, tablefmt=table_style))
            
        except ValueError:
            print ("Masukkan Value dalam bentuk Angka (int)")
        
        except KeyError:
            print ("Masukkan Kode Produk Sesuai List yang disediakan")

    """Modul untuk menghapus jumlah barang dari kode product yang diinput"""
    def Delete_items(self):
        # Menampilkan Daftar Keranjang untuk kepentingan Crosscheck User
        print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
        table = [value for key, value in self.order.items()]
        header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
        table_style = "fancy_grid"
        print(tabulate(table, header, tablefmt=table_style))
        # Menginput kode barang yang akan dihapuskan
        product_code = int(input("Silahkan ketik Kode Produk yang ingin dihapus: "))
        if product_code in self.order.keys():
            print (f'Anda berhasil menghapus barang {self.order[product_code][1]}')
            self.order.pop(product_code)
            print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
            table = [value for key, value in self.order.items()]
            header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
            table_style = "fancy_grid"
            print(tabulate(table, header, tablefmt=table_style))
 
        # Jika kode tidak ada dalam Daftar Keranjang   
        else:
            print ("Kode produk tidak ada dalam Daftar Keranjang")
        
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
    """Modul untuk mengecek Daftar Keranjang"""
    def Check_order(self):
        print ("===Daftar Keranjang===")
        table = [value for key, value in self.order.items()]
        header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
        table_style = "fancy_grid"
        print(tabulate(table, header, tablefmt=table_style))    
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

"""Modul ini mendefinisikan Transaksi yang dilakukan oleh Member Toko"""        
class Mem_transaction:
    def __init__(self, username):
        self.order = {}
        self.username = username
        self.add_discount = 5
    
    """Modul untuk menambahkan jumlah barang dari kode product yang diinput bagi Member"""
    def Add_items(self):

        
        try:
            print("=========Daftar Barang yang Tersedia=========")
            table = [value for key, value in dict_order.items()]
            header = ['Kode Produk', 'Nama Barang', 'Harga Barang']
            table_style = "fancy_grid"
            print(tabulate(table, header, tablefmt=table_style))
            product_code = int(input("Silahkan ketik Kode Produk dari Barang yang ingin ditambahkan: "))
            if product_code in self.order.keys() :
                print('Barang sudah ada di Keranjang, Silahkan pilih menu "Perbaharui Jumlah"')
            else:    
                id_barang = dict_order[product_code][0]
                nama_barang = dict_order[product_code][1]
                harga_barang = dict_order[product_code][2]
                print(f'Barang yang akan anda tambahkan adalah {nama_barang}')
                qty = int(input("\nSilahkan masukkan jumlah barang yang diinginkan: "))
                total_harga = qty * harga_barang

                if qty < 1:
                    print ("Minimal pembelian 1(satu) barang")

                else:
                    print (f'Anda telah menambahkan {nama_barang} sejumlah {qty} pcs dengan total harga Rp. {total_harga} ke Keranjang')
                    self.order[id_barang] = [id_barang, nama_barang, qty, harga_barang, total_harga]
                    print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
                    table = [value for key, value in self.order.items()]
                    header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
                    table_style = "fancy_grid"
                    print(tabulate(table, header, tablefmt=table_style))
            
        except ValueError:
            print ("Masukkan Value dalam bentuk Angka (int)")
        
        except KeyError:
            print ("Masukkan Kode Produk Sesuai List yang disediakan")
        
    """Modul untuk mengubah jumlah barang dari kode product yang diinput bagi Member""" 
    def Update_items(self):
        try:
            print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
            table = [value for key, value in self.order.items()]
            header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
            table_style = "fancy_grid"
            print(tabulate(table, header, tablefmt=table_style))
            product_code = int(input("Silahkan ketik Kode Produk dari Jumlah Barang yang ingin diubah: "))
            id_barang = self.order[product_code][0]
            nama_barang = self.order[product_code][1]
            harga_barang = self.order[product_code][3]
            print(f'Barang yang akan anda Ubah adalah {nama_barang}')
            qty = int(input("Silahkan masukkan jumlah barang yang baru: "))
            total_harga = qty * harga_barang

            if qty < 1:
                print ("Minimal pembelian 1(satu) barang")

            else:
                print (f'Anda telah mengubah {nama_barang} menjadi sejumlah {qty} pcs dengan total harga Rp. {total_harga} ke Keranjang')
                self.order[id_barang] = [id_barang, nama_barang, qty, harga_barang, total_harga]
                print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
                table = [value for key, value in self.order.items()]
                header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
                table_style = "fancy_grid"
                print(tabulate(table, header, tablefmt=table_style))
            
        except ValueError:
            print ("Masukkan Value dalam bentuk Angka (int)")
        
        except KeyError:
            print ("Masukkan Kode Produk Sesuai List yang disediakan")

    """Modul untuk menghapus jumlah barang dari kode product yang diinput bagi Member"""
    def Delete_items(self):
        print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
        table = [value for key, value in self.order.items()]
        header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
        table_style = "fancy_grid"
        print(tabulate(table, header, tablefmt=table_style))

        product_code = int(input("Silahkan ketik Kode Produk yang ingin dihapus: "))
        
        if product_code in self.order.keys():
            print (f'Anda berhasil menghapus barang {self.order[product_code][1]}')
            self.order.pop(product_code)
            print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
            table = [value for key, value in self.order.items()]
            header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
            table_style = "fancy_grid"
            print(tabulate(table, header, tablefmt=table_style))
            
        else:
            print ("Kode produk tidak ada dalam Daftar Keranjang")
        
    """Modul untuk menghapus seluruh barang yang ada di Daftar Keranjang bagi Member"""
    def Reset_items(self):
        sure = input("Apakah anda yakin akan menghapus seluruh Barang di Daftar Keranjang? (y/n): ")
        if sure == 'y':
            print ('Daftar Keranjang telah Kosong')
            self.order.clear()
        elif sure == 'n':
            print ('Kembali ke Menu Awal')
        else:
            print ('Isikan huruf (y) atau (n)')
    """Modul untuk mengecek Total jumlah belanjaan bagi Member"""
    def Check_order(self):
        print ("===Daftar Keranjang===")
        table = [value for key, value in self.order.items()]
        header = ['Kode Produk', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
        table_style = "fancy_grid"
        print(tabulate(table, header, tablefmt=table_style))     
    
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