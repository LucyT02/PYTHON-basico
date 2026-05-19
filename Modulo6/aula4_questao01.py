pares = [num for num in range(20, 51) if num % 2 == 0]
quadrados = [num ** 2 for num in [1,2,3,4,5,6,7,8,9]]
divisiveis = [num for num in range(1, 101) if num % 7 == 0]

lista = ["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]

print("Pares:", pares)
print("Quadrados:", quadrados)
print("Divisíveis por 7:", divisiveis)
print("Par ou ímpar:", lista)