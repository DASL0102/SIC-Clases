import math
import random
import time
from datetime import datetime, timedelta
import os

print("=== 1. DEMOSTRACIÓN DE MÓDULOS ESTÁNDAR ===")

# 1. Módulo math: Funciones matemáticas avanzadas
valor_seno = math.sin(math.radians(90)) # Seno de 90 grados convertido a radianes
print(f"Seno de 90 grados: {valor_seno}")

# 2. Módulo random: Generación de números aleatorios y muestreo
flotante_azar = random.random() # Devuelve un flotante entre [0.0, 1.0)
entero_azar = random.randint(1, 100) # Entero aleatorio entre 1 y 100
print(f"Número flotante aleatorio [0,1): {flotante_azar}")
print(f"Número entero aleatorio (1-100): {entero_azar}")

# Muestreo sin reemplazo de una lista de elementos
lenguajes = ['Python', 'JavaScript', 'C++', 'Java', 'TypeScript', 'Kotlin']
seleccion_aleatoria = random.sample(lenguajes, 3)
print(f"Muestreo aleatorio de 3 lenguajes: {seleccion_aleatoria}")

# 3. Módulos time y datetime: Control de pausas y marcas de tiempo
print("Pausando la ejecución por 1 segundo...")
time.sleep(1) # Detiene el hilo de ejecución durante 1 segundo

ahora = datetime.now() # Fecha y hora actual del sistema
print(f"Timestamp actual detallado: {ahora}")

# Uso de timedelta para calcular fechas futuras
plazo_entrega = ahora + timedelta(days=15, hours=4)
print(f"Fecha límite exacta en 15 días y 4 horas: {plazo_entrega.strftime('%Y-%m-%d %H:%M:%S')}")

# 4. Módulo os: Consultas al sistema operativo
directorio_actual = os.getcwd()
print(f"Directorio de trabajo actual (OS): {directorio_actual}")