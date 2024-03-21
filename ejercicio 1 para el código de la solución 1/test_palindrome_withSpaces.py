import unittest
from solucion_palindromo import es_palindromo

class Test_palindrome_withSpaces(unittest.TestCase):
    def testConEspacio(self):
        resultado = es_palindromo("Se verlas al reves")
        self.assertTrue(resultado)
        with open('output_test_palindrome_withSpaces.txt', 'w') as f:
            f.write(f"# Output de la prueba unitaria test_palindrome_withSpaces\n")
            f.write("# Resultado esperado: True esta oracion 'Se verlas al reves' es palindrome\n")
            f.write(str(resultado))
if __name__ == '__main__':
    unittest.main()