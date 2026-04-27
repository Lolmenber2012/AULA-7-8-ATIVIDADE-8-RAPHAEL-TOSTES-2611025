import random 
lista_palavras = [
    'lobo',
    'cachorro',
    'elefante',
    'tigre',
    'galinha',
    'coelho',
    'sardinha',
    'urso',
    'gaivota',
    'humano'
]
palavra_escolhida=random.choice(lista_palavras)
espaços = ''
tamanho_palavra = len(palavra_escolhida)
for i in range(tamanho_palavra):
    espaços = espaços+ '_'
print('Palavra escondida:' + espaços)


vidas = 6
game_over = False
while not game_over:
     print("\nVocê tem ", vidas, "!")
     tentativa = input('adivinhe uma letra:').lower()
     letras_tentadas = []
     palavra = ""
     for letra in palavra_escolhida:
        if letra == palavra_escolhida:
            palavra  = palavra + letra
            letras_tentadas.append(tentativa)
        elif letra in letras_tentadas:
            palavra  = palavra + letra
        else:
            palavra = palavra + "_"
     print('Palavra a ser descoberta:', palavra )
     if tentativa in letras_tentadas:
         print(f'Você já tentou a letra: {tentativa}')
     if '_' not in palavra:
         game_over = True
         print('\nVocê já achou a palavra! PARABÉNS!!!!!')
     if tentativa not in palavra_escolhida:
         vidas-= 1
         print(f'\n {tentativa} não está na palavra. Você perdeu uma vida :o')
     if vidas == 0:
         game_over = True
         print(f'\n A palavra era {palavra_escolhida}! Você morreu :( ')

     

    




     
   