import unittest
from ejecisio3 import min_jumps_simplified
class TestCase1(unittest.TestCase):
    def test_case_1(self):
        resultado = min_jumps_simplified(1)
        self.assertEqual(resultado, 1)

        with open('output_test_case_1.txt', 'w') as f:
            f.write("# Output de la prueba unitaria test_case_1\n")
            f.write("# Resultado esperado: 1\n")
            f.write(str(resultado))

if __name__ == '__main__':
    unittest.main()
