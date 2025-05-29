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
    """Mide el tiempo que tarda en ordenarse un array"""
    array_copy = array.copy()  # Trabajar con una copia para no modificar el original
    start_time = time.time()
    algorithm(array_copy)
    end_time = time.time()
    return end_time - start_time, array_copy

def benchmark_algorithm(sizes=[100, 500, 1000, 5000, 10000]):
    """Ejecuta benchmarks para diferentes tamaños de arrays"""
    results = []
    
    for size in sizes:
        # Generar arrays aleatorios
        random_array = random.sample(range(1, size*10), size)
        sorted_array = list(range(1, size+1))
        reversed_array = list(range(size, 0, -1))
        
        # Medir tiempos para cada tipo de array
        random_time, _ = measure_sorting_time(geoflux_sort, random_array)
        sorted_time, _ = measure_sorting_time(geoflux_sort, sorted_array)
        reversed_time, _ = measure_sorting_time(geoflux_sort, reversed_array)
        
        # Medir tiempos de Python sorted() para comparación
        python_random_time, _ = measure_sorting_time(sorted, random_array)
        python_sorted_time, _ = measure_sorting_time(sorted, sorted_array)
        python_reversed_time, _ = measure_sorting_time(sorted, reversed_array)
        
        results.append([
            size,
            f"{random_time:.6f}s", 
            f"{sorted_time:.6f}s",
            f"{reversed_time:.6f}s",
            f"{python_random_time:.6f}s",
            f"{python_sorted_time:.6f}s",
            f"{python_reversed_time:.6f}s"
        ])
    
    return results

if __name__ == "__main__":
    print("Ejecutando benchmark para GeoFlux Sort...")
    print("Este proceso puede tardar dependiendo de los tamaños de arrays...")
    
    # Puedes modificar estos tamaños según tus necesidades
    sizes = [100, 500, 1000, 2000, 5000]
    results = benchmark_algorithm(sizes)
    
    headers = [
        "Tamaño", 
        "GeoFlux (Random)", 
        "GeoFlux (Ordenado)", 
        "GeoFlux (Invertido)", 
        "Python (Random)",
        "Python (Ordenado)",
        "Python (Invertido)"
    ]
    
    print("\nResultados del benchmark:")
    print(tabulate(results, headers=headers, tablefmt="grid"))