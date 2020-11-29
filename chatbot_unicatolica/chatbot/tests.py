from django.test import TestCase

# Create your tests here.


def soma(x, y):
    resultado = x + y
    return resultado


class MeusTestes(TestCase):

    def test_soma_dois_mais_dois_igual_quatro(self):
        resultado = soma(2, 2)
        resultado_esperado = 4
        self.assertEqual(resultado, resultado_esperado)

    def test_soma_dois_mais_quatro_igual_seis(self):
        resultado = soma(2, 4)
        resultado_esperado = 6
        self.assertEqual(resultado, resultado_esperado)


