import random

print("vamos tentar adivinhar um numero e 1 a 10!")
n = int(input("me fale um numero: "))

num = random.randint(1,10)

while n != num:
    if n < num:
        print("muito baixo")
    else:
        print("muito alto")
    
    n = int(input("tente novamente: "))

print("parabens!! acertou")
print("o numero era:", num)




