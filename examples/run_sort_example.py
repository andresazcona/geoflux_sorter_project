# geoflux_sorter_project/examples/run_sort_example.py
import random
import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH para encontrar el paquete geoflux_sorter
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from geoflux_sorter import geoflux_sort

if __name__ == "__main__":
    # Prueba con una lista aleatoria
    my_list_random = random.sample(range(1, 101), 15)
    print(f"Lista aleatoria original: {my_list_random}")
    geoflux_sort(my_list_random)
    print(f"Lista aleatoria ordenada: {my_list_random}\n")

    # Prueba con una lista ya ordenada
    my_list_sorted = list(range(1, 11))
    print(f"Lista ya ordenada original: {my_list_sorted}")
    geoflux_sort(my_list_sorted)
    print(f"Lista ya ordenada (después de ordenar): {my_list_sorted}\n")

    # Prueba con una lista en orden inverso
    my_list_reversed = list(range(10, 0, -1))
    print(f"Lista inversa original: {my_list_reversed}")
    geoflux_sort(my_list_reversed)
    print(f"Lista inversa ordenada: {my_list_reversed}\n")

    # Prueba con una lista vacía
    my_list_empty = []
    print(f"Lista vacía original: {my_list_empty}")
    geoflux_sort(my_list_empty)
    print(f"Lista vacía ordenada: {my_list_empty}\n")

    # Prueba con una lista de un solo elemento
    my_list_single = [42]
    print(f"Lista de un solo elemento original: {my_list_single}")
    geoflux_sort(my_list_single)
    print(f"Lista de un solo elemento ordenada: {my_list_single}\n")

    # Prueba con duplicados
    my_list_duplicates = [5, 2, 8, 2, 5, 5, 1, 8]
    print(f"Lista con duplicados original: {my_list_duplicates}")
    geoflux_sort(my_list_duplicates)
    print(f"Lista con duplicados ordenada: {my_list_duplicates}\n")