expenses = [{'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
                {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
                {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},]

def add_expense(expenses,tanggal, deksripsi, jumlah):
    copy_expenses = expenses.copy()
    add_new = {'tanggal': tanggal, 'deskripsi': deksripsi, 'jumlah':jumlah}
    copy_expenses.append(add_new)
    return copy_expenses

def add_expense_interactively(expenses):
   date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
   description = input("Masukkan deskripsi pengeluaran: ")
   amount = int(input("Masukkan jumlah pengeluaran: "))
   new_expenses = add_expense(expenses,date, description, amount)
   print("Pengeluaran berhasil ditambahkan.")
   return new_expenses

def display_menu():
   print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
   print("1. Tambah Pengeluaran")
   print("2. Total Pengeluaran Harian")
   print("3. Lihat Pengeluaran berdasarkan Tanggal")
   print("4. Lihat Laporan Pengeluaran Harian")
   print("5. Keluar")

get_user_input =  lambda command: int(input(command))
   
def main():
   global expenses
   while True:
       display_menu()
       choice = get_user_input("Pilih menu (1/2/3/4/5): ")
       if choice == 1:
            add_expense_interactively(expenses)
       elif choice == 2:
           print(add_expense_interactively(expenses))
           print(expenses)
       elif choice == 5:
           break
       else:
           print("unknown error")
           
if __name__ == "__main__":
    main()