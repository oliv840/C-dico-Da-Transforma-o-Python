# conta_bancaria.py

class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para saque.")
        self.saldo -= valor
        return self.saldo
