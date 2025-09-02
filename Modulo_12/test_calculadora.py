import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    """
    Testes unitários para a classe Calculadora.

    Atividade 2:
    Desenvolver cenários de teste para os métodos de soma e divisão.

    Atividade 3:
    Validar o comportamento do programa diante de entradas inválidas,
    como a tentativa de realizar divisão por zero.
    """

    def setUp(self):
        """Instancia a classe Calculadora antes de cada teste."""
        self.calc = Calculadora()

    def test_soma(self):
        """Valida se o método somar retorna o valor esperado."""
        self.assertEqual(self.calc.somar(10, 5), 15)

    def test_divisao(self):
        """Valida se o método dividir retorna o valor correto."""
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_divisao_por_zero(self):
        """Assegura que a divisão por zero resulta em exceção adequada."""
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == "__main__":
    unittest.main()
