# Lógica: Verifica a faixa etária com base na idade informada

idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade < 12:
    print("Você é uma criança.")
elif idade < 18:
    print("Você é um adolescente.")
elif idade < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
