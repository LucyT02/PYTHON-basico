n = int(input("digite a quantidade de números: "))
maior = 0

while n > 0:
    x = float(input("digite um número: "))
    
    if x > maior:
        maior = x
    
    n = n - 1

print("O maior número é:", maior)