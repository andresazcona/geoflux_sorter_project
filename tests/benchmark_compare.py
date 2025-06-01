import random
import time
import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Importar el algoritmo original y optimizado
from geoflux_sorter import geoflux_sort

# Implementación del algoritmo original para comparar
def geoflux_sort_original(arr):
    """
    Versión original del algoritmo GeoFlux Sort (para comparación)
    """
    n = len(arr)
    if n <= 1:
        return
    
    # Umbral para considerar elementos como similares/parte del mismo grupo
    umbral_similitud = (max(arr) - min(arr)) * 0.05  # 5% del rango
    
    elementos_desplazados_en_ciclo = True
    while elementos_desplazados_en_ciclo:
        elementos_desplazados_en_ciclo = False

        # --- Pasada de Flujo Ascendente (grupos hacia la izquierda) ---
        i = 1
        while i < n:
            # Identificar un grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            
            # Buscar el final del grupo actual
            while grupo_fin + 1 < n and abs(arr[grupo_fin + 1] - arr[grupo_inicio]) <= umbral_similitud:
                grupo_fin += 1
            
            # Verificar si el grupo debe moverse hacia la izquierda
            if grupo_inicio > 0 and arr[grupo_inicio] < arr[grupo_inicio - 1]:
                # Extraer grupo
                grupo_valores = arr[grupo_inicio:grupo_fin + 1]
                grupo_valores.sort()  # Ordenar el grupo internamente
                
                # Encontrar punto de inserción para el grupo
                j = grupo_inicio - 1
                while j >= 0 and arr[j] > grupo_valores[0]:
                    j -= 1
                
                # Punto de inserción es j+1
                punto_insercion = j + 1
                
                # Mover elementos entre punto_insercion y grupo_inicio
                elementos_a_desplazar = arr[punto_insercion:grupo_inicio]
                
                # Reorganizar el arreglo
                # 1. Colocar grupo ordenado
                for idx, val in enumerate(grupo_valores):
                    arr[punto_insercion + idx] = val
                
                # 2. Colocar elementos desplazados
                for idx, val in enumerate(elementos_a_desplazar):
                    arr[punto_insercion + len(grupo_valores) + idx] = val
                
                elementos_desplazados_en_ciclo = True
            
            # Avanzar al siguiente índice después del grupo actual
            i = grupo_fin + 1
        
        # --- Pasada de Flujo Descendente (grupos hacia la derecha) ---
        i = n - 2
        while i >= 0:
            # Identificar un grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            
            # Buscar el inicio del grupo actual
            while grupo_inicio > 0 and abs(arr[grupo_inicio - 1] - arr[grupo_fin]) <= umbral_similitud:
                grupo_inicio -= 1
                
            # Verificar si el grupo debe moverse hacia la derecha
            if grupo_fin + 1 < n and arr[grupo_fin] > arr[grupo_fin + 1]:
                # Extraer grupo
                grupo_valores = arr[grupo_inicio:grupo_fin + 1]
                grupo_valores.sort()  # Ordenar el grupo internamente
                
                # Encontrar punto final para el grupo
                j = grupo_fin + 1
                while j < n and arr[j] < grupo_valores[-1]:
                    j += 1
                
                # Mover elementos entre grupo_fin+1 y j
                elementos_a_desplazar = arr[grupo_fin + 1:j]
                
                # Reorganizar el arreglo
                # 1. Colocar elementos desplazados primero
                for idx, val in enumerate(elementos_a_desplazar):
                    arr[grupo_inicio + idx] = val
                
                # 2. Colocar grupo ordenado
                for idx, val in enumerate(grupo_valores):
                    arr[grupo_inicio + len(elementos_a_desplazar) + idx] = val
                
                elementos_desplazados_en_ciclo = True
                
            # Retroceder al siguiente índice antes del grupo actual
            i = grupo_inicio - 1

def measure_sorting_time(algorithm, array):
    """Mide el tiempo que tarda en ordenarse un array"""
    array_copy = array.copy()  # Trabajar con una copia para no modificar el original
    start_time = time.time()
    algorithm(array_copy)
    end_time = time.time()
    return end_time - start_time, array_copy

def run_comparison_benchmark():
    """Ejecuta benchmarks comparando la versión original con la optimizada"""
    sizes = [100, 500, 1000, 5000, 10000]
    distributions = {
        "Random": lambda n: random.sample(range(1, n*10), n),
        "Sorted": lambda n: list(range(1, n+1)),
        "Reversed": lambda n: list(range(n, 0, -1)),
        "Clustered": lambda n: [random.randint(1, 10) for _ in range(n//3)] + 
                          [random.randint(40, 50) for _ in range(n//3)] +
                          [random.randint(90, 100) for _ in range(n - 2*(n//3))]
    }
    
    print("-" * 100)
    print("GeoFlux Sort: Comparación de rendimiento entre versión original y optimizada")
    print("-" * 100)
    print("| {:^10} | {:^15} | {:^25} | {:^25} | {:^12} |".format(
        "Tamaño", "Distribución", "Original (segundos)", "Optimizada (segundos)", "Mejora (%)"
    ))
    print("-" * 100)
    
    for size in sizes:
        for dist_name, dist_func in distributions.items():
            # Generar datos
            data = dist_func(size)
            
            # Medir tiempos de la versión original
            original_time, _ = measure_sorting_time(geoflux_sort_original, data)
            
            # Medir tiempos de la versión optimizada
            optimized_time, _ = measure_sorting_time(geoflux_sort, data)
            
            # Calcular mejora porcentual
            if original_time > 0:
                improvement = ((original_time - optimized_time) / original_time) * 100
            else:
                improvement = 0
            
            print("| {:^10} | {:^15} | {:^25.6f} | {:^25.6f} | {:^+12.2f} |".format(
                size, dist_name, original_time, optimized_time, improvement
            ))
    
    print("-" * 100)

if __name__ == "__main__":
    print("Ejecutando benchmark comparativo...")
    run_comparison_benchmark()