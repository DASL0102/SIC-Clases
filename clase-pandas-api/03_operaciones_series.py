import pandas as pd

print("\n=== 3. INDEXACIÓN, SELECCIÓN Y OPERACIONES CON NaN ===")

# Creación de una Serie con etiquetas de índice alfabéticas personalizadas
elementos_base = ['Elemento_A', 'Elemento_B', 'Elemento_C', 'Elemento_D']
serie_etiquetada = pd.Series(elementos_base, index=['w', 'x', 'y', 'z'])
print("Serie con índices etiquetados:")
print(serie_etiquetada)

# 1. Selección de elementos específicos
print(f"\nSelección por etiqueta única ['y']: {serie_etiquetada['y']}")
print("\nSelección por múltiples etiquetas [['w', 'z']]:")
print(serie_etiquetada[['w', 'z']])

# 2. Operaciones aritméticas entre dos Series y generación de NaN
serie_a = pd.Series([10, 20, 30, 40], index=[0, 1, 2, 3])
serie_b = pd.Series([5, 15, 25], index=[0, 1, 2]) # Falta el índice 3

resultado_suma = serie_a + serie_b
print("\n--- Resultado de Operación Aritmética (Alineación con NaN) ---")
print(resultado_suma)