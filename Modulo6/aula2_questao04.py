lista1 = []
lista2 = []
lista3 = []

qtd1 = int(input("digite a quantidade de elementos da lista 1: "))

print("Digite os", qtd1, "elementos da lista 1:")

for i in range(qtd1):
    num = int(input())
    lista1.append(num)

qtd2 = int(input("digite a quantidade de elementos da lista 2: "))

print("Digite os", qtd2, "elementos da lista 2:")

for i in range(qtd2):
    num = int(input())
    lista2.append(num)

menor = qtd1

if qtd2 < qtd1:
    menor = qtd2

for i in range(menor):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

if qtd1 > qtd2:
    for i in range(menor, qtd1):
        lista3.append(lista1[i])

else:
    for i in range(menor, qtd2):
        lista3.append(lista2[i])

print("Lista intercalada:", end=" ")
for num in lista3:
    print(num, end=" ")