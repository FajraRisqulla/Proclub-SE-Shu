from os import system
import Function

system("clear")
a, b = input("Masukkan angka 1 + angka 2\t: ").split()
age = Function.add(int(a), int(b))
a, b = input("Masukkan angka 1 - angka 2\t: ").split()
height = Function.substrack(int(a), int(b))
a, b = input("Masukkan angka 1 * angka 2\t: ").split()
weight = Function.multiply(int(a), int(b))
a, b = input("Masukkan angka 1 / angka 2\t: ").split()
iq = Function.divide(float(a), float(b))

print(
    """ 
Age = {}
Height = {}
Weight = {}
Iq = {}
""".format(
        age, height, weight, iq
    )
)

what = Function.add(
    age, Function.substrack(height, Function.multiply(weight, Function.divide(iq, 2)))
)
print("what = {}".format(what))