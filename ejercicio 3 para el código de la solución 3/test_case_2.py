import unittest
from ejecisio3 import min_jumps_simplified
class TestCase2(unittest.TestCase):
    def test_case_2(self):
        resultado = min_jumps_simplified(2)
        self.assertEqual(resultado, 3)

        with open('output_test_case_2.txt', 'w') as f:
            f.write("# Output de la prueba unitaria test_case_2\n")
            f.write("# Resultado esperado: 3\n")
            f.write(str(resultado))

if __name__ == '__main__':
    unittest.main()
