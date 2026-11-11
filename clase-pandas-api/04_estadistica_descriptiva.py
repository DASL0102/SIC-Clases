import pandas as pd

print("\n=== 4. MÉTODOS DE ESTADÍSTICA DESCRIPTIVA EN PANDAS ===")

# Construcción de una Serie con valores numéricos y presencia de NaN
datos_numericos = pd.Series([12.5, 45.0, 33.2, None, 88.4, 21.0, None])
print("Serie numérica con datos nulos (NaN):")
print(datos_numericos)

# Aplicando funciones de estadística descriptiva del material de estudio
print(f"\nCantidad de registros válidos (count): {datos_numericos.count()}") # Omite NaN
print(f"Suma total de los valores (sum): {datos_numericos.sum()}")
print(f"Promedio o media aritmética (mean): {datos_numericos.mean():.2f}")
print(f"Mediana estadística (median): {datos_numericos.median()}")
print(f"Valor mínimo registrado (min): {datos_numericos.min()}")
print(f"Valor máximo registrado (max): {datos_numericos.max()}")
print(f"Desviación estándar (std): {datos_numericos.std():.2f}")

# Operaciones acumulativas
print("\nSuma acumulada secuencial (cumsum):")
print(datos_numericos.cumsum())