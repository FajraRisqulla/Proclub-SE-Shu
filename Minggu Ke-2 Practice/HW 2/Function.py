from os import system


def pertandinganDanHasil(clubA, clubB):
    hasil = []
    i = 0
    system("clear")
    while True:
        pertandingan = [None] * (i + 1) * 2
        print(f"Pertandingan {i+1} : ", end="")
        pertandingan[i], pertandingan[i + 1] = input().split()
        pertandingan[i] = int(pertandingan[i])
        pertandingan[i + 1] = int(pertandingan[i + 1])
        if pertandingan[i] < 0 or pertandingan[i + 1] < 0:
            break
        elif pertandingan[i] > pertandingan[i + 1]:
            hasil.append(clubA)
        elif pertandingan[i] < pertandingan[i + 1]:
            hasil.append(clubB)
        elif pertandingan[i] == pertandingan[i + 1]:
            hasil.append("Draw")
        i = i + 1

    system("clear")
    for i in range(0, len(hasil)):
        print(f"Hasil {i+1} : {hasil[i]}")
    print("Pertandingan Selesai")
