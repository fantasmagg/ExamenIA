def es_palindromo(texto): return (lambda s: s == s[::-1])( ''.join('a' if c in 'á' else 'e' if c in 'é' else 'i' if c in 'í' else 'o' if c in 'ó' else 'u' if c in 'ú' else c for c in texto.lower().replace(" ", "")) )
print("Es un palíndromo." if es_palindromo("aná") else "No es un palíndromo.")
