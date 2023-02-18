print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print("Bem vindo ao jogo de adivinhação")
print('-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

numero_secreto = 42
tentativas = 3
rodada = 1

while rodada <= tentativas:
    print(f'Tentativa {rodada} de {tentativas}')
    chute = int(input('Digite o seu número: '))
    print('Você digitou', chute)

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
    rodada += 1

print('Fim do jogo!')
