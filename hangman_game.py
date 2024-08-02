import random 


print("Bem vindo ao jogo da forca!")
print("Advinhe a palabra abaixo: ")


palavras = ["banana", "uva", "manga", "melancia"]
fruta = random.choice(palavras)
palavra = print(fruta)

spac = len(fruta)
print('_'* spac)
print(f'A palavra possui: {len(fruta)} letras')

