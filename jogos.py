from forca import jogar_forca
from adivinhacao import jogar_adivinhacao


def escolhe_jogo():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print("      Qual jogo quer jogar??")
    print('-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    print('[1] Forca [2] Adivinhação ')
    jogo = int(input('Qual jogo quer jogar? '))

    if jogo == 1:
        print('Jogando jogo da Forca...')
        jogar_forca()
    elif jogo == 2:
        print('Jogando jogo da Adivinhação...')
        jogar_adivinhacao()


if __name__ == '__main__':
    escolhe_jogo()
