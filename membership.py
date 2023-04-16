import re
import json

# Baca database dari file
with open('database_member.json') as f:
    database = json.load(f)

class Member:
    def __init__(self):
        pass

    def Add_member(self):
        try:
            username = input("Masukkan username: ").lower()
            if username in database["username"]:
                print("Username sudah terdaftar, Masukkan username lain")
                return
            else:
                if re.match("^[a-zA-Z0-9]*$", username):
                    print("Username valid")
                else:
                    print("Username tidak valid, isian hanya menggunakan huruf dan angka")
                    return

            name = input("Masukkan Nama Lengkap Anda: ")
            telp = str(input("Masukkan Nomor Telp Anda: "))

            if re.match("^[0-9]{9,14}$", telp):
                print("Nomor Telpon valid")

                print(f'\n\nSelamat datang {name}\nAnda telah terdaftar sebagai Member Zura Shop \nUsername anda : {username}\n*Harap mencatat dan mengingat username anda untuk promo menarik dari kami*')
                # Menambahkan data baru ke dalam database
                database["username"].append(username)
                database["nama"].append(name)
                database["nomor_telp"].append(telp)

                with open('database_member.json', 'w') as f:
                    json.dump(database, f)
            else:
                print("Nomor Telpon tidak valid")

        except ValueError:
            print("Isian Nomor Telpon Menggunakan Angka")