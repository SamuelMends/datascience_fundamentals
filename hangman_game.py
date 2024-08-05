import random 

print("Bem vindo ao jogo da forca!")
print("\nAdvinhe a palabra abaixo: ")
palavras = ["banana", "uva", "manga", "melancia"]
fruta = random.choice(palavras)



letras_descobertas = ['_' for letra in palavras]

chance = 5

letras_erradas = []

while chance > 0:

    print(" ".join(letras_descobertas))
    print("\nChances restantes", cont)
    print("Letras erradas:", " ".join(letras_erradas))
    
    tentativa = str(input('Digite uma letra: ')).lower()
    print(f"Você possui {cont} tentativas.")
    if tentativa not in fruta:
        cont = cont - 1
    if cont == 0:
        break
    

print('Jogo encerrado, você não possui mais tentativas.')
    
    

