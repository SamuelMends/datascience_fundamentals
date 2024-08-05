import random 

print("Bem vindo ao jogo da forca!")
palavras = ["banana", "uva", "manga", "melancia"]
fruta = random.choice(palavras)

cont = 5

letras_descobertas = ['_' for letra in palavras]



while cont > 0:
    print("\nAdvinhe a palabra abaixo: ")
    letras_erradas = []

    print(" ".join(letras_descobertas))
    print("\nChances restantes", cont)
    print("Letras erradas:", " ".join(letras_erradas))
    
    user = str(input('Digite uma letra: ')).lower()
    print(f"Você possui {cont} tentativas.")
    if user not in fruta:
        cont = cont - 1
    if cont == 0:
        break
    

print('Jogo encerrado, você não possui mais tentativas.')
    
    

