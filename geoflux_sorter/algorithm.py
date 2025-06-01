def geoflux_sort(arr):
    """
    Ordena un arreglo en su lugar utilizando el algoritmo GeoFlux Sort
    con enfoque en grupos de elementos similares.
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

def geoflux_sort_generator(arr_original):
    """
    Generador para el algoritmo GeoFlux Sort con enfoque de grupos,
    cediendo el estado del arreglo y la información de operaciones.
    """
    arr = list(arr_original)
    n = len(arr)
    
    if n <= 1:
        yield {'array': list(arr), 'pass_type': 'Finalizado', 'status': 'Arreglo muy pequeño, ya ordenado',
               'highlights': {'all_sorted': True}}
        return
    
    # Umbral para considerar elementos como similares/parte del mismo grupo
    umbral_similitud = 5
    
    max_iterations = n * n + n + 5  # Límite por seguridad
    current_iterations = 0
    
    elementos_desplazados_en_ciclo = True
    while elementos_desplazados_en_ciclo:
        current_iterations += 1
        if current_iterations > max_iterations:
            yield {'array': list(arr), 'pass_type': 'Detenido', 
                   'status': 'Parada por seguridad (max_iterations)', 
                   'highlights': {}}
            return
        
        elementos_desplazados_en_ciclo = False
        
        # --- Pasada de Flujo Ascendente (grupos hacia la izquierda) ---
        yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 
               'status': 'Iniciando Pasada Ascendente de Grupos', 
               'highlights': {}}
        
        i = 1
        while i < n:
            # Identificar un grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            
            # Buscar el final del grupo actual
            while grupo_fin + 1 < n and abs(arr[grupo_fin + 1] - arr[grupo_inicio]) <= umbral_similitud:
                grupo_fin += 1
            
            # Visualización: Identificando grupo
            grupo_highlights = {idx: 'grupo' for idx in range(grupo_inicio, grupo_fin + 1)}
            yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 
                   'status': f'Identificando grupo desde A[{grupo_inicio}] hasta A[{grupo_fin}]',
                   'highlights': grupo_highlights}
            
            grupo_tamaño = grupo_fin - grupo_inicio + 1
            
            # Verificar si el grupo debe moverse hacia la izquierda
            if grupo_inicio > 0 and arr[grupo_inicio] < arr[grupo_inicio - 1]:
                # Extraer grupo
                grupo_valores = arr[grupo_inicio:grupo_fin + 1]
                grupo_valores_original = list(grupo_valores)
                grupo_valores.sort()  # Ordenar el grupo internamente
                
                yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 
                       'status': f'Extrayendo grupo {grupo_valores_original} para ordenamiento',
                       'highlights': grupo_highlights}
                
                # Encontrar punto de inserción para el grupo
                j = grupo_inicio - 1
                while j >= 0 and arr[j] > grupo_valores[0]:
                    yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 
                           'status': f'Comparando A[{j}]={arr[j]} con valor mínimo del grupo {grupo_valores[0]}',
                           'highlights': {**grupo_highlights, 'j': j}}
                    j -= 1
                
                # Punto de inserción es j+1
                punto_insercion = j + 1
                
                yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 
                       'status': f'Punto de inserción para el grupo: {punto_insercion}',
                       'highlights': {**grupo_highlights, 'insertion_at': punto_insercion}}
                
                # Mover elementos entre punto_insercion y grupo_inicio
                elementos_a_desplazar = arr[punto_insercion:grupo_inicio]
                
                # Hacer una copia del arreglo antes de modificarlo
                arr_antes = list(arr)
                
                # Reorganizar el arreglo
                # 1. Colocar grupo ordenado
                for idx, val in enumerate(grupo_valores):
                    arr[punto_insercion + idx] = val
                
                # 2. Colocar elementos desplazados
                for idx, val in enumerate(elementos_a_desplazar):
                    arr[punto_insercion + len(grupo_valores) + idx] = val
                
                # Visualizar el movimiento del grupo
                yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 
                       'status': 'Grupo movido a nueva posición y ordenado internamente',
                       'highlights': {idx: 'moved_group' for idx in range(punto_insercion, punto_insercion + len(grupo_valores))}}
                
                elementos_desplazados_en_ciclo = True
            
            # Avanzar al siguiente índice después del grupo actual
            i = grupo_fin + 1
        
        # --- Pasada de Flujo Descendente (grupos hacia la derecha) ---
        yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 
               'status': 'Iniciando Pasada Descendente de Grupos', 
               'highlights': {}}
        
        i = n - 2
        while i >= 0:
            # Identificar un grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            
            # Buscar el inicio del grupo actual
            while grupo_inicio > 0 and abs(arr[grupo_inicio - 1] - arr[grupo_fin]) <= umbral_similitud:
                grupo_inicio -= 1
                
            # Visualización: Identificando grupo
            grupo_highlights = {idx: 'grupo' for idx in range(grupo_inicio, grupo_fin + 1)}
            yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 
                   'status': f'Identificando grupo desde A[{grupo_inicio}] hasta A[{grupo_fin}]',
                   'highlights': grupo_highlights}
            
            # Verificar si el grupo debe moverse hacia la derecha
            if grupo_fin + 1 < n and arr[grupo_fin] > arr[grupo_fin + 1]:
                # Extraer grupo
                grupo_valores = arr[grupo_inicio:grupo_fin + 1]
                grupo_valores_original = list(grupo_valores)
                grupo_valores.sort()  # Ordenar el grupo internamente
                
                yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 
                       'status': f'Extrayendo grupo {grupo_valores_original} para ordenamiento',
                       'highlights': grupo_highlights}
                
                # Encontrar punto final para el grupo
                j = grupo_fin + 1
                while j < n and arr[j] < grupo_valores[-1]:
                    yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 
                           'status': f'Comparando A[{j}]={arr[j]} con valor máximo del grupo {grupo_valores[-1]}',
                           'highlights': {**grupo_highlights, 'j': j}}
                    j += 1
                
                yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 
                       'status': f'Punto final para el grupo: {j}',
                       'highlights': {**grupo_highlights}}
                
                # Mover elementos entre grupo_fin+1 y j
                elementos_a_desplazar = arr[grupo_fin + 1:j]
                
                # Hacer una copia del arreglo antes de modificarlo
                arr_antes = list(arr)
                
                # Reorganizar el arreglo
                # 1. Colocar elementos desplazados primero
                for idx, val in enumerate(elementos_a_desplazar):
                    arr[grupo_inicio + idx] = val
                
                # 2. Colocar grupo ordenado
                for idx, val in enumerate(grupo_valores):
                    arr[grupo_inicio + len(elementos_a_desplazar) + idx] = val
                
                # Visualizar el movimiento del grupo
                yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 
                       'status': 'Grupo movido a nueva posición y ordenado internamente',
                       'highlights': {idx: 'moved_group' for idx in range(grupo_inicio + len(elementos_a_desplazar), 
                                                                          grupo_inicio + len(elementos_a_desplazar) + len(grupo_valores))}}
                
                elementos_desplazados_en_ciclo = True
                
            # Retroceder al siguiente índice antes del grupo actual
            i = grupo_inicio - 1
    
    # Arreglo completamente ordenado
    yield {'array': list(arr), 'pass_type': 'Finalizado', 
           'status': '¡Arreglo Ordenado!', 
           'highlights': {'all_sorted': True}}