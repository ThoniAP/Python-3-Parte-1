print("*******************************************")
print("Bem vindo ao jogo de adivinhação")
print("*******************************************")

tentativas = 3
rodada = 1

while (rodada <= tentativas):
    numero_secreto = 47
    print("Rodada {} de {}".format(rodada, tentativas))
    numero_digitado = int(input("Digite um numero:"))

    acertou = numero_digitado == numero_secreto

    maior = numero_digitado > numero_secreto

    menor = numero_digitado < numero_secreto

    if (acertou):
        print("Você acertou!")
        rodada = 4

    else:
        if (maior):
            print("O numero secreto é menor!")
        elif(menor):
            print("O numero secreto é maior")

    rodada = rodada + 1

print("Fim do Jogo")
