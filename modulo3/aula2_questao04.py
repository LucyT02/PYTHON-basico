classe = input("Digite a classe do personagem (mago, guerreiro ou arqueiro): ")
forca = int(input("Digite a força do personagem (1 a 20): "))
magia = int(input("Digite a magia do personagem (1 a 20): "))

pode_jogar = (
    (classe == "mago" and magia <= 15 and forca <= 10) or
    (classe == "guerreiro" and forca <= 15 and magia <= 10) or
    (classe == "arqueiro" and 5 <= forca <= 15 and 5 <= magia <= 15))

print("Pontos de atributo consistentes com a classe escolhida:", pode_jogar)