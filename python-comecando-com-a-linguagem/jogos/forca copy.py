import forca
import advinhacao

print('************************')
print('   Escolha seu Jogo!   ')
print('************************')

print('(1)Forca (2)Jogo da advinhação')
jogo = int(input('Qual jogo? '))

if (jogo == 1):
    print('Jogando Forca')
    forca.jogar()
elif(jogo == 2):
    print('Jogando advinhação')
    advinhacao.jogar()

print('fim do jogo')