from Function import tampil_menu_segitiga, print_pattern, system

system("clear")
tampil_menu_segitiga()
pattern = int(input("\nPilih Jenis Pattern\t: "))
row = int(input("Pilih Banyak Baris\t: "))

system("clear")
print("==========")
print_pattern(pattern, row)
print("==========")
