def refactor_calculate_points(positions, scoring_system):
    # Calcula los puntos obtenidos por cada competidor según el sistema de puntuación
    return [scoring_system[pos - 1] if pos <= len(scoring_system) else 0 for pos in positions]

def refactor_determine_champion(total_points):
    # Determina el índice de los competidores con la mayor cantidad de puntos
    max_points = max(total_points)
    return [i + 1 for i, p in enumerate(total_points) if p == max_points]

# Procesamiento de la entrada refactorizado para mayor claridad
def process_input(input_data):
    lines = input_data.split('\n')
    i = 0
    results = []
    while i < len(lines):
        G, P = map(int, lines[i].split())
        if G == 0 and P == 0: break  # Condición de terminación
        races_results = [list(map(int, lines[j].split())) for j in range(i + 1, i + G + 1)]
        S = int(lines[i + G + 1])
        scoring_systems = [list(map(int, lines[k].split())) for k in range(i + G + 2, i + G + S + 2)]
        # Calcula y agrega los resultados para este conjunto de carreras y sistemas de puntuación
        results.extend(process_races(P, races_results, scoring_systems))
        i += G + S + 2
    return results

def process_races(P, races_results, scoring_systems):
    # Procesa cada sistema de puntuación para las carreras dadas
    race_results = []
    for scoring in scoring_systems:
        total_points = [0] * P
        for race in races_results:
            points = refactor_calculate_points(race, scoring[1:])
            total_points = [sum(x) for x in zip(total_points, points)]
        champions = refactor_determine_champion(total_points)
        race_results.append(' '.join(map(str, champions)))
    return race_results

# Entrada de ejemplo
input_data_example = '''1 3
3 2 1
3
3 5 3 2
3 5 3 1
3 1 1 1
3 10
1 2 3 4 5 6 7 8 9 10
10 1 2 3 4 5 6 7 8 9
9 10 1 2 3 4 5 6 7 8
2
5 5 4 3 2 1
3 10 5 1
2 4
1 3 4 2
4 1 3 2
2
3 3 2 1
3 5 4 2
0 0'''

# Procesar entrada y generar salida
refactored_output = process_input(input_data_example)
for i in range(len(refactored_output)):
    print(refactored_output[i])
