import random

lista1 = []
lista2 = []
interseccao = []

for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

for num in lista1:
    if num in lista2 and num not in interseccao:
        interseccao.append(num)

interseccao.sort()

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("\nInterseção:", interseccao)
print("\nContagem")

for num in interseccao:
    cont1 = lista1.count(num)
    cont2 = lista2.count(num)
    print(num, ": (lista1 =", cont1, ", lista2 =", cont2, ")")