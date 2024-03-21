# Instrucciones para Ejecutar el Código

Este repositorio contiene una solución para un problema de palíndromos.

## Requisitos

Antes de ejecutar el código, asegúrate de tener Python instalado en tu sistema. Además, necesitarás instalar la librería
`unidecode` para manejar caracteres con acentos. Puedes instalarla usando pip:
## Consola
pip install unidecode

pip install unittest

## Archivos Disponibles

- `solucion_palindromo.py`: Contiene la implementación de la función `es_palindromo` para verificar si una cadena es un palíndromo.
- `test_palindrome_positivo.py`, `test_palindrome_negativo.py`, `test_palindrome_withSpaces.py`: Archivos de prueba unitaria
- para probar la función `es_palindromo`.
- `output_test_palindrome_positivo.txt`, `output_test_palindrome_negativo.txt`, `output_test_palindrome_withSpaces.txt`: 
- Archivos de salida con los resultados esperados de las pruebas unitarias correspondientes.

## Ejecutar las Pruebas

Para ejecutar las pruebas unitarias, puedes usar el siguiente comando en la terminal:

#comando test 1
python -m unittest test_palindrome_positivo.py

#comando test 2
python -m unittest test_palindrome_negativo.py

#comando test 3
python -m unittest test_palindrome_withSpaces.py


## Informacion Adicional

- Asegúrate de tener Python instalado en tu sistema antes de ejecutar las pruebas.
- Puedes agregar mas pruebas unitarias o funciones en el archivo `solucion_palindromo.py` y sus archivos de prueba correspondientes.