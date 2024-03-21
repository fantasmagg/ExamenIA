import unittest
from ejercicio2 import refactor_calculate_points,refactor_determine_champion
class Test_calculate_points_out_of_range(unittest.TestCase):
    def test_calculate_points_out_of_range(self):
        # Prueba que la función asigna correctamente los puntos
        positions = [1, 5]
        scoring_system = [10, 8, 6]
        expected_points = [10, 0]
        resultado =refactor_calculate_points(positions, scoring_system)

        self.assertEqual(resultado, expected_points)

        with open('output_test_calculate_points_out_of_range.txt', 'w') as f:
                f.write(f"# Output de la prueba unitaria test_calculate_points_out_of_range\n")
                f.write("# Resultado esperado: [10, 0]\n")
                f.write(str(resultado))
if __name__ == '__main__':
    unittest.main()