import random 

print("Bem vindo ao jogo da forca!")
palavras = ["banana", "uva", "manga", "melancia"]
fruta = random.choice(palavras)

cont = 5
letras_adivinhadas = ['_' for _ in fruta]

while cont > 0:
    print("\nAdvinhe a palavra abaixo: ")
    print(' '.join(letras_adivinhadas))
    
    print(f'A palavra possui: {len(fruta)} letras')
    
    user = input('Digite uma letra: ').lower()
    
    if user in fruta:
        for index, letra in enumerate(fruta):
            if letra == user:
                letras_adivinhadas[index] = user
        print("Você adivinhou uma letra!")
    else:
        cont -= 1
        print(f"Você errou. Tentativas restantes: {cont}")
    
    if '_' not in letras_adivinhadas:
        print("\nParabéns! Você adivinhou a palavra:", fruta)
        break
else:
    print('\nJogo encerrado, você não possui mais tentativas.')
    print(f'A palavra era: {fruta}')
