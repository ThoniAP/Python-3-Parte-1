print("*******************************************")
print("Bem vindo ao jogo de adivinhação")
print("*******************************************")

numero_secreto = 45

numero_digitado = int(input("Digite um numero:"))

if numero_secreto == numero_digitado:
    print("Você acertou!")

else:
    print("Você errou!")

print("Fim do Jogo")