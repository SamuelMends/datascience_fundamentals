import random 

print("Bem vindo ao jogo da forca!")
print("\nAdvinhe a palabra abaixo: ")

def game():

    # Listas de palavras:
    palavras = ["banana", "uva", "manga", "melancia"]

    # Escolha aleatória das palavras:
    fruta = random.choice(palavras)

    # List Comprehension:
    letras_descobertas = ['_' for letra in palavras]

    # Número de chances:
    chance = 6

    # Armazena letras erradas:
    letras_erradas = []

    # Loop enquanto número de chances for maior do que o zero:
    while chance > 0:
    
        # Print:
        print(" ".join(letras_descobertas))
        print("\nChances restantes", chance)
        print("Letras erradas:", " ".join(letras_erradas))
    
        # Tentativa:
        tentativa = input("\nDigite uma letra: ").lower()
    
        # Condicional:
        if tentativa in fruta:
            index = 0
        
            for letra in fruta:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chance -= 1
            letras_erradas.append(tentativa)
    
        # Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", fruta)
            break
    
game()

    
    

