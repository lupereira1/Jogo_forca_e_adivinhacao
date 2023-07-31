# Jogo do número secreto python
import random
def jogar():

    import random
    print("Bem vindo ao jogo do número secreto!")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Em qual nível de dificuldade você deseja jogar?")
    print(" (1) Fácil (2) Médio (3) Difícil  ")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 15
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou e fez {pontos} pontos no jogo!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

                
    print(f"Fim do jogo, o número secreto era {numero_secreto}!")

if (__name__ == "__main__"):
    jogar()
