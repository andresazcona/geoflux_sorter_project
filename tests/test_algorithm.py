# geoflux_sorter_project/tests/test_algorithm.py
import unittest
import random
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from geoflux_sorter.algorithm import geoflux_sort # O from geoflux_sorter import geoflux_sort

class TestGeoFluxSort(unittest.TestCase):

    def assertListSorted(self, original_list, sorted_list):
        # Comprueba si la lista está ordenada comparándola con la versión ordenada por Python
        expected_sorted = sorted(original_list)
        self.assertEqual(sorted_list, expected_sorted, 
                         f"Fallo al ordenar: {original_list}. Esperado: {expected_sorted}, Obtenido: {sorted_list}")

    def test_empty_list(self):
        arr = []
        original_copy = list(arr)
        geoflux_sort(arr)
        self.assertListSorted(original_copy, arr)

    def test_single_element_list(self):
        arr = [42]
        original_copy = list(arr)
        geoflux_sort(arr)
        self.assertListSorted(original_copy, arr)

    def test_already_sorted_list(self):
        arr = [1, 2, 3, 4, 5, 6]
        original_copy = list(arr)
        geoflux_sort(arr)
        self.assertListSorted(original_copy, arr)

    def test_reverse_sorted_list(self):
        arr = [6, 5, 4, 3, 2, 1]
        original_copy = list(arr)
        geoflux_sort(arr)
        self.assertListSorted(original_copy, arr)

    def test_random_list(self):
        arr = random.sample(range(-50, 51), 20)
        original_copy = list(arr)
        geoflux_sort(arr)
        self.assertListSorted(original_copy, arr)

    def test_list_with_duplicates(self):
        arr = [5, 2, 8, 2, 5, 5, 1, 8, 0, -3, -3]
        original_copy = list(arr)
        geoflux_sort(arr)
        self.assertListSorted(original_copy, arr)

    def test_list_with_negative_numbers(self):
        arr = [-5, -2, -8, -1, -10]
        original_copy = list(arr)
        geoflux_sort(arr)
        self.assertListSorted(original_copy, arr)
    
    def test_mixed_positive_and_negative(self):
        arr = [3, -1, 4, -1, 5, -9, 2, -6]
        original_copy = list(arr)
        geoflux_sort(arr)
        self.assertListSorted(original_copy, arr)

if __name__ == '__main__':
    unittest.main()