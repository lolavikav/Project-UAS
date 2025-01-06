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
    @staticmethod
    def display_table(data):
        print("+--------------------+------------------+----------------+-------------+")
        print("|    Nama Pelanggan  |     Tanggal      |    Jumlah Baju | Total Harga |")
        print("+--------------------+------------------+----------------+-------------+")
        print(f"| {data['Nama Pelanggan']:18} | {data['Tanggal']:16} | {data['Jumlah Baju']:14} | Rp {data['Total Harga']:8} |")
        print("+--------------------+------------------+----------------+-------------+")

    @staticmethod
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

