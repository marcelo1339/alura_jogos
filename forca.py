
def jogar_forca():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print("Bem vindo ao jogo da forca")
    print('-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    perdeu = ganhou = False

    palavra_secreta = 'banana'

    while not perdeu or not ganhou:
        chute = str(input('Qual letra? ')).strip().lower()
        index = 0

        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print(f'A letra "{letra}", está na posição {index}')

            index += 1

    print('Fim do jogo!')


if __name__ == '__main__':
    jogar_forca()
