"""
Ejemplo de visualización animada del algoritmo GeoFlux Sort.

Este script crea una animación interactiva que muestra el proceso
de ordenamiento paso a paso, permitiendo observar cómo los grupos
de elementos similares migran a través del arreglo.

Ejecutar:
    python examples/run_animation_example.py
    
Nota:
    La animación se mostrará en una ventana de matplotlib.
    Cierra la ventana para finalizar el programa.
"""

import random
import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from geoflux_sorter import create_geoflux_animation


if __name__ == "__main__":
    print("=" * 60)
    print("VISUALIZACION DEL ALGORITMO GEOFLUX SORT")
    print("=" * 60)
    
    # Configuración de datos para animar
    # Puedes modificar estas líneas para probar diferentes casos
    
    # Opción 1: Datos aleatorios (por defecto)
    sample_data = [random.randint(0, 100) for _ in range(100)]
    
    # Opción 2: Lista en orden inverso (descomenta para usar)
    # sample_data = list(range(50, 0, -1))
    
    # Opción 3: Lista parcialmente ordenada (descomenta para usar)
    # sample_data = [10, 20, 30, 40, 50, 5, 15, 25, 35, 45]
    
    # Opción 4: Lista con grupos naturales (descomenta para usar)
    # sample_data = [5, 6, 7, 45, 46, 47, 15, 16, 17, 25, 26, 27]
    
    print(f"\nDatos para animar ({len(sample_data)} elementos)")
    print(f"Primeros 10 valores: {sample_data[:10]}...")
    print(f"\nCreando animacion...")
    print("(Cierra la ventana de matplotlib para finalizar)\n")
    
    # Crear y mostrar la animación
    # interval: tiempo en milisegundos entre frames (menor = más rápido)
    animation_obj = create_geoflux_animation(sample_data, interval=10)
    
    # Para guardar la animación como video, descomenta la siguiente línea:
    # (Requiere ffmpeg instalado)
    # animation_obj = create_geoflux_animation(
    #     sample_data,
    #     interval=200,
    #     save_to_file="geoflux_sort.mp4"
    # )
    
    print("Animacion completada.")
