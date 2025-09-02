class Calculadora:
    '''Classe que implementa operações matemáticas básicas.'''

    def somar(self, a: float, b: float) -> float:
        return a + b

    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError('Divisão por zero não é permitida.')
        return a / b
