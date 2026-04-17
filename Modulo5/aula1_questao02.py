import random
import math

x= 0


n = (int(input("me diga quantas vezes voce quer calcular a raiz quadrada de numeros aleatorios: ")))
print ("gerando valores...")

while x<n: 
    num= random.randint (1,100)
    raiz = math.sqrt (num)
    print ("numero aleatorio:",num)
    print ("raiz:",raiz)
    x+=1

