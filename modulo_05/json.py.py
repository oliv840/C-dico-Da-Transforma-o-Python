# módulo_05/json.py
# Trabalhando com arquivos JSON

import json

def salvar_json():
    dados = {
        "nome": "Ana",
        "idade": 25,
        "cursos": ["Python", "Git", "Lógica"],
        "ativo": True
    }
    with open("usuario.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)
    print("Arquivo 'usuario.json' salvo com sucesso!")

def carregar_json():
    try:
        with open("usuario.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            print("Dados carregados do JSON:")
            print(dados)
    except FileNotFoundError:
        print("Arquivo JSON não encontrado.")

# Executando funções
salvar_json()
carregar_json()
