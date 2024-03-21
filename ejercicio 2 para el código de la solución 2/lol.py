# Importar la librería para pruebas unitarias
import unittest
from ejercicio2 import refactor_calculate_points,refactor_determine_champion

class TestRacingFunctions(unittest.TestCase):
    def test_calculate_points(self):
        # Prueba que la función asigna correctamente los puntos
        positions = [1, 2, 3, 4]
        scoring_system = [10, 8, 6, 5]
        expected_points = [10, 8, 6, 5]
        self.assertEqual(refactor_calculate_points(positions, scoring_system), expected_points)

    def test_calculate_points_out_of_range(self):
        # Prueba cómo se manejan las posiciones fuera del rango del sistema de puntuación
        positions = [1, 5]  # La posición 5 no está en el sistema de puntuación
        scoring_system = [10, 8, 6]
        expected_points = [10, 0]  # Se espera 0 puntos para la posición 5
        self.assertEqual(refactor_calculate_points(positions, scoring_system), expected_points)

    def test_determine_champion_single_winner(self):
        # Prueba la identificación correcta de un único ganador
        points = [10, 8, 6, 5]
        expected_champion = [1]  # El primer competidor es el campeón
        self.assertEqual(refactor_determine_champion(points), expected_champion)

    def test_determine_champion_tie(self):
        # Prueba la identificación correcta de múltiples ganadores en caso de empate
        points = [10, 10, 6, 5]  # Los primeros dos competidores están empatados
        expected_champions = [1, 2]
        self.assertEqual(refactor_determine_champion(points), expected_champions)


# Ejecutar las pruebas unitarias
unittest.main(argv=[''], exit=False)
