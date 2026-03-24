idade_juliana = int(input("Digite a idade de Júlia: "))
idade_Cris= int(input("Digite a idade de Cris: "))

pode_entrar = idade_juliana >= 18 or idade_Cris >= 18 
print("Júlia ou Cris pode entrar na festa?", pode_entrar)