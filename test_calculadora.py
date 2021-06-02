import unittest
from calculadora import soma

# Todos os testes criados devem iniciar com a palavra test para serem executados

class TesteCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)
        
    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        # self.assertEqual(soma(-5, 5), 1) # Forçando uma falha
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (1, 2, 3),
            (5, -2, 3),
            (7, 2, 9),
            (1000, 24, 1024),
            (1.13, 2, 3.13),
            (7.25, 2.5, 9.75),
        )

        for x_y_saida in x_y_saidas:
            x, y, saida = x_y_saida
            self.assertEqual(soma(x, y), saida)
    
    # Este teste passará pois tratamos essa possibilidade com AssertionError lá na função soma()
    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('2', 1)
    
    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(2, '1')

unittest.main(verbosity=2)