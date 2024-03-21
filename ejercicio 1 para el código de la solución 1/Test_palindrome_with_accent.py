import unittest
from solucion_palindromo import es_palindromo

class TestPalindromeWithAccent(unittest.TestCase):
    def test_palindrome_with_accent(self):
        resultado = es_palindromo("Dábale arroz a la zorra el abad")
        self.assertTrue(resultado)
        with open("output_test_palindrome_with_accent.txt", "w") as f:
            f.write("# Output de la prueba unitaria test_palindrome_with_accent\n")
            f.write("# Resultado esperado es: True\n")
            f.write(str(resultado))
if __name__ == '__main__':
    unittest.main()
