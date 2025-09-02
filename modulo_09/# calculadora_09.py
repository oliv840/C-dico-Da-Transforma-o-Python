# calculadora_09.py

def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
