from tabulate import tabulate

class Transaction:
  '''Class untuk menampung method agar transaksi dapat dilakukan'''
  
  # List berisi stok nama buah, jumlah, dah harga
  list_item_availabel = {"Ayam Goreng" : [100, 20_000],
                         "Pasta Gigi" : [100, 15_000],
                         "Durian" : [30, 100_000],
                         "Manggis" : [90, 1_000]
                         }

  def __init__(self, nama_depan, nama_belakang):
    self.nama_depan = nama_depan
    self.nama_belakang = nama_belakang 
    self.list_belanja = {}
    self.__list_id = {}
    self.total_tagihan = 0

  def generate_id(self, jenis_id):
    '''
    Fungsi untuk membuat id pelanggan dan menyimpannya
    
    Parameter:
      nama_depan (str) : nama depan user
      nama_belakang (str) : nama belakang user
    '''

    self.jenis_id = jenis_id
    id_user = self.nama_depan + self.nama_belakang
    self.__list_id[self.jenis_id] = id_user
    return id_user

  def add_item(self, nama_item, jumlah_item, harga_item):
    '''
    Fungsi untuk menambah item 

    Parameter:
      nama_item (str) : nama item yang ingin di-add
      jumlah_item (int) : jumlah item yang ingin di-add
      harga_item (int) : harga item yang ingin di-add
    '''
    self.nama_item = nama_item
    self.jumlah_item = jumlah_item
    self.harga_item = harga_item
    self.list_belanja[self.nama_item] = [self.jumlah_item, self.harga_item]

  def update_nama(self, nama_lama, nama_update):
    '''
    Fungsi untuk mengupdate daftar item yang sudah di-add

    Parameter:
      nama_lama (str) : nama item yang ingin diganti
      nama_update (str) : nama item baru untuk menggantikan item lama
    '''
    self.nama_lama = nama_lama
    self.nama_update = nama_update
    self.list_belanja[self.nama_update] = self.list_belanja.pop(self.nama_lama)

  def update_qty(self, nama_ganti, qty_update):
    '''
    Fungsi untuk mengupdate kuantitas yang sudah di-add

    Parameter:
      nama_ganti (str) : nama item yang ingin diganti kuantitasnya
      qty_update (int) : jumlah untuk menggantikan kuantitas lama
    '''
    self.nama_ganti = nama_ganti
    self.qty_update = qty_update
    self.list_belanja[self.nama_ganti][0] = self.qty_update

  def update_price(self, nama_update_price, harga_update):
    '''
    Fungsi untuk mengupdate harga yang sudah di-add

    Parameter:
      nama_update_price (str) : nama item yang ingin diganti kuantitasnya
      harga_update (int) : harga untuk menggantikan harga lama
    '''
    self.harga_update = harga_update
    self.nama_update_price = nama_update_price
    self.list_belanja[self.nama_update_price][1] = self.harga_update

  def delete_item(self, nama_item):
    '''
    Fungsi untuk menghapus item sudah di-add beserta kuantitas dan harganya

    Parameter:
      nama_item (str) : nama item yang ingin dihapus
    '''
    self.nama_item = nama_item
    self.total_tagihan -= (self.list_belanja[self.nama_item][1] 
                           * self.list_belanja[self.nama_item][0]) # Mengurangi
                                                                   # Total Tagihan
    del self.list_belanja[self.nama_item]
    print(f"{self.nama_item} berhasil dihapus")

  def reset_transaction(self):
    '''Fungsi untuk menghapus semua belanjaan di dalam list_belanja'''
    self.list_belanja.clear()
    self.harga_total = 0
    self.total_tagihan = 0
    Transaction.list_item_availabel = {"Ayam Goreng" : [100, 20_000],
                          "Pasta Gigi" : [100, 15_000],
                          "Durian" : [30, 100_000],
                          "Manggis" : [90, 1_000]
                          }
    print("Daftar belanja sudah di-reset")

  def check_order(self):
    '''Fungsi untuk melakukan cek input data belanjaan'''
    temp = False
    
    # Melakukan cek ketersediaan nama item
    for key in self.list_belanja.keys():
      if key in self.list_item_availabel:

        # Melakukan pengurangan stok di database berdsarkan jumlah orderan
        if self.list_belanja[key][1] == self.list_item_availabel[key][1]:
          temp_list_item_availabel = self.list_item_availabel[key][0] \
                                      - self.list_belanja[key][0]

          # Mengubah kuantitas pembelian menjadi maksimal jika
          # kuantitas pembelian melebihi stok yang ada
          if temp_list_item_availabel >= 0:
            self.list_item_availabel[key][0] = temp_list_item_availabel
          else:
            print(f"stok '{key}' tersedia hanya {self.list_item_availabel[key][0]} buah."
                  f" Sistem memasukkan {self.list_item_availabel[key][0]} sebagai"
                  f" jumlah pesanan '{key}' anda")
            self.list_belanja[key][0] = self.list_item_availabel[key][0]
            self.list_item_availabel[key][0] = 0

        # Melakukan deteksi kesalahan bila harga yang dimasukkan salah
        if self.list_belanja[key][1] != self.list_item_availabel[key][1]:
          print(f"'{key}' harganya salah")
          temp = True

      # Melakukan deteksi kesalahan bila nama item yang dimasukkan salah
      if key not in self.list_item_availabel:
        print(f"item '{key}' tidak tersedia")
        temp = True
    if temp == True:
      print("Terdapat kesalahan input data")
    else:
      print("Pemesanan sudah benar")

    # Membuat tabel dengan mengubah dict menjadi list terlebih dahulu
    header = ["No", "Nama Item", "Jumlah Item", "Harga per Item", "Total Harga"]
    tabel = [[i+1, item, jumlah, harga, jumlah*harga]  \
             for i, (item, (jumlah, harga)) in  \
             enumerate(self.list_belanja.items())]  # Mengubah dict menjadi list
    print(tabulate(tabel, headers=header, tablefmt="github"))
    
    # Menghitng total tagihan berdasarkan index-4 dari tiap
    # list yang ada dalam list 'tabel'
    for harga_total in tabel: self.total_tagihan += harga_total[4]

    return None

  def total_price(self):
    '''Fungsi untuk menampilkan total harga beserta diskon'''
    print(f"Total belanja adalah Rp.{self.total_tagihan}")

    # Melakukan penentuan diskon berdasarkan jumlah tagihan
    if 200_000 <= self.total_tagihan < 300_000:
      self.tagihan_diskon = self.total_tagihan - (self.total_tagihan * 0.05)
      print(f"Selamat, anda mendapat diskon 5%, "
            f"total tagihan anda adalah {self.tagihan_diskon}")
    elif 300_000 <= self.total_tagihan < 500_000:
      self.tagihan_diskon = self.total_tagihan - (self.total_tagihan * 0.08)
      print(f"Selamat, anda mendapat diskon 8%, "
            f"total tagihan anda adalah {self.tagihan_diskon}")
    elif self.total_tagihan >= 500_000:
      self.tagihan_diskon = self.total_tagihan - (self.total_tagihan * 0.1)
      print(f"Selamat, anda mendapat diskon 10%, "
            f"total tagihan anda adalah {self.tagihan_diskon}")

