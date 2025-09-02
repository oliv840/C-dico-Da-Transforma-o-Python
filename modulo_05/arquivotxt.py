# módulo_05/arquivotxt.py
# Trabalhando com arquivos .txt

def escrever_txt():
    with open("dados.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Olá! Este é um arquivo de texto.\n")
        arquivo.write("Podemos escrever várias linhas aqui.\n")
        arquivo.write("Este é o módulo arquivotxt.py\n")
    print("Arquivo 'dados.txt' criado com sucesso!")

def ler_txt():
    try:
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado. Escreva antes de ler.")

# Executando funções
escrever_txt()
ler_txt()
