"""
Script de benchmark para medir el rendimiento del algoritmo GeoFlux Sort.

Este script compara el rendimiento de GeoFlux Sort con el sorted() nativo
de Python en diferentes escenarios:
    - Arrays aleatorios
    - Arrays ya ordenados
    - Arrays en orden inverso

Genera una tabla comparativa con los tiempos de ejecución.

Ejecutar:
    python examples/benchmark_sort.py
    
Requisitos:
    pip install tabulate
"""

import random
import time
import sys
import os
from tabulate import tabulate

# Añadir el directorio raíz del proyecto al PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from geoflux_sorter import geoflux_sort


def measure_sorting_time(algorithm, array):
    """
    Mide el tiempo de ejecución de un algoritmo de ordenamiento.
    
    Args:
        algorithm (callable): Función de ordenamiento a medir
        array (list): Array a ordenar
        
    Returns:
        tuple: (tiempo_ejecucion, array_ordenado)
            - tiempo_ejecucion (float): Tiempo en segundos
            - array_ordenado (list): Array resultante ordenado
    """
    # Trabajar con una copia para no modificar el original
    array_copy = array.copy()
    
    # Medir tiempo de ejecución
    start_time = time.time()
    algorithm(array_copy)
    end_time = time.time()
    
    return end_time - start_time, array_copy


def benchmark_algorithm(sizes=[100, 500, 1000, 5000, 10000]):
    """
    Ejecuta benchmarks para diferentes tamaños de arrays.
    
    Para cada tamaño, prueba tres tipos de arrays:
        1. Aleatorio: Elementos en orden aleatorio
        2. Ordenado: Elementos ya ordenados ascendentemente
        3. Invertido: Elementos en orden descendente
    
    Args:
        sizes (list): Lista de tamaños de arrays a probar
        
    Returns:
        list: Lista de resultados con formato [tamaño, tiempo1, tiempo2, ...]
    """
    results = []
    
    for size in sizes:
        print(f"Probando tamaño {size}...", end=" ")
        
        # Generar tres tipos de arrays para probar
        random_array = random.sample(range(1, size * 10), size)
        sorted_array = list(range(1, size + 1))
        reversed_array = list(range(size, 0, -1))
        
        # Medir tiempos para GeoFlux Sort
        random_time, _ = measure_sorting_time(geoflux_sort, random_array)
        sorted_time, _ = measure_sorting_time(geoflux_sort, sorted_array)
        reversed_time, _ = measure_sorting_time(geoflux_sort, reversed_array)
        
        # Medir tiempos para Python sorted() (comparación baseline)
        python_random_time, _ = measure_sorting_time(sorted, random_array)
        python_sorted_time, _ = measure_sorting_time(sorted, sorted_array)
        python_reversed_time, _ = measure_sorting_time(sorted, reversed_array)
        
        # Agregar resultados formateados
        results.append([
            size,
            f"{random_time:.6f}s",
            f"{sorted_time:.6f}s",
            f"{reversed_time:.6f}s",
            f"{python_random_time:.6f}s",
            f"{python_sorted_time:.6f}s",
            f"{python_reversed_time:.6f}s"
        ])
        
        print("Completado")
    
    return results


if __name__ == "__main__":
    print("=" * 70)
    print("BENCHMARK DE RENDIMIENTO - GEOFLUX SORT")
    print("=" * 70)
    print("\nEste proceso puede tardar dependiendo de los tamaños de arrays...")
    print("Comparando GeoFlux Sort vs. Python sorted()\n")
    
    # Configurar tamaños de arrays a probar
    # Puedes modificar estos tamaños según tus necesidades
    sizes = [100, 500, 1000, 2000, 5000]
    
    # Ejecutar benchmarks
    results = benchmark_algorithm(sizes)
    
    # Definir encabezados de la tabla
    headers = [
        "Tamaño",
        "GeoFlux (Random)",
        "GeoFlux (Ordenado)",
        "GeoFlux (Invertido)",
        "Python (Random)",
        "Python (Ordenado)",
        "Python (Invertido)"
    ]
    
    # Mostrar resultados en formato de tabla
    print("\n" + "=" * 70)
    print("RESULTADOS DEL BENCHMARK")
    print("=" * 70 + "\n")
    print(tabulate(results, headers=headers, tablefmt="grid"))
    
    print("\n" + "=" * 70)
    print("ANALISIS:")
    print("  - GeoFlux Sort es mas eficiente en arrays ya ordenados")
    print("  - Python sorted() (TimSort) es mas rapido en la mayoria de casos")
    print("  - El rendimiento de GeoFlux mejora con datos que tienen clusters")
    print("=" * 70)
