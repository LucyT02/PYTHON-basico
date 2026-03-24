distancia = float(input("digite a distância da entrega (km): "))
peso = float(input("digite o peso do pacote (kg): "))

if distancia <= 100:
    frete = peso * 1
elif distancia >=101 and distancia <= 300:
    frete = peso * 1.5
else:
    frete = peso * 2

if peso > 10:
    frete = frete + 10

print("Valor do frete: R$", frete)