import unittest
from ejercicio2 import refactor_calculate_points,refactor_determine_champion
class Test_determine_champion_single_winner(unittest.TestCase):
    def test_determine_champion_single_winner(self):
        # Prueba que la función asigna correctamente los puntos
        points = [10, 8, 6, 5]
        expected_champion = [1]  # El primer competidor es el campeón
        resultado = refactor_determine_champion(points)
        self.assertEqual(refactor_determine_champion(points), expected_champion)

        with open('output_test_determine_champion_single_winner.txt', 'w') as f:
                f.write(f"# Output de la prueba unitaria test_determine_champion_single_winner\n")
                f.write("# Resultado esperado: [1]\n")
                f.write(str(resultado))
if __name__ == '__main__':
    unittest.main()