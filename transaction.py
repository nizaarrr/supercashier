
from tabulate import tabulate


dict_order = {
    101 : [101, "Ayam Goreng", 20_000],
    102 : [102, "Tahu Crispy", 10_000],
    103 : [103, "Tempe" , 5_000],
    104 : [104, "Pasta Gigi", 15_000],
    105 : [105, "Es Krim", 17_000]
} 

id_barang = ()
nama_barang = ()
harga_barang = ()
qty = ()



class Pub_transaction:
    def __init__(self):
        self.order = {}
        
    
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
                    header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
                    table_style = "fancy_grid"
                    print(tabulate(table, header, tablefmt=table_style))
            
        except ValueError:
            print ("Masukkan Value dalam bentuk Angka (int)")
        
        except KeyError:
            print ("Masukkan Kode Produk Sesuai List yang disediakan")
        
     
    def Update_items(self):
        try:
            print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
            table = [value for key, value in self.order.items()]
            header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
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
                header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
                table_style = "fancy_grid"
                print(tabulate(table, header, tablefmt=table_style))
            
        except ValueError:
            print ("Masukkan Value dalam bentuk Angka (int)")
        
        except KeyError:
            print ("Masukkan Kode Produk Sesuai List yang disediakan")

    
    def Delete_items(self):
        print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
        table = [value for key, value in self.order.items()]
        header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
        table_style = "fancy_grid"
        print(tabulate(table, header, tablefmt=table_style))

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
            
        else:
            print ("Kode produk tidak ada dalam Daftar Keranjang")
        
    
    def Reset_items(self):
        sure = input("Apakah anda yakin akan menghapus seluruh Barang di Daftar Keranjang? (y/n): ")
        if sure == 'y':
            print ('Daftar Keranjang telah Kosong')
            self.order.clear()
        elif sure == 'n':
            print ('Kembali ke Menu Awal')
        else:
            print ('Isikan huruf (y) atau (n)')
    
    def Check_order(self):
        print ("===Daftar Keranjang===")
        table = [value for key, value in self.order.items()]
        header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
        table_style = "fancy_grid"
        print(tabulate(table, header, tablefmt=table_style))    
    
    def Total_order(self):
        discount = 0
        jumlah_harga = 0
        
        for id_barang, nama_barang, qty, harga_barang, total_price in self.order.values():
            jumlah_harga += total_price
        
        if jumlah_harga > 200_000 and jumlah_harga <= 300_000:
            discount = 5
        elif jumlah_harga > 300_000 and jumlah_harga <= 500_000:
            discount = 8
        elif jumlah_harga > 500_000:
            discount = 10
            
        harga_akhir = (1-discount/100)*jumlah_harga
        if discount == 0:
            print (f'Total harga belanjaan Anda adalah Rp. {harga_akhir}')
        else:
            print (f'Selamat, anda mendapatkan Diskon sebesar {discount}% \nTotal harga belanjaan Anda adalah Rp. {harga_akhir}')
        
class Mem_transaction:
    def __init__(self, username):
        self.order = {}
        self.username = username
        self.add_discount = 5
    
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
                    header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
                    table_style = "fancy_grid"
                    print(tabulate(table, header, tablefmt=table_style))
            
        except ValueError:
            print ("Masukkan Value dalam bentuk Angka (int)")
        
        except KeyError:
            print ("Masukkan Kode Produk Sesuai List yang disediakan")
        
     
    def Update_items(self):
        try:
            print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
            table = [value for key, value in self.order.items()]
            header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
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
                header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
                table_style = "fancy_grid"
                print(tabulate(table, header, tablefmt=table_style))
            
        except ValueError:
            print ("Masukkan Value dalam bentuk Angka (int)")
        
        except KeyError:
            print ("Masukkan Kode Produk Sesuai List yang disediakan")

    
    def Delete_items(self):
        print ("""
                    \n===========================================================================
                    \n=============================Daftar Keranjang==============================
                    \n===========================================================================""")
        table = [value for key, value in self.order.items()]
        header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
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
            header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
            table_style = "fancy_grid"
            print(tabulate(table, header, tablefmt=table_style))
            
        else:
            print ("Kode produk tidak ada dalam Daftar Keranjang")
        
    
    def Reset_items(self):
        sure = input("Apakah anda yakin akan menghapus seluruh Barang di Daftar Keranjang? (y/n): ")
        if sure == 'y':
            print ('Daftar Keranjang telah Kosong')
            self.order.clear()
        elif sure == 'n':
            print ('Kembali ke Menu Awal')
        else:
            print ('Isikan huruf (y) atau (n)')
    
    def Check_order(self):
        print ("===Daftar Keranjang===")
        table = [value for key, value in self.order.items()]
        header = ['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
        table_style = "fancy_grid"
        print(tabulate(table, header, tablefmt=table_style))     
    
    def Total_order(self):
        discount = 0
        jumlah_harga = 0
        
        for id_barang, nama_barang, qty, harga_barang, total_price in self.order.values():
            jumlah_harga += total_price
        
        if jumlah_harga > 200_000 and jumlah_harga <= 300_000:
            discount = 5
        elif jumlah_harga > 300_000 and jumlah_harga <= 500_000:
            discount = 8
        elif jumlah_harga > 500_000:
            discount = 10
            
        harga_akhir = (1-self.add_discount/100)*((1-discount/100)*jumlah_harga)
        if discount == 0:
            print (f'Selamat anda mendapatkan Promo Diskon Member sebesar {self.add_discount}% \nTotal harga belanjaan Anda adalah Rp. {harga_akhir}')
        else:
            print (f'Selamat, anda mendapatkan Diskon sebesar {discount}% dan tambahan Promo Diskon Member sebesar {self.add_discount}% \nTotal harga belanjaan Anda adalah Rp. {harga_akhir}')