# geoflux_sorter_project/examples/run_animation_example.py
import random
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from geoflux_sorter import create_geoflux_animation

if __name__ == "__main__":
    # Puedes cambiar 'sample_data' por la lista que quieras visualizar
    sample_data = [random.randint(0, 100) for _ in range(50)]
    # sample_data = [50, 40, 30, 20, 10] # Ejemplo inverso
    # sample_data = [10, 20, 30, 40, 50] # Ejemplo ordenado
    
    print(f"Datos para animar: {sample_data}")
    
    # Para mostrar la animación:
    animation_obj = create_geoflux_animation(sample_data, interval=10)
    
    # Para guardar la animación en un archivo (descomenta y asegúrate de tener ffmpeg):
    # animation_obj = create_geoflux_animation(sample_data, interval=200, save_to_file="geoflux_sort.mp4")
    
    # Si create_geoflux_animation ya llama a plt.show() o guarda, no necesitas hacer más aquí
    # a menos que quieras interactuar con animation_obj.