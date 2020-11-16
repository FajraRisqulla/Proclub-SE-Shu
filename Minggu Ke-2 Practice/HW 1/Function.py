def hitungMinMax(arrBerat):
    print("Berat balita minimum\t : %.2f Kg" % min(arrBerat))
    print("Berat balita maksimum\t : %.2f Kg" % max(arrBerat))


def rerata(arrBerat):
    rata = sum(arrBerat) / len(arrBerat)
    print("Rerata berat balita\t : %.2f Kg" % rata)
