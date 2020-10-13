def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    #lista
    letras_acertadas = ["_" for letra in palavra_secreta]

    #for letra in palavra_secreta:
    #   letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou): 

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas) 

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()


#Tuplas
# instrutor1 = ("Nico", 39) ->imutavel, como no c#
#é possivel transformar listas em tupla:
#linhas_tuple = tuple(Lista)
#Tambem é possive transformar Tupla em lista:
#linhas_list = list(linhas_tuple)

#SET: Lista que não permite campos duplicados
#Inicializando -> colecao = {11122233344, 22233344455, 33344455566}
#colecao.add(44455566677)
#set não possui um índice
#set não é ordenado.

#Dictionary
#instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
#instrutores['Flavio']