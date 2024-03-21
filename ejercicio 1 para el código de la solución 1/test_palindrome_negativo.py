import unittest
from solucion_palindromo import es_palindromo

class TestPalindromeNegativo(unittest.TestCase):
    def testPlNegativo(self):
        resultado = es_palindromo("hola mundo")
        self.assertFalse(resultado)
        with open("output_test_palindrome_negativo.txt","w") as f:
            f.write("# Output de la prueba unitaria test_palindrome_negatio\n")
            f.write("# Resultado esperado es: False, ya que 'hola mundo' no es palindromo\n")
            f.write(str(resultado))
if __name__ == '__main__':
    unittest.main()

