import random


def jogar():

    print('********************************')
    print('bem vindo no jogo de advinhação')
    print('********************************')

    num_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nivel de dificuldade?')
    print('1- Facil 2- Médio 3- Dificil')
    nivel = input('Define o nivel: ')

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas+1):
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
            print('você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if (chute_maior):
                print('você errou! o chute foi maior do que o numero secreto.')
            elif(chute_menor):
                print('você errou! o seu chute foi menor que o numero secreto')
            pontos_perdidos = abs(num_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('fim do jogo')

    
if(__name__ == '__main__'):
    jogar()
