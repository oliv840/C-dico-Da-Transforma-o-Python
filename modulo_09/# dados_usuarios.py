# dados_usuarios.py

def validar_idade(idade):
    if not isinstance(idade, int):
        raise ValueError("Idade deve ser um número inteiro.")
    if idade <= 0:
        raise ValueError("Idade deve ser um número positivo.")
    return True
