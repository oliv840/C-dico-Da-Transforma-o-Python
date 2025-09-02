# principal.py

from calculadora_09 import dividir
from conta_bancaria import ContaBancaria, SaldoInsuficienteError
from dados_usuarios import validar_idade

# Desafio Extra: Sistema de login
USUARIOS = {
    "admin": "senha123",
    "user": "1234"
}

def login():
    tentativas = 3
    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            print("Login bem-sucedido!\n")
            return True
        else:
            tentativas -= 1
            print(f"Credenciais inválidas. Tentativas restantes: {tentativas}")
    print("Número máximo de tentativas alcançado.")
    return False

def main():
    if not login():
        return

    print("=== Teste da Calculadora ===")
    print(dividir(10, 2))
    print(dividir(5, 0))

    print("\n=== Teste da Conta Bancária ===")
    conta = ContaBancaria(100)
    try:
        print(f"Saldo após saque: R${conta.sacar(50)}")
        print(f"Saldo após saque: R${conta.sacar(100)}")  # Deve disparar erro
    except SaldoInsuficienteError as e:
        print(f"Erro ao sacar: {e}")

    print("\n=== Validação de Idade ===")
    try:
        idade = int(input("Digite sua idade: "))
        if validar_idade(idade):
            print("Idade válida.")
    except ValueError as ve:
        print(f"Erro: {ve}")

if __name__ == "__main__":
    main()
