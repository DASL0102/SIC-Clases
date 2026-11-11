import pandas as pd
import matplotlib.pyplot as plt

print("\n=== 5. VISUALIZACIÓN DE DATOS CON MATPLOTLIB ===")

# Creación de una Serie demográfica estructurada
poblacion_megaciudades = pd.Series({
    'Tokyo': 37339804,
    'Delhi': 31181376,
    'Shanghai': 27795702,
    'Sao Paulo': 22237472,
    'Mexico City': 21918936,
    'Cairo': 21322750
})

# 1. Configurar las dimensiones del lienzo en pulgadas
plt.figure(figsize=(10, 5))

# 2. Generar el gráfico de barras horizontal utilizando el método integrado de Pandas
poblacion_megaciudades.plot(kind='barh', color='rebeccapurple', edgecolor='black')

# 3. Incorporar metadatos y etiquetas institucionales al gráfico
plt.title('Demografía Global: Top Megaciudades del Mundo', fontsize=14, fontweight='bold')
plt.xlabel('Población Total (Habitantes)', fontsize=12)
plt.ylabel('Áreas Metropolitanas', fontsize=12)

# 4. Ajustar diseño y renderizar la interfaz gráfica en pantalla
plt.tight_layout()
print("Renderizando ventana gráfica interactiva...")
#plt.show()
# En lugar de plt.show()
plt.savefig('poblacion_megaciudades.png', dpi=300, bbox_inches='tight')
print("Gráfico guardado exitosamente como 'poblacion_megaciudades.png'.")