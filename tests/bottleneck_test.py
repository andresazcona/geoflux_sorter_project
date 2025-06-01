import random
import time
import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from geoflux_sorter import geoflux_sort

class ProfTimer:
    """Utilidad simple para medir el tiempo de ejecución de secciones de código"""
    def __init__(self):
        self.start_time = None
        self.sections = {}
        
    def start(self):
        self.start_time = time.time()
        
    def mark(self, section_name):
        if self.start_time is not None:
            elapsed = time.time() - self.start_time
            self.sections[section_name] = elapsed
            self.start_time = time.time()
            
    def report(self):
        print("\n--- PROFILING REPORT ---")
        total_time = sum(self.sections.values())
        print(f"Total time: {total_time:.6f} seconds")
        
        print("\nBreakdown by section:")
        for section, time_taken in sorted(self.sections.items(), key=lambda x: x[1], reverse=True):
            percentage = (time_taken / total_time) * 100 if total_time > 0 else 0
            print(f"{section}: {time_taken:.6f} seconds ({percentage:.2f}%)")

def instrumented_geoflux_sort(arr, report=True):
    """
    Versión instrumentada del algoritmo GeoFlux Sort
    para identificar cuellos de botella.
    """
    timer = ProfTimer()
    n = len(arr)
    
    timer.start()
    # Caso base
    if n <= 1:
        timer.mark("Verificación casos base")
        if report:
            timer.report()
        return
    
    timer.start()
    # Detección rápida de arrays ya ordenados
    is_sorted = True
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            is_sorted = False
            break
    
    if is_sorted:
        timer.mark("Detección de array ordenado")
        if report:
            timer.report()
        return
    
    timer.start()
    # Para arreglos pequeños, usar insertion sort directamente
    if n <= 20:
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        timer.mark("Insertion sort para arrays pequeños")
        if report:
            timer.report()
        return
    
    timer.start()
    # Umbral para considerar elementos como similares
    rango = max(arr) - min(arr)
    umbral_similitud = rango * 0.05  # 5% del rango
    timer.mark("Cálculo de umbral de similitud")
    
    elementos_desplazados_en_ciclo = True
    ciclos = 0
    
    while elementos_desplazados_en_ciclo:
        ciclos += 1
        timer.start()
        elementos_desplazados_en_ciclo = False
        
        # Detección de secciones ya ordenadas
        seccion_ordenada_inicio = 0
        while seccion_ordenada_inicio + 1 < n and arr[seccion_ordenada_inicio] <= arr[seccion_ordenada_inicio + 1]:
            seccion_ordenada_inicio += 1
            
        seccion_ordenada_fin = n - 1
        while seccion_ordenada_fin > 0 and arr[seccion_ordenada_fin - 1] <= arr[seccion_ordenada_fin]:
            seccion_ordenada_fin -= 1
        
        timer.mark(f"Ciclo {ciclos} - Detección de secciones ordenadas")
            
        # Si todo está ordenado, terminar
        if seccion_ordenada_inicio >= seccion_ordenada_fin:
            if report:
                timer.report()
            return

        # --- Pasada de Flujo Ascendente (grupos hacia la izquierda) ---
        i = max(1, seccion_ordenada_inicio + 1)
        grupos_identificados = 0
        grupos_movidos = 0
        
        timer.start()
        while i < seccion_ordenada_fin + 1:
            timer.start()
            # Identificar un grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            valor_referencia = arr[i]
            
            # Buscar el final del grupo actual con límite
            j = i + 1
            max_grupo_size = min(50, n - i)
            while j < i + max_grupo_size and j < n and abs(arr[j] - valor_referencia) <= umbral_similitud:
                grupo_fin = j
                j += 1
            
            grupos_identificados += 1
            timer.mark(f"Ciclo {ciclos} - Ascendente - Identificación de grupo {grupos_identificados}")
            
            # Verificar si el grupo debe moverse hacia la izquierda
            if grupo_inicio > 0 and arr[grupo_inicio] < arr[grupo_inicio - 1]:
                timer.start()
                # Extraer grupo
                grupo_valores = sorted(arr[grupo_inicio:grupo_fin + 1])
                timer.mark(f"Ciclo {ciclos} - Ascendente - Ordenamiento de grupo {grupos_identificados}")
                
                # Encontrar punto de inserción para el grupo
                min_valor = grupo_valores[0]
                j = grupo_inicio - 1
                while j >= 0 and arr[j] > min_valor:
                    j -= 1
                
                punto_insercion = j + 1
                timer.mark(f"Ciclo {ciclos} - Ascendente - Búsqueda de punto de inserción grupo {grupos_identificados}")
                
                # Reorganizar el arreglo
                timer.start()
                elementos_a_desplazar = arr[punto_insercion:grupo_inicio]
                nuevo_segmento = grupo_valores + elementos_a_desplazar
                
                for idx, val in enumerate(nuevo_segmento):
                    arr[punto_insercion + idx] = val
                    
                timer.mark(f"Ciclo {ciclos} - Ascendente - Reordenamiento grupo {grupos_identificados}")
                
                elementos_desplazados_en_ciclo = True
                grupos_movidos += 1
            
            # Avanzar al siguiente índice después del grupo actual
            i = grupo_fin + 1
        
        timer.mark(f"Ciclo {ciclos} - Pasada Ascendente completa ({grupos_identificados} grupos, {grupos_movidos} movidos)")
        
        # --- Pasada de Flujo Descendente (grupos hacia la derecha) ---
        timer.start()
        i = min(n - 2, seccion_ordenada_fin - 1)
        grupos_identificados = 0
        grupos_movidos = 0
        
        while i >= seccion_ordenada_inicio:
            timer.start()
            # Identificar un grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            valor_referencia = arr[i]
            
            # Buscar el inicio del grupo actual con límite
            j = i - 1
            max_grupo_size = min(50, i + 1)
            while j >= i - max_grupo_size and j >= 0 and abs(arr[j] - valor_referencia) <= umbral_similitud:
                grupo_inicio = j
                j -= 1
                
            grupos_identificados += 1
            timer.mark(f"Ciclo {ciclos} - Descendente - Identificación de grupo {grupos_identificados}")
            
            # Verificar si el grupo debe moverse hacia la derecha
            if grupo_fin + 1 < n and arr[grupo_fin] > arr[grupo_fin + 1]:
                timer.start()
                # Extraer grupo
                grupo_valores = sorted(arr[grupo_inicio:grupo_fin + 1])
                timer.mark(f"Ciclo {ciclos} - Descendente - Ordenamiento de grupo {grupos_identificados}")
                
                # Encontrar punto final para el grupo
                max_valor = grupo_valores[-1]
                j = grupo_fin + 1
                while j < n and arr[j] < max_valor:
                    j += 1
                
                timer.mark(f"Ciclo {ciclos} - Descendente - Búsqueda de punto de inserción grupo {grupos_identificados}")
                
                # Reorganizar el arreglo
                timer.start()
                elementos_a_desplazar = arr[grupo_fin + 1:j]
                nuevo_segmento = elementos_a_desplazar + grupo_valores
                
                for idx, val in enumerate(nuevo_segmento):
                    arr[grupo_inicio + idx] = val
                    
                timer.mark(f"Ciclo {ciclos} - Descendente - Reordenamiento grupo {grupos_identificados}")
                
                elementos_desplazados_en_ciclo = True
                grupos_movidos += 1
                
            # Retroceder al siguiente índice antes del grupo actual
            i = grupo_inicio - 1
            
        timer.mark(f"Ciclo {ciclos} - Pasada Descendente completa ({grupos_identificados} grupos, {grupos_movidos} movidos)")
    
    if report:
        timer.report()

def run_bottleneck_tests():
    sizes = [50, 100, 500, 1000]
    distributions = {
        "Random": lambda n: random.sample(range(1, n*10), n),
        "Almost Sorted": lambda n: sorted(random.sample(range(1, n*10), n)) + [random.randint(1, n*10) for _ in range(n//10)],
        "Reversed": lambda n: list(range(n, 0, -1)),
        "Clustered": lambda n: [random.randint(1, 10) for _ in range(n//3)] + 
                          [random.randint(40, 50) for _ in range(n//3)] +
                          [random.randint(90, 100) for _ in range(n - 2*(n//3))]
    }
    
    print("=== BOTTLENECK TESTING ===")
    print("Testing different sizes and distributions...")
    
    for size in sizes:
        print(f"\n--- Testing with size: {size} ---")
        for dist_name, dist_func in distributions.items():
            print(f"\nDistribution: {dist_name}")
            test_data = dist_func(size)
            print(f"Sample data (first 10): {test_data[:10]}...")
            
            # Ejecutar versión instrumentada
            test_copy = test_data.copy()
            instrumented_geoflux_sort(test_copy)
            
            # Verificar si está correctamente ordenado
            is_sorted = all(test_copy[i] <= test_copy[i+1] for i in range(len(test_copy)-1))
            print(f"Correctamente ordenado: {'Sí' if is_sorted else 'No'}")

if __name__ == "__main__":
    print("==== GeoFlux Sort Optimizado - Prueba de Cuello de Botella ====")
    print("Identificando secciones lentas del algoritmo para futuras optimizaciones...")
    run_bottleneck_tests()