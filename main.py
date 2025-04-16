import random
import time


def sortear_bingo():
    numeros = list(range(1, 76))
    random.shuffle(numeros)

    print("🔔 Sorteador de Bingo Iniciado!\n")

    for numero in numeros:
        if numero <= 15:
            letra = 'B'
        elif numero <= 30:
            letra = 'I'
        elif numero <= 45:
            letra = 'N'
        elif numero <= 60:
            letra = 'G'
        else:
            letra = 'O'

        print(f"🎱 Número sorteado: {letra}-{numero}")
        input("Pressione ENTER para sortear o próximo número...")


if __name__ == "__main__":
    sortear_bingo()
