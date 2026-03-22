comprimento = int(input("Digite o comprimento do terreno:"))
largura = int(input("Digite a largura do terreno:"))
area_m2 = comprimento * largura
preco_m2 = float(input("digite o valor do terreno:"))
preco_total = preco_m2 * area_m2
print("o terreno possui", area_m2, "m2 e custa R$", preco_total)