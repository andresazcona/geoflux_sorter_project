"""
Ejemplo de uso básico del algoritmo GeoFlux Sort.

Este script demuestra el funcionamiento del algoritmo con varios
casos de prueba comunes:
    - Lista aleatoria
    - Lista ya ordenada
    - Lista en orden inverso
    - Lista vacía
    - Lista con un solo elemento
    - Lista con valores duplicados

Ejecutar:
    python examples/run_sort_example.py
"""

import random
import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
# Esto permite importar el paquete geoflux_sorter
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from geoflux_sorter import geoflux_sort


def print_test_case(description, original_list):
    """
    Ejecuta un caso de prueba y muestra los resultados.
    
    Args:
        description (str): Descripción del caso de prueba
        original_list (list): Lista a ordenar
    """
    print(f"\n{description}")
    print(f"Original:  {original_list}")
    
    # Ordenar la lista (in-place)
    geoflux_sort(original_list)
    
    print(f"Ordenada:  {original_list}")


if __name__ == "__main__":
    print("=" * 70)
    print("DEMOSTRACION DEL ALGORITMO GEOFLUX SORT")
    print("=" * 70)
    
    # Caso 1: Lista aleatoria
    lista_aleatoria = random.sample(range(1, 101), 15)
    print_test_case("Caso 1: Lista aleatoria", lista_aleatoria)

    # Caso 2: Lista ya ordenada
    lista_ordenada = list(range(1, 11))
    print_test_case("Caso 2: Lista ya ordenada", lista_ordenada)

    # Caso 3: Lista en orden inverso
    lista_inversa = list(range(10, 0, -1))
    print_test_case("Caso 3: Lista en orden inverso", lista_inversa)

    # Caso 4: Lista vacía
    lista_vacia = []
    print_test_case("Caso 4: Lista vacia", lista_vacia)

    # Caso 5: Lista de un solo elemento
    lista_unica = [42]
    print_test_case("Caso 5: Lista de un solo elemento", lista_unica)

    # Caso 6: Lista con duplicados
    lista_duplicados = [5, 2, 8, 2, 5, 5, 1, 8]
    print_test_case("Caso 6: Lista con duplicados", lista_duplicados)
    
    print("\n" + "=" * 70)
    print("TODOS LOS CASOS DE PRUEBA COMPLETADOS")
    print("=" * 70)
