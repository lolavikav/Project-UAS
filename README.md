# Biodata 

## Nama : Lola Seftyliani
## Kelas : TI.24.A.4
## NIM : 312410339

![Screenshot 2025-01-06 135647](https://github.com/user-attachments/assets/e3b5a3e9-75ba-4812-bab2-8284ebbbb8cd)

Program ini adalah aplikasi sederhana untuk sistem laundry  berbasis terminal. Program ini dibuat dengan pendekatan modular dan menggunakan prinsip OOP (Object-Oriented Programming). Program ini memungkinkan pengguna menambahkan jumlah baju yang otomatis mengubah harga total sesuai dengan jumlah baju yang di input

```python
class LaundryData:
    def __init__(self):
        self.total_clothes = 0
        self.total_price = 0
        self.customer_name = ""
        self.date = ""

    def set_clothes(self, num_clothes):
        if num_clothes < 0:
            raise ValueError("Jumlah baju tidak boleh negatif.")
        self.total_clothes = num_clothes
        self.total_price = num_clothes * 2000

    def set_customer_info(self, name, date):
        self.customer_name = name
        self.date = date

    def get_data(self):
        return {
            'Nama Pelanggan': self.customer_name,
            'Tanggal': self.date,
            'Jumlah Baju': self.total_clothes,
            'Total Harga': self.total_price
        }


class LaundryView:
    def display_table(data):
        print("+--------------------+------------------+----------------+-------------+")
        print("|    Nama Pelanggan  |     Tanggal      |    Jumlah Baju | Total Harga |")
        print("+--------------------+------------------+----------------+-------------+")
        print(f"| {data['Nama Pelanggan']:18} | {data['Tanggal']:16} | {data['Jumlah Baju']:14} | Rp {data['Total Harga']:8} |")
        print("+--------------------+------------------+----------------+-------------+")

    def get_input():
        name = input("Masukkan nama pelanggan: ")
        date = input
        while True:
            try:
                num_clothes = int(input("Masukkan jumlah baju yang akan dicuci: "))
                return name, date, num_clothes
            except ValueError:
                print("Harap masukkan angka yang valid.")


class LaundryProcess:
    def __init__(self):
        self.data = LaundryData()
        self.view = LaundryView()

    def run(self):
        while True:
            name, date, num_clothes = self.view.get_input()
            try:
                self.data.set_customer_info(name, date)
                self.data.set_clothes(num_clothes)
                result = self.data.get_data()
                self.view.display_table(result)
            except ValueError as e:
                print(e)
            repeat = input("Apakah Anda ingin melanjutkan? (ya/tidak): ").lower()
            if repeat != 'ya':
                print("Terima kasih telah menggunakan layanan kami!")
                break


if __name__ == "__main__":
    LaundryProcess().run()
```

# Class LaundryData `RegistrationData`
- LaundryData adalah Menyimpan data jumlah baju, total harga, nama pelanggan, dan tanggal transaksi: Class ini bertugas untuk menyimpan semua data penting terkait transaksi laundry.
- Menghitung total harga berdasarkan jumlah baju: Class ini juga bertanggung jawab untuk menghitung total harga berdasarkan tarif yang telah ditentukan.

```python
class LaundryData:
    def __init__(self):
        self.total_clothes = 0
        self.total_price = 0
        self.customer_name = ""
        self.date = ""

    def set_clothes(self, num_clothes):
        if num_clothes < 0:
            raise ValueError("Jumlah baju tidak boleh negatif.")
        self.total_clothes = num_clothes
        self.total_price = num_clothes * 2000

    def set_customer_info(self, name, date):
        self.customer_name = name
        self.date = date

    def get_data(self):
        return {
            'Nama Pelanggan': self.customer_name,
            'Tanggal': self.date,
            'Jumlah Baju': self.total_clothes,
            'Total Harga': self.total_price
        }
```
Penjelasan:
- `__init__(self)`: Konstruktor yang menginisialisasi atribut total_clothes (jumlah baju) dan total_price (total harga).
- `set_clothes((self, num_clothes)`: Method untuk mengatur jumlah baju dan menghitung total harga dengan tarif Rp 2.000 per baju.
- Ada validasi untuk memastikan jumlah baju tidak negatif.
- `get_data(self)`: Method untuk mengembalikan data dalam bentuk dictionary.

# Class `View`
- LaundryView adalah Menangani input dari pengguna: Class ini bertugas untuk meminta input dari pengguna seperti nama pelanggan, tanggal, dan jumlah baju.
- Menampilkan data dalam format tabel: Class ini juga menampilkan hasil transaksi dalam bentuk tabel yang rapi.

```python
class LaundryView:
    def display_table(data):
        print("+--------------------+------------------+----------------+-------------+")
        print("|    Nama Pelanggan  |     Tanggal      |    Jumlah Baju | Total Harga |")
        print("+--------------------+------------------+----------------+-------------+")
        print(f"| {data['Nama Pelanggan']:18} | {data['Tanggal']:16} | {data['Jumlah Baju']:14} | Rp {data['Total Harga']:8} |")
        print("+--------------------+------------------+----------------+-------------+")

    def get_input():
        name = input("Masukkan nama pelanggan: ")
        date = input
        while True:
            try:
                num_clothes = int(input("Masukkan jumlah baju yang akan dicuci: "))
                return name, date, num_clothes
            except ValueError:
                print("Harap masukkan angka yang valid.")
```
Penjelasan:
- `display_table(data)`: Method untuk menampilkan data dalam format tabel.
- `get_input()`: Method untuk meminta input dari pengguna.

  - Menggunakan loop `while` untuk memastikan input yang diberikan adalah angka.
  - Jika input tidak valid, akan ditampilkan pesan error dan meminta pengguna mengisi ulang.
 
# Class `Controller/Process Layer`
- LaundryProcess adalah Mengatur alur kerja program: Class ini bertindak sebagai pengontrol utama yang menghubungkan data, tampilan, dan proses.
- Mengelola input, data, dan tampilan: Class ini menangani alur input dari pengguna, mengelola data yang diperoleh, dan menampilkan hasilnya kepada pengguna.

```python
class LaundryProcess:
    def __init__(self):
        self.data = LaundryData()
        self.view = LaundryView()

    def run(self):
        while True:
            name, date, num_clothes = self.view.get_input()
            try:
                self.data.set_customer_info(name, date)
                self.data.set_clothes(num_clothes)
                result = self.data.get_data()
                self.view.display_table(result)
            except ValueError as e:
                print(e)
            repeat = input("Apakah Anda ingin melanjutkan? (ya/tidak): ").lower()
            if repeat != 'ya':
                print("Terima kasih telah menggunakan layanan kami!")
                break
```

Penjelasan: 
- `__init__(self)`: Konstruktor yang membuat instance dari class LaundryData dan LaundryView.
- `run(self)`: Method utama untuk menjalankan program.

  - Meminta input jumlah baju dari pengguna.
  - Mengatur data jumlah baju dan menghitung harga.
  - Menampilkan hasil dalam bentuk tabel.

# Bagian Main Program

```python
if __name__ == "__main__":
    LaundryProcess().run()
```

Penjelasan: 
- Bagian ini memastikan bahwa program hanya akan dijalankan jika file Python ini dijalankan langsung, bukan diimpor sebagai modul.
- `LaundryProcess().run()` memanggil method `run()` untuk memulai program.

# Contoh Input dan Ouput pada Program
Berikut adalah contoh input dan  output setelah pengguna berhasil memasukkan data:

![Screenshot 2025-01-06 100725](https://github.com/user-attachments/assets/0e0a6ef0-4c3e-498d-905f-7b4a32185b9e)







