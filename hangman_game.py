import random 

print("Bem vindo ao jogo da forca!")
print("\nAdvinhe a palabra abaixo: ")

#Listas de palavras:
palavras = ["banana", "uva", "manga", "melancia"]

#Escolha aleatória das palavras:
fruta = random.choice(palavras)

#List Comprehension:
letras_descobertas = ['_' for letra in palavras]

#Número de chances:
chance = 5

#Armazena letras erradas:
letras_erradas = []

#Loop enquanto número de chances for maior do que o zero:
while chance > 0:

    print(" ".join(letras_descobertas))
    print("\nChances restantes", chance)
    print("Letras erradas:", " ".join(letras_erradas))
    
    tentativa = str(input('Digite uma letra: ')).lower()
    print(f"Você possui {chance} tentativas.")
    if tentativa not in fruta:
        chance = chance - 1
    if chance == 0:
        break
    

print('Jogo encerrado, você não possui mais tentativas.')
    
    

