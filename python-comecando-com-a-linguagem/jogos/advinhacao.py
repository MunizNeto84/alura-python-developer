import random

print('********************************')
print ('bem vindo no jogo de advinhação')
print('********************************')

num_secreto = random.randrange(1,101)
total_de_tentativas = 3

for rodada in range (1, total_de_tentativas+1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute_str = input('Digite o seu número de 1 a 100: ')
    print('Você digitou ', chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print('Você deve digitar um numero de 1 a 100')
        continue
    

    acertou = chute == num_secreto
    chute_maior = chute > num_secreto
    chute_menor = chute < num_secreto


    if (acertou):
        print('você acertou')
        break
    else:
        if (chute_maior):
            print('você errou! o chute foi maior do que o numero secreto.')   
        elif(chute_menor):
            print('você errou! o seu chute foi menor que o numero secreto')    

print('fim do jogo')