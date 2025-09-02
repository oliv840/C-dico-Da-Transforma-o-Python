# módulo_03/dicionario.py
# Trabalhando com dicionários para armazenar e acessar dados

# Dicionário com notas de alunos
notas_alunos = {
    "Ana": 8.5,
    "Bruno": 6.0,
    "Carlos": 9.2,
    "Diana": 7.8
}

# Acessar dados
print("Nota de Ana:", notas_alunos["Ana"])

# Adicionar novo aluno
notas_alunos["Eduardo"] = 5.9

# Atualizar nota
notas_alunos["Bruno"] = 7.0

# Remover aluno
del notas_alunos["Carlos"]

# Exibir todos os alunos e notas
for aluno, nota in notas_alunos.items():
    print(f"{aluno}: {nota}")
