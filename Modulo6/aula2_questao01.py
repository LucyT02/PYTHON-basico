import random

lista = []

for i in range(20):
    numero = random.randint(-100, 100)
    lista.append(numero)

original = lista.copy()  



lista.sort()
print ("lista ordenada:", lista)

print("lista original:",original)

print("maior valor:", max(lista))
print ("menor valor:",min(lista))