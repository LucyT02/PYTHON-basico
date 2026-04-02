#Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo ('S', 'R' ou 'C') com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).

#Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual de cada uma em relação ao total de cobaias utilizadas

sapos = 0
ratos = 0
coelhos = 0
n = int(input("Digite a quantidade de experimentos registrados: "))
contador = 0
while contador < n:
    quatia = int(input("Digite a quantidade de cobaias utilizadas: "))
    tipo = input("Digite o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho): ")
    if tipo == 'S':
        sapos += quatia
    elif tipo == 'R':
        ratos += quatia
    elif tipo == 'C':
        coelhos += quatia
    contador += 1

total = sapos + ratos + coelhos

print(f"Total de cobaias utilizadas: {total}")
print(f"Total de sapos: {sapos}")
print(f"Total de ratos: {ratos}")
print(f"Total de coelhos: {coelhos}")

print("Sapos %:", (sapos * 100) / total)
print("Ratos %:", (ratos * 100) / total)
print("Coelhos %:", (coelhos * 100) / total)