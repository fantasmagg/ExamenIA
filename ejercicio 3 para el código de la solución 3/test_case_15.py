import unittest
from ejecisio3 import min_jumps_simplified
class TestCase15(unittest.TestCase):
    def test_case_15(self):
        resultado = min_jumps_simplified(15)
        self.assertEqual(resultado, 5)

        with open('output_test_case_15.txt', 'w') as f:
            f.write("# Output de la prueba unitaria test_case_15\n")
            f.write("# Resultado esperado: 5\n")
            f.write(str(resultado))

if __name__ == '__main__':
    unittest.main()
