lista = []

qtd = int(input("quantos numeros você quer digitar? "))

while qtd < 4:
    qtd = int(input("digite no minimo 4 numeros: "))

for i in range(qtd):
    numero = int(input("digite um numero: "))
    lista.append(numero)

print()
print("Lista original:", lista)
print("3 primeiros elementos:", lista[:3])
print("2 últimos elementos:", lista[-2:])
print("Lista invertida:", lista[::-1])
print("Elementos de índice par:", lista[::2])
print("Elementos de índice ímpar:", lista[1::2])