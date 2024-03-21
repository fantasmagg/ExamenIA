import unittest
from ejecisio3 import min_jumps_simplified

class TestCase3(unittest.TestCase):
    def test_case_3(self):
        resultado = min_jumps_simplified(3)
        self.assertEqual(resultado, 2)

        with open('output_test_case_3.txt', 'w') as f:
            f.write("# Output de la prueba unitaria test_case_3\n")
            f.write("# Resultado esperado: 2\n")
            f.write(str(resultado))

if __name__ == '__main__':
    unittest.main()
