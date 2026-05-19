import random

num_elementos = random.randint(5, 20)
elementos = []

for i in range(num_elementos):
    numero = random.randint(1, 10)
    elementos.append(numero)

print("Lista:", elementos)
soma = sum(elementos)
print("Soma:", soma)

media = soma / len(elementos)
print("Média:", media)