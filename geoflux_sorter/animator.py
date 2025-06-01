import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .algorithm import geoflux_sort_generator  # Relative import

# Diccionario de colores para los resaltados - Ampliado para grupos
COLOR_MAP = {
    'default': 'skyblue',
    'i': 'cornflowerblue',        # Puntero principal i
    'j': 'sandybrown',            # Puntero secundario j (comparación)
    'key_floating': 'hotpink',    # Elemento clave "extraído" o "flotando"
    'shifting': 'lightcoral',     # Elemento que se está desplazando para hacer espacio
    'insertion_at': 'mediumpurple', # Elemento recién insertado
    'all_sorted': 'lightgreen',   # El Arreglo esta ordenado
    'grupo': 'gold',              # Grupo identificado
    'moved_group': 'limegreen'    # Grupo que se ha movido
}

# Función que se llamará para cada frame de la animación
def update_plot(frame_data, rects, status_text_obj, details_text_obj, fig, ax, n_elements, max_val):
    if frame_data is None:  # Generator might be exhausted
        return tuple(rects) + (status_text_obj, details_text_obj)

    info = frame_data 
    arr_state = info.get('array', [])  # Get array or empty list if not present

    # Ensure arr_state has the correct length for rects
    if len(arr_state) != n_elements:
        # Fallback: draw current rect heights if arr_state is short, or default if too long
        current_heights = [r.get_height() for r in rects]
        for i, rect in enumerate(rects):
            if i < len(arr_state):
                rect.set_height(arr_state[i])
            else:  # if arr_state is shorter than rects
                rect.set_height(current_heights[i] if i < len(current_heights) else 0)
    else:  # Normal case
        for rect, val in zip(rects, arr_state):
            rect.set_height(val)
    
    status_text_obj.set_text(info.get('status', 'Actualizando...'))
    
    # Adaptar visualización de detalles para grupos
    pass_info = f"Pasada: {info.get('pass_type', '')}"
    details_text_obj.set_text(pass_info)

    # Aplicar los colores según los highlights, incluyendo grupos
    highlights = info.get('highlights', {})
    for idx, rect in enumerate(rects):
        color = COLOR_MAP['default']
        
        if highlights.get('all_sorted'):
            color = COLOR_MAP['all_sorted']
        elif idx in highlights:
            # Si el índice está en highlights, usar el color correspondiente
            highlight_type = highlights[idx]
            if isinstance(highlight_type, str) and highlight_type in COLOR_MAP:
                color = COLOR_MAP[highlight_type]
            elif highlight_type == 'i':
                color = COLOR_MAP['i']
            elif highlight_type == 'j':
                color = COLOR_MAP['j']
        elif idx == highlights.get('insertion_at'):
            color = COLOR_MAP['insertion_at']
        elif idx == highlights.get('key_floating'):
            color = COLOR_MAP['key_floating']
        elif idx == highlights.get('shifting_to') or idx == highlights.get('shifting_from'):
            color = COLOR_MAP['shifting']
        elif idx == highlights.get('i') and highlights.get('i') < n_elements:  # Check index validity
            color = COLOR_MAP['i']
        elif idx == highlights.get('j') and highlights.get('j') < n_elements:  # Check index validity
            color = COLOR_MAP['j']
            
        rect.set_color(color)
        
    return tuple(rects) + (status_text_obj, details_text_obj)


def create_geoflux_animation(initial_data, interval=300, save_to_file=None):
    """
    Crea y muestra (o guarda) una animación del GeoFlux Sort.
    """
    if not initial_data:
        print("No se proporcionaron datos para la animación.")
        return None

    n_elements = len(initial_data)
    max_val = max(initial_data) if initial_data else 10

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_title("GeoFlux Sort Animation", fontsize=16)
    ax.set_xlabel("Índice del Elemento")
    ax.set_ylabel("Valor del Elemento")

    # Usamos initial_data para las alturas iniciales de las barras
    bar_rects = ax.bar(range(n_elements), initial_data, 
                       align='edge', width=0.8, color=COLOR_MAP['default']) 
    ax.set_xticks(range(n_elements))
    ax.set_xticklabels([str(i) for i in range(n_elements)])
    ax.set_xlim(-0.5, n_elements - 0.5)
    ax.set_ylim(0, max_val * 1.1)

    status_text_obj = fig.text(0.5, 0.95, "Inicializando Animación...", ha="center", va="bottom", fontsize=12)
    details_text_obj = fig.text(0.5, 0.01, "", ha="center", va="bottom", fontsize=10)

    sorter_generator = geoflux_sort_generator(list(initial_data))  # Usar una copia

    # Calcular save_count para guardar la animación de forma fiable
    # Esto puede ser costoso para algoritmos complejos, así que usamos un valor estimado
    # basado en el tamaño de los datos
    save_count = min(1000, n_elements * n_elements + 100)

    ani = animation.FuncAnimation(fig, update_plot, frames=sorter_generator, 
                                  fargs=(bar_rects, status_text_obj, details_text_obj, fig, ax, n_elements, max_val),
                                  blit=False, interval=interval, repeat=False,
                                  save_count=save_count) 

    plt.tight_layout(rect=[0, 0.05, 1, 0.92]) 

    if save_to_file:
        try:
            ani.save(save_to_file, writer="ffmpeg", fps=max(1, int(1000 / interval)))
            print(f"Animación guardada como {save_to_file}")
        except Exception as e:
            print(f"Error al guardar la animación: {e}")
            print("Asegúrate de que ffmpeg esté instalado y en el PATH del sistema.")
            print("Mostrando animación en su lugar...")
            plt.show()
    else:
        plt.show()
    
    return ani