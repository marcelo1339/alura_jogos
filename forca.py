from random import randrange


def bem_vindo():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print("   Bem vindo ao jogo da forca")
    print('-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


def selecionar_palavra():
    arquivo = open('palavras.txt', 'r', encoding='utf-8')
    palavras = list()

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    posicao_aleatoria = randrange(0, len(palavras))
    palavra_qualquer = palavras[posicao_aleatoria].upper()

    return palavra_qualquer


def palavra_incompleta(palavra):

    return ['_' for letra in palavra]


def tentativa_usuario():
    tentativa = str(input('Tente uma letra? ')).strip().upper()[0]
    return tentativa


def substituir_por_letra(tentativa, palavra, letras_acertadas):
    index = 0
    for letra in palavra:
        if tentativa == letra:
            letras_acertadas[index] = tentativa
        index += 1


def mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar_forca():

    bem_vindo()

    palavra_secreta = selecionar_palavra()

    letras_acertadas = palavra_incompleta(palavra_secreta)
    print(letras_acertadas)

    perdeu = ganhou = False
    tentativas = erros = 0

    while not perdeu and not ganhou:
        print(f'Tentativa {tentativas + 1} de 7')

        chute = tentativa_usuario()

        if chute in palavra_secreta:
            substituir_por_letra(chute, palavra_secreta, letras_acertadas)
        elif chute not in palavra_secreta:
            tentativas += 1
            desenha_forca(tentativas)

        print(letras_acertadas)

        perdeu = tentativas == 7
        ganhou = '_' not in letras_acertadas

        if ganhou:
            mensagem_vitoria()
        
        if perdeu:
            mensagem_derrota(palavra_secreta)

    print('Fim do jogo!')


if __name__ == '__main__':
    jogar_forca()
