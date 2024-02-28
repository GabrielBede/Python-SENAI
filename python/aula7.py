import random

print ('♟ - DESCUBRA O NÚMERO!')
jogador1 = input('Olá jogador 1! Qual é o seu user?: ')
jogador2 = input('Olá jogador 2! Qual é o seu user?: ')

n = [3,2,1]
for c in n:
    randomico = random.randint(1,10)
    jog1 = int(input('Digite um número jogador 1: '))
    jog2 = int(input('Digite um número jogador 2: '))
    c = c - 1
    
    if randomico  ==  jog1:
        print (f'Jogador {jogador1} você acertou! O número é: {randomico}.')
    if randomico  ==  jog2:
        print (f'Parabéns {jogador2} você acertou! O número é: {randomico}.')
    if randomico  ==  jog1  ==  jog2:
        print (f'Parabéns {jogador1} e {jogador2} vocês acertaram! O número é: {randomico}.')
        break
    elif randomico != jog1 and randomico != jog1 and randomico > 0:
        print (f'Nenhum dos jogadores acertou o número era: {randomico},  vocês tem {c} chances.')
        if c == 0:
            print (f'Vocês gastaram as possibilidades, total de chances:  {c}. Vocês perderam!')
            break



