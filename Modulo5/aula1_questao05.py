import emoji

print("digite uma frase e ela sera emojizada")

print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

frase = input("digite a frase: ")
reacao = input("digite o emoji (ex: :red_heart:): ")

resultado = emoji.emojize(frase + " " + reacao)

print(resultado)