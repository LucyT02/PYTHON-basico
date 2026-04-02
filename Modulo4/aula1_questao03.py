n1 = int(input("digite o primeiro numero inteiro: "))
n2 = int(input("digite o segundo numero inteiro: "))
n3 = int(input("digite o terceiro numero inteiro: "))

m = (n1 + n2 + n3) / 3
print("A media dos numeros digitados é:", m)

if m >= 60:
    print("Aprovado")
else:
    if m >= 40:
        print("Recuperação")
    else:
        print("Reprovado")
        print ("fim")