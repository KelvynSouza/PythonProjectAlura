import random
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
rodada = 1
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

    if(acertou):
        print("Parabéns! Você acertou!")
        break
    else:
        if(maior):

            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
    rodada = rodada + 1
print(F"Fim do jogo, numero secreto é {numero_secreto}")
