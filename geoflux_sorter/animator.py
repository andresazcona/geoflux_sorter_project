"""
Módulo de animación para GeoFlux Sort.

Este módulo proporciona funcionalidad para crear visualizaciones animadas
del proceso de ordenamiento de GeoFlux Sort utilizando matplotlib.
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .algorithm import geoflux_sort_generator

# Mapa de colores para diferentes estados de elementos en la visualización
COLOR_MAP = {
    'default': 'skyblue',            # Color por defecto de las barras
    'i': 'cornflowerblue',           # Índice principal actual
    'j': 'sandybrown',               # Índice de comparación
    'key_floating': 'hotpink',       # Elemento siendo movido
    'shifting': 'lightcoral',        # Elementos siendo desplazados
    'insertion_at': 'mediumpurple',  # Punto de inserción
    'all_sorted': 'lightgreen',      # Arreglo completamente ordenado
    'grupo': 'gold',                 # Grupo de elementos similares identificado
    'moved_group': 'limegreen'       # Grupo que ha sido reubicado
}


def update_plot(frame_data, rects, status_text_obj, details_text_obj, fig, ax, n_elements, max_val):
    """
    Actualiza la visualización para cada frame de la animación.
    
    Esta función es llamada por FuncAnimation para cada paso del algoritmo.
    Actualiza las alturas y colores de las barras según el estado actual.
    
    Args:
        frame_data (dict): Datos del frame actual del generador
        rects (list): Lista de objetos Rectangle de matplotlib
        status_text_obj: Objeto de texto para mostrar el estado
        details_text_obj: Objeto de texto para mostrar detalles adicionales
        fig: Figura de matplotlib
        ax: Axes de matplotlib
        n_elements (int): Número de elementos en el arreglo
        max_val (int): Valor máximo para escalar el eje Y
        
    Returns:
        tuple: Tupla de objetos modificados para blit
    """
    # Verificar si el generador se ha agotado
    if frame_data is None:
        return tuple(rects) + (status_text_obj, details_text_obj)

    info = frame_data
    arr_state = info.get('array', [])

    # Asegurar que arr_state tiene la longitud correcta
    if len(arr_state) != n_elements:
        # Fallback: mantener alturas actuales si hay discrepancia
        current_heights = [r.get_height() for r in rects]
        for i, rect in enumerate(rects):
            if i < len(arr_state):
                rect.set_height(arr_state[i])
            else:
                rect.set_height(current_heights[i] if i < len(current_heights) else 0)
    else:
        # Actualizar alturas de todas las barras
        for rect, val in zip(rects, arr_state):
            rect.set_height(val)
    
    # Actualizar textos de estado
    status_text_obj.set_text(info.get('status', 'Actualizando...'))
    pass_info = f"Pasada: {info.get('pass_type', '')}"
    details_text_obj.set_text(pass_info)

    # Aplicar colores según los highlights
    highlights = info.get('highlights', {})
    
    for idx, rect in enumerate(rects):
        # Color por defecto
        color = COLOR_MAP['default']
        
        # Verificar si todo el arreglo está ordenado
        if highlights.get('all_sorted'):
            color = COLOR_MAP['all_sorted']
        # Verificar si el índice tiene un highlight específico
        elif idx in highlights:
            highlight_type = highlights[idx]
            # Si el tipo de highlight está en el mapa de colores, usarlo
            if isinstance(highlight_type, str) and highlight_type in COLOR_MAP:
                color = COLOR_MAP[highlight_type]
            # Manejar highlights específicos
            elif highlight_type == 'i':
                color = COLOR_MAP['i']
            elif highlight_type == 'j':
                color = COLOR_MAP['j']
        # Verificar highlights especiales (punto de inserción, etc.)
        elif idx == highlights.get('insertion_at'):
            color = COLOR_MAP['insertion_at']
        elif idx == highlights.get('key_floating'):
            color = COLOR_MAP['key_floating']
        elif idx == highlights.get('shifting_to') or idx == highlights.get('shifting_from'):
            color = COLOR_MAP['shifting']
        elif idx == highlights.get('i') and highlights.get('i') < n_elements:
            color = COLOR_MAP['i']
        elif idx == highlights.get('j') and highlights.get('j') < n_elements:
            color = COLOR_MAP['j']
            
        rect.set_color(color)
        
    return tuple(rects) + (status_text_obj, details_text_obj)


def create_geoflux_animation(initial_data, interval=300, save_to_file=None):
    """
    Crea y muestra (o guarda) una animación del proceso de GeoFlux Sort.
    
    Esta función genera una visualización animada paso a paso del algoritmo
    GeoFlux Sort, mostrando cómo los grupos de elementos migran a través
    del arreglo.
    
    Args:
        initial_data (list): Lista de valores numéricos a ordenar
        interval (int, optional): Tiempo en milisegundos entre frames. 
            Menor valor = animación más rápida. Por defecto 300ms.
        save_to_file (str, optional): Ruta del archivo para guardar la animación.
            Si es None, muestra la animación en pantalla. Requiere ffmpeg
            instalado para guardar. Por defecto None.
            
    Returns:
        matplotlib.animation.FuncAnimation: Objeto de animación creado,
            o None si no hay datos.
            
    Ejemplo:
        >>> datos = [5, 2, 9, 1, 5, 6]
        >>> animacion = create_geoflux_animation(datos, interval=200)
        >>> # O para guardar:
        >>> animacion = create_geoflux_animation(datos, save_to_file="sort.mp4")
        
    Nota:
        Para guardar animaciones se requiere ffmpeg instalado en el sistema
        y accesible desde el PATH.
    """
    # Validar que hay datos para animar
    if not initial_data:
        print("No se proporcionaron datos para la animación.")
        return None

    # Configuración inicial
    n_elements = len(initial_data)
    max_val = max(initial_data) if initial_data else 10

    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_title("GeoFlux Sort Animation", fontsize=16)
    ax.set_xlabel("Indice del Elemento")
    ax.set_ylabel("Valor del Elemento")

    # Crear barras iniciales
    bar_rects = ax.bar(
        range(n_elements),
        initial_data,
        align='edge',
        width=0.8,
        color=COLOR_MAP['default']
    )
    
    # Configurar ejes
    ax.set_xticks(range(n_elements))
    ax.set_xticklabels([str(i) for i in range(n_elements)])
    ax.set_xlim(-0.5, n_elements - 0.5)
    ax.set_ylim(0, max_val * 1.1)

    # Crear objetos de texto para información de estado
    status_text_obj = fig.text(
        0.5, 0.95,
        "Inicializando Animacion...",
        ha="center",
        va="bottom",
        fontsize=12
    )
    details_text_obj = fig.text(
        0.5, 0.01,
        "",
        ha="center",
        va="bottom",
        fontsize=10
    )

    # Crear generador del algoritmo
    sorter_generator = geoflux_sort_generator(list(initial_data))

    # Calcular número estimado de frames para guardar
    # Esto evita problemas al guardar animaciones largas
    save_count = min(1000, n_elements * n_elements + 100)

    # Crear animación
    ani = animation.FuncAnimation(
        fig,
        update_plot,
        frames=sorter_generator,
        fargs=(bar_rects, status_text_obj, details_text_obj, fig, ax, n_elements, max_val),
        blit=False,
        interval=interval,
        repeat=False,
        save_count=save_count
    )

    # Ajustar layout
    plt.tight_layout(rect=[0, 0.05, 1, 0.92])

    # Guardar o mostrar la animación
    if save_to_file:
        try:
            # Intentar guardar la animación como video
            fps = max(1, int(1000 / interval))
            ani.save(save_to_file, writer="ffmpeg", fps=fps)
            print(f"Animacion guardada como {save_to_file}")
        except FileNotFoundError:
            print("Error: ffmpeg no esta instalado o no esta en el PATH")
            print("Para guardar animaciones, instala ffmpeg:")
            print("  - Windows: winget install ffmpeg")
            print("  - MacOS: brew install ffmpeg")
            print("  - Linux: sudo apt-get install ffmpeg")
            print("\nMostrando animacion en su lugar...")
            plt.show()
        except Exception as e:
            print(f"Error al guardar la animacion: {e}")
            print("Mostrando animacion en su lugar...")
            plt.show()
    else:
        # Mostrar la animación en pantalla
        plt.show()
    
    return ani
