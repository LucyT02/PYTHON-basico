idade = int(input("Digite a idade: "))
jogador_intermediario = int(input("ja jogou pelo menos 3 vezes jogos de rpg?: "))
ganhos = int(input("quantas vezes venceu?: "))
pode_jogar = idade >= 16 and idade <= 18 and jogador_intermediario >= 3 and ganhos >= 1
print("O jogador pode jogar?", pode_jogar)