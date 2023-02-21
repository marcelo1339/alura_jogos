from random import random, randint, randrange

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print("Bem vindo ao jogo de adivinhação")
print('-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

numero_secreto = randrange(1, 101)
tentativas = 3

for rodada in range(1, tentativas + 1):

    print(f'Tentativa {rodada} de {tentativas}')
    chute = int(input('Digite um número entre 1 e 100: '))
    print('Você digitou', chute)

    if chute < 1 or chute > 100:
        print('Você deve digitar um número entre 1 e 100')
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou!')
        break
    else:
        if maior:
            print('Errou! Seu chute foi maior que o número secreto.')
        elif menor:
            print('Errou! Seu chute foi menor que o número secreto.')


print('Fim do jogo!')
