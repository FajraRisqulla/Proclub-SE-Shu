from os import system
from Function import hitungMinMax, rerata

arrBerat = []

system("clear")
n = int(input("Masukkan Banyak Data Berat Balita :"))

for i in range(n):
    print(f"Masukkan Berat Balita Ke-{i+1} : ", end="")
    n = float(input())
    arrBerat.append(n)

arrBerat.sort()
hitungMinMax(arrBerat)
rerata(arrBerat)