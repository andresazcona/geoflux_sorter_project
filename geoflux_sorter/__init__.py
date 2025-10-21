"""
GeoFlux Sorter - Algoritmo de ordenamiento bidireccional con migración por grupos.

Este paquete proporciona una implementación del algoritmo GeoFlux Sort,
un algoritmo de ordenamiento experimental que identifica grupos de elementos
similares y los migra como unidades hacia sus posiciones correctas.

Módulos principales:
    - algorithm: Implementación del algoritmo de ordenamiento
    - animator: Sistema de visualización y animación

Funciones exportadas:
    - geoflux_sort: Ordena un arreglo in-place
    - geoflux_sort_generator: Versión generadora para seguimiento paso a paso
    - create_geoflux_animation: Crea visualizaciones animadas del algoritmo

Ejemplo básico:
    >>> from geoflux_sorter import geoflux_sort
    >>> datos = [5, 2, 9, 1, 5, 6]
    >>> geoflux_sort(datos)
    >>> print(datos)
    [1, 2, 5, 5, 6, 9]

Ejemplo con visualización:
    >>> from geoflux_sorter import create_geoflux_animation
    >>> datos = [64, 34, 25, 12, 22, 11, 90]
    >>> animacion = create_geoflux_animation(datos, interval=200)

Autor: Andrés Azcona
Versión: 1.0.0
Licencia: MIT
"""

from .algorithm import geoflux_sort, geoflux_sort_generator
from .animator import create_geoflux_animation

__all__ = [
    'geoflux_sort',
    'geoflux_sort_generator',
    'create_geoflux_animation'
]

__version__ = '1.0.0'
__author__ = 'Andres Azcona'
__license__ = 'MIT'
