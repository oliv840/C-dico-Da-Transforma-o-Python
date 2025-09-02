# módulo_06/jogodeadivinhacao.py
# Aqui está toda a lógica do jogo de adivinhação

import random
from utilidades import obter_numero_inteiro

def jogar_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número de 1 a 100...")

    numero_secreto = random.randint(1, 100)  # O computador escolhe um número aleatório
    tentativas = 0
    acertou = False

    while not acertou:
        chute = obter_numero_inteiro("Digite seu palpite: ")
        tentativas += 1

        if chute < numero_secreto:
            print("Tente um número maior.")
        elif chute > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            acertou = True
