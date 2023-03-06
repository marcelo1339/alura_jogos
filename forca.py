
def jogar_forca():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print("   Bem vindo ao jogo da forca")
    print('-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    perdeu = ganhou = False

    palavra_secreta = 'maçã'.upper()
    letras_acertadas = []

    for letra in palavra_secreta:
        letras_acertadas.append('_')

    tentativas = erros = 0

    while not perdeu and not ganhou:
        print(f'Tentativa {tentativas + 1} de 6')

        chute = str(input('Tente uma letra? ')).strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = chute
                index += 1
        elif chute not in palavra_secreta:
            tentativas += 1

        print(letras_acertadas)

        perdeu = tentativas == 6
        ganhou = '_' not in letras_acertadas

        if ganhou:
            print('Você ganhou!!')

    print('Fim do jogo!')


if __name__ == '__main__':
    jogar_forca()
