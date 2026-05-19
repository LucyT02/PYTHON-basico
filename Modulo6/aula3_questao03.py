import random

lista = []

for i in range(20):
    lista.append(random.randint(-10, 10))

print("Original:", lista)

inicio = 0
fim = 0

maior_inicio = 0
maior_fim = 0
maior = 0

i = 0

while i < len(lista):

    if lista[i] < 0:
        inicio = i

        while i < len(lista) and lista[i] < 0:
            i += 1

        fim = i

        quantidade = fim - inicio

        if quantidade > maior:
            maior = quantidade
            maior_inicio = inicio
            maior_fim = fim

    else:
        i += 1

del lista[maior_inicio:maior_fim]

print("Editada:", lista)