n = int (input("digite a quatidade de representantes: "))

soma = 0
contador = 0

while contador<n:
    idade = int(input("digite a idade: "))
    soma += idade
    contador += 1

media = soma/n

print(media)