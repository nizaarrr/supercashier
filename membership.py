# Memasukkan modul re untuk memastikan isian hanya huruf dan angka
import re
# Memasukkan modul json untuk memproses database dengan format .json
import json

# Baca database dari file
with open('database_member.json') as f:
    database = json.load(f)

# Mendefinisikan Class Member
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