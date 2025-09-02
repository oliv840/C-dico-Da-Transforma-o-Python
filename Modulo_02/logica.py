def soma(a: int, b: int) -> int:
    return a + b

def maioridade(idade: int) -> str:
    return 'Maior de idade' if idade >= 18 else 'Menor de idade'

if __name__ == '__main__':
    print(soma(10, 5))
    print(maioridade(20))
