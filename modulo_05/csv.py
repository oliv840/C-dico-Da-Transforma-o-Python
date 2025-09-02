# módulo_05/csv.py
# Trabalhando com arquivos CSV

import csv

def salvar_csv():
    with open("alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Nome", "Nota"])
        escritor.writerow(["Lucas", 8.5])
        escritor.writerow(["Marina", 9.0])
        escritor.writerow(["João", 7.2])
    print("Arquivo 'alunos.csv' salvo com sucesso!")

def ler_csv():
    try:
        with open("alunos.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            print("Conteúdo do CSV:")
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")

# Executando funções
salvar_csv()
ler_csv()
