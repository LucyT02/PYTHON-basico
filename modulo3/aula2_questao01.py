idade_juliana = int(input("Digite a idade de Júlia: "))
idade_Cris= int(input("Digite a idade de Cris: "))

pode_entrar = idade_juliana >= 18 and idade_Cris >= 18
print("Júlia e Cris podem entrar na festa?", pode_entrar)