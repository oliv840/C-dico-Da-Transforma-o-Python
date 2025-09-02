# módulo_03/estruturas_dados.py
# Trabalhando com listas e list comprehension

# Lista de números de 1 a 20
numeros = list(range(1, 21))

# List comprehension para quadrados
quadrados = [n ** 2 for n in numeros]
print("Quadrados de 1 a 20:", quadrados)

# Filtrar pares
pares = [n for n in numeros if n % 2 == 0]
print("Números pares:", pares)

# Filtrar múltiplos de 3 maiores que 10
multiplos_de_3 = [n for n in numeros if n % 3 == 0 and n > 10]
print("Múltiplos de 3 maiores que 10:", multiplos_de_3)
