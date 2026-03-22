nome1= input("digite o nome do produto1:")
preco1= float(input("digite o preço do produto1:"))
quantidade1= int(input("digite a quantidade do produto1:"))
total1= preco1 * quantidade1

nome2= input("digite o nome do produto2:")
preco2= float(input("digite o preço do produto2:"))
quantidade2= int(input("digite a quantidade do produto2:"))
total2= preco2 * quantidade2

nome3= input("digite o nome do produto3:")
preco3= float(input("digite o preço do produto3:"))
quantidade3= int(input("digite a quantidade do produto3:"))
total3= preco3 * quantidade3

total_compra= total1 + total2 + total3
print("O total da compra é R$", total_compra)