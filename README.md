# Python Project: Super Cashier

## 1. Latar Belakang
Sebuah supermarket ingin menerapkan jenis pelayanan self-service. Pelayanan jenis ini memungkinkan pelanggan untuk melakukan pembelian
tanpa perlu berada di supermarket tersebut. Hal ini membuka potensi naiknya pendapatan supermarket karena jangkauan supermarket tersebut 
menjadi lebih luas sehingga semakin besar potensi pelanggan untuk melakukan transaksi di supermarket
tersebut.

## 2. Requirements
1) Membuat proses untuk menghasilkan ID transaksi pelanggan
2) Membuat proses untuk menambahkan item dengan melakukan input nama barang, harga barang, dan jumlah barang
3) Membuat proses update yang terdiri atas:
    a) Update nama barang
    b) Update harga barang
    c) Update jumlah barang
4) Membuat proses untuk menghapus barang
5) Membuat proses untuk mereset daftar belanjaan
6) Membuat proses untuk melakukan pengecekan pesanan pelanggan dan menampilkan pesanan dalam bentuk tabel
7) Membuat proses untuk melihat harga total belanjaan dan menentukan diskon
berdasarkan harga total belanjaan. Diskon tersebut terbagi dalam 3 kategori
sebagai berikut :
    a) Total belanja di atas Rp. 200.000 akan mendapatkan diskon 5%
    b) Total belanja di atas Rp. 300.000 akan mendapatkan diskon 8%
    c) Total belanja di atas Rp. 500.000 akan mendapatkan diskon 10%
    

## 3. Flowchart
![Untitled Diagram drawio (15)](https://user-images.githubusercontent.com/117027412/232245487-29b5c6cc-ed35-48c3-a7d7-f2efce4dacdd.png)


## 4. Fungsi dan Atribut
#### 1) init()
#### Merupakan fungsi inisialisai class Transaction
![image_2023-04-16_005649075](https://user-images.githubusercontent.com/117027412/232245579-f17ebef5-4848-4bb3-bf7e-5dc45c09f1f4.png)

#### 2) generate_id()
#### Merupakan fungsi untuk membuat ID dan menyimpan ID tersebut
![image_2023-04-16_010031699](https://user-images.githubusercontent.com/117027412/232245726-cb95e91f-4d24-49f4-b96e-e6181f71e87b.png)

#### 3) add_item()
#### Merupakan fungsi untuk menambahkan item ke dalam daftar belanjaan
![image_2023-04-16_010059806](https://user-images.githubusercontent.com/117027412/232245761-dbedc587-c9bd-4917-9a07-c9c6621c2584.png)

#### 4) update_nama()
#### Merupakan fungsi untuk mengubah nama item yang sudah ditambahkan dalam daftar belanjaan
![image_2023-04-16_010609681](https://user-images.githubusercontent.com/117027412/232246051-a467b73a-892c-4c07-b87c-bdaa27c82331.png)

#### 5) update_qty()
#### Merupakan fungsi untuk mengubah jumlah item yang sudah ditambahkan dalam daftar belanjaan
![image_2023-04-16_010714833](https://user-images.githubusercontent.com/117027412/232246102-c1e878fa-cff6-4880-9330-d1763a4da991.png)

#### 6) update_price()
#### Merupakan fungsi untuk mengubah harga item yang sudah ditambahkan dalam daftar belanjaan
![image_2023-04-16_010809146](https://user-images.githubusercontent.com/117027412/232246139-ba74f0ec-736e-494a-bb56-09abbf2aa438.png)

#### 7) delete_item()
#### Merupakan fungsi untuk menghapus item yang sudah ditambahkan dalam daftar belanjaan
![image_2023-04-16_011008135](https://user-images.githubusercontent.com/117027412/232246232-6ee62f85-abf6-40e1-8cde-34c29d9a9755.png)

#### 8) reset_transaction()
#### Merupakan fungsi untuk menghapus semua item yang sudah ditambahkan dalam daftar belanjaan
![image_2023-04-16_011041398](https://user-images.githubusercontent.com/117027412/232246252-f7390213-06b9-4ed1-85ff-a8e7f970b472.png)

#### 9) check_order()
#### Merupakan fungsi untuk melakukan cek item yang sudah ditambahkan dalam daftar belanjaan dan menampilkannya dalam bentuk tabel
![image_2023-04-16_011359612](https://user-images.githubusercontent.com/117027412/232246541-17aac606-1338-40fa-8024-fa6ceed92b35.png)

#### 10) total_price()
#### Merupakan fungsi untuk menjumlahkan semua harga item yang sudah ditambahkan dalam daftar belanjaan
![image_2023-04-16_011856371](https://user-images.githubusercontent.com/117027412/232246722-7cf4913d-ecbd-432d-910a-7f5e40484e60.png)



## 5. Demonstrasi
#### Test Case 1
![image_2023-04-16_013308125](https://user-images.githubusercontent.com/117027412/232247426-13ab85ed-7bef-43cc-a1e1-8abfe3f16f80.png)

#### Test Case 2
![image_2023-04-16_013409178](https://user-images.githubusercontent.com/117027412/232247457-55a9e530-7c11-46b1-95e8-1fb2d61f2573.png)

#### Test Case 3
![image_2023-04-16_013527047](https://user-images.githubusercontent.com/117027412/232247533-094e47fc-98a3-4aee-9d04-39478c9fa447.png)

#### Test Case 4
![image_2023-04-16_013635868](https://user-images.githubusercontent.com/117027412/232247587-7610cbcf-c0e8-41e8-b9d5-bdf5a7eb7830.png)

## 6. Future Work
1) Menambahkan kupon berisi diskon tertentu pada pelanggan baru
2) Menambahkan kupon berisi diskon pada pelanggan yang sudah memiliki akun lenih dari 3 bulan
3) Menambahkan fitur untuk memnampilkan barang terjual paling banyak dalam sebulan terakhir


