import random 

print("Bem vindo ao jogo da forca!")
palavras = ["banana", "uva", "manga", "melancia"]
fruta = random.choice(palavras)

cont = 5

while cont > 0:
    print("\nAdvinhe a palabra abaixo: ")
    print(fruta)

    spac = len(fruta)
    print('_' * spac)
    
    print(f'A palavra possui: {len(fruta)} Letras')
    
    user = str(input('Digite uma letra: '))
    print(f"Você possui {cont} tentativas.")
    if user not in fruta:
        cont = cont - 1
    if cont == 0:
        break

print('Jogo encerrado, você não possui mais tentativas.')
    
    

