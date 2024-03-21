def min_jumps_simplified(x):
    jumps = 0
    total = 0

    while total < x:
        jumps += 1
        total += jumps
        if total >= x:
            if (total - x) % 2 == 0:
                return jumps
            else:
                jumps += 1
                total += jumps

    return jumps
inputs = [5, 1,2,3,4,5]
# Aplicando la función simplificada a los mismos casos de prueba para verificar que la salida sea la misma
simplified_outputs = [min_jumps_simplified(x) for x in inputs[1:]]

print(simplified_outputs)