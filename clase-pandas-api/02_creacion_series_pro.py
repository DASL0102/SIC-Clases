import pandas as pd
import numpy as np

print("\n=== 2. CREACIÓN DE OBJETOS SERIES EN PANDAS ===")

# 1. Crear Serie desde una lista de Python (Índices automáticos enteros 0, 1, 2...)
artistas_pop = ['Post Malone', 'Taylor Swift', 'The Weeknd', 'Drake']
serie_lista = pd.Series(artistas_pop)
print("\n--- A. Serie construida desde Lista ---")
print(serie_lista)

# 2. Crear Serie desde un Diccionario (Claves = Índices personalizados)
poblacion_capitales = {'Tokyo': 37339804, 'Delhi': 31181376, 'Cairo': 21322750}
serie_dict = pd.Series(poblacion_capitales)
print("\n--- B. Serie construida desde Diccionario ---")
print(serie_dict)

# 3. Crear Serie utilizando un array de NumPy
array_numerico = np.linspace(10, 50, 5) # 5 números equispaceados entre 10 y 50
serie_numpy = pd.Series(array_numerico)
print("\n--- C. Serie construida desde NumPy Array ---")
print(serie_numpy)

# 4. Creación de una Serie de Tiempo con un DatetimeIndex
rango_fechas = pd.date_range(start='2026-01-01', periods=3, freq='D')
serie_temporal = pd.Series([105.2, 108.4, 107.9], index=rango_fechas)
print("\n--- D. Serie de Tiempo con Índices Datetime ---")
print(serie_temporal)