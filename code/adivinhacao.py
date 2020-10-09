import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3
    pontos = 1000
    rodada = 1

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5




    while (rodada <= total_de_tentativas):
        print("Tentativa", rodada, "de", total_de_tentativas)
        #print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        #função input retorna string
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        acabou_tentativas = rodada == total_de_tentativas

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
            elif(acabou_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        rodada = rodada + 1
    print(F"Fim do jogo, numero secreto é {numero_secreto}")

if (__name__ == "__main__"):
    jogar()