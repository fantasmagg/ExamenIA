import unittest
from solucion_palindromo import es_palindromo

class TestPalindromePositive(unittest.TestCase):
    def test_palindrome_positive(self):
        resultado = es_palindromo("ANA")
        self.assertTrue(resultado)
        with open('output_test_palindrome_positive.txt', 'w') as f:
            f.write(f"# Output de la prueba unitaria test_palindrome_positive\n")
            f.write("# Resultado esperado: True (debido a que 'ANA' es un palindromo)\n")
            f.write(str(resultado))
if __name__ == '__main__':
    unittest.main()