# expressoes-matematica.py

def calcular_divisao(a, b):
    try:
        resultado = a / b
        print(f"Resultado da divisão: {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

# Exemplo de uso
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
calcular_divisao(num1, num2)
