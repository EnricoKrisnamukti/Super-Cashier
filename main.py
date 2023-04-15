from transaction import Transaction
from tabulate import tabulate

list_user = []

nama_user_d = input("Silakan masukkan nama depan anda ")
nama_user_b = input("Silakan masukkan nama belakang anda ")
jenis_user = input("Apakah anda pelanggan baru atau lama: ")
user_id = Transaction(nama_user_d, nama_user_b)
user_jenis = user_id.generate_id(jenis_user)

try:

  add = True
  while add == True:
    nama_item = input("Nama item: ")
    jumlah_item = int(input("Jumlah item: "))
    harga_item = int(input("Harga item: "))
    user_belanja = user_id.add_item(nama_item, jumlah_item, harga_item)
    user_check = user_id.check_order()
    user_price = user_id.total_price()
    add_temp = input("Apakah mau add lagi? Ya/Tidak")
    if add_temp == "Ya": add = True
    else:
      add = False
    # user_belanja = user_id.add_item(nama_item, jumlah_item, harga_item)
    # user_check = user_id.check_order()
    # user_price = user_id.total_price()
except ValueError:
  print("Masukkan jumlah/harga dalam bentuk angka")



temp_branch = True

try:

  while temp_branch == True:
    temp = input("Apakah anda ingin mengubah pesanan? Ya/Tidak")
    if temp == "Ya":
      temp = input("Silahkan pilih add/update/delete/reset")

      # Percabangan untuk melakukan add
      if temp == "add":
        nama_item = input("Nama item: ")
        jumlah_item = int(input("Jumlah item: "))
        harga_item = int(input("Harga item: "))
        user_belanja = user_id.add_item(nama_item, jumlah_item, harga_item)
        user_check = user_id.check_order()
        user_price = user_id.total_price()


      # Percabangan untuk melakukan update
      if temp == "update":
        temp = input("apa yang ingin diupdate? nama/harga/jumlah")
        if temp == "nama":
          temp_item = input("Masukkan nama item yang ingin diganti ")
          temp_item_b = input("Masukkan nama item baru ")
          user_id.update_nama(temp_item, temp_item_b)
        elif temp == "harga":
          temp_item = input("Masukkan nama item yang ingin diganti ")
          temp_item_b = int(input("Masukkan harga item baru "))
          user_id.update_price(temp_item, temp_item_b)
        elif temp == "jumlah":
          temp_item = input("Masukkan nama item yang ingin diganti ")
          temp_item_b = int(input("Masukkan jumlah item baru "))
          user_id.update_qty(temp_item, temp_item_b)
      
      # Percabangan untuk melakukan delete
      if temp == "delete":
        temp_item = input("Masukkan nama item yang ingin dihapus ")
        user_id.delete_item(temp_item)
      
      # Percabangan untuk melakukan reset daftar belanjaan
      if temp == "reset":
        user_id.reset_transaction()

    else:
      temp_branch = False

except Exception as e:
  print(e)

user_check = user_id.check_order()
user_price = user_id.total_price()
print("Silahkan melakukan pembayaran")

