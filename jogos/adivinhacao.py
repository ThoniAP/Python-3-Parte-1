import random

def jogar():

    print("*******************************************")
    print("Bem vindo ao jogo de adivinhação")
    print("*******************************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontuacao = 1000
    rodada = 1

    print("Defina o nivel do jogo")
    print("(1) Facíl (2) Médio (3) Difícil")

    nivel = input("Digite o nivel desejado:")

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print(numero_secreto)

        print("Rodada {} de {}".format(rodada, tentativas))
        numero_digitado = int(input("Digite um numero:"))

        if (numero_digitado < 1 or numero_digitado > 100):
            print("O numero secreto esta entre 1 e 100")
            continue

        acertou = numero_digitado == numero_secreto
        maior = numero_digitado > numero_secreto
        menor = numero_digitado < numero_secreto

        if (acertou):
            print("Você acertou!")
            print("Sua pontuação foi {}".format(pontuacao))
            break

        else:
            if (maior):
                print("O numero secreto é menor!")
            elif (menor):
                print("O numero secreto é maior")
        pontuacao = pontuacao - abs(numero_secreto - numero_digitado)

    print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar()