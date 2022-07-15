print('********************************')
print ('bem vindo no jogo de advinhação')
print('********************************')

num_secreto = 42

chute_str = input('Digite o seu numero')
print('Você digitou ', chute_str)

chute = int(chute_str)
acertou = chute == num_secreto
chute_maior = chute > num_secreto
chute_menor = chute < num_secreto


if (acertou):
    print('você acertou')
else:
    if (chute_maior):
        print('você errou! o chute foi maior do que o numero secreto.')   
    elif(chute_menor):
        print('você errou! o seu chute foi menor que o numero secreto')    

print('fim do jogo')