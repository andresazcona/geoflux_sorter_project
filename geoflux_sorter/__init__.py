# geoflux_sorter_project/geoflux_sorter/__init__.py
from .algorithm import geoflux_sort, geoflux_sort_generator
from .animator import create_geoflux_animation

__all__ = [
    'geoflux_sort', 
    'geoflux_sort_generator', 
    'create_geoflux_animation'
]
__version__ = '1.0.0'  # Actualizado a la versión 1.0.0