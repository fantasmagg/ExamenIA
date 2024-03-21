import unittest
from ejercicio2 import refactor_calculate_points,refactor_determine_champion
class Test_determine_champion_tie(unittest.TestCase):
    def test_determine_champion_tie(self):
        # Prueba que la función asigna correctamente los puntos
        points = [10, 10, 6, 5]
        expected_champions = [1, 2]
        resultado = refactor_determine_champion(points)
        self.assertEqual(resultado, expected_champions)


        with open('output_test_determine_champion_tie.txt', 'w') as f:
                f.write(f"# Output de la prueba unitaria test_determine_champion_tie\n")
                f.write("# Resultado esperado:[1, 2]\n")
                f.write(str(resultado))
if __name__ == '__main__':
    unittest.main()