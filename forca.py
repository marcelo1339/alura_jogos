
def jogar_forca():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print("Bem vindo ao jogo da forca")
    print('-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    perdeu = ganhou = False

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    while not perdeu or not ganhou:
        chute = str(input('Qual letra? ')).strip().lower()
        index = 0

        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = chute

            index += 1

        print(letras_acertadas)


    print('Fim do jogo!')


if __name__ == '__main__':
    jogar_forca()
