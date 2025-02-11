import unittest
from ejecisio3 import min_jumps_simplified
class TestCase10(unittest.TestCase):
    def test_case_10(self):
        resultado = min_jumps_simplified(10)
        self.assertEqual(resultado, 4)

        with open('output_test_case_10.txt', 'w') as f:
            f.write("# Output de la prueba unitaria test_case_10\n")
            f.write("# Resultado esperado: 4\n")
            f.write(str(resultado))

if __name__ == '__main__':
    unittest.main()
