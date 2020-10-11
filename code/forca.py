def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    #lista
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not acertou and not enforcou): 

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

        print("Jogando")

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