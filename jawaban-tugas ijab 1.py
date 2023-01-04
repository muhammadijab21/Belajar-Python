angka = 21
angka2 = 40

def genap (): 
    for i in range(0, angka):
        if i % 2 == 0:
            print(i, end=" ")

def ganjil (): 
    for i in range(21, angka2):
        if i % 2 != 0:
            print(i, end=" ")
genap()
print()
ganjil()

            