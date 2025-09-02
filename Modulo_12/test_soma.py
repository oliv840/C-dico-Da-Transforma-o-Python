import unittest
from calculadora import Calculadora

class TestSoma(unittest.TestCase):
    """
    Testes unitários para validar a operação de soma.

    Atividade 1:
    Desenvolver um teste simples que assegure o funcionamento correto
    da função responsável por realizar somas.
    """

    def test_soma_simples(self):
        """Verifica se a soma de dois valores inteiros é realizada corretamente."""
        calc = Calculadora()
        self.assertEqual(calc.somar(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
