def geoflux_sort(arr):
    """
    Ordena un arreglo en su lugar utilizando el algoritmo GeoFlux Sort.
    """
    n = len(arr)
    if n <= 1:
        return

    elementos_desplazados_en_ciclo = True
    while elementos_desplazados_en_ciclo:
        elementos_desplazados_en_ciclo = False

        # --- Pasada de Flujo Ascendente (Pequeños a la izquierda) ---
        for i in range(1, n):
            elemento_clave = arr[i]
            if elemento_clave < arr[i-1]: 
                j = i - 1
                while j >= 0 and arr[j] > elemento_clave:
                    arr[j+1] = arr[j]
                    j -= 1
                arr[j+1] = elemento_clave 
                elementos_desplazados_en_ciclo = True
        
        # --- Pasada de Flujo Descendente (Grandes a la derecha) ---
        for i in range(n - 2, -1, -1): 
            elemento_clave = arr[i]
            if i + 1 < n and elemento_clave > arr[i+1]:  # Asegurar que i+1 es un índice válido
                j = i + 1
                while j < n and arr[j] < elemento_clave:
                    arr[j-1] = arr[j]
                    j += 1
                arr[j-1] = elemento_clave 
                elementos_desplazados_en_ciclo = True
        
def geoflux_sort_generator(arr_original):
    """
    Generador para el algoritmo GeoFlux Sort, cediendo el estado
    del arreglo y la información de la operación actual en cada paso,
    ideal para visualizaciones.
    """
    arr = list(arr_original) 
    n = len(arr)
    elementos_desplazados_en_ciclo = True
    
    max_iterations = n * n * 2 + n + 5 # Límite generoso para todas las pasadas y yields iniciales/finales
    current_iterations = 0

    while elementos_desplazados_en_ciclo:
        current_iterations += 1
        if current_iterations > max_iterations:
            yield {'array': list(arr), 'pass_type': 'Detenido', 'i': -1, 'j': -1, 
                   'key_val': None, 'key_original_idx': -1, 'status': 'Parada por seguridad (max_iterations)', 
                   'highlights': {}}
            return 
            
        elementos_desplazados_en_ciclo = False
        
        # --- Pasada de Flujo Ascendente ---
        yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 'i': -1, 'j': -1, 
               'key_val': None, 'key_original_idx': -1, 'status': 'Iniciando Pasada Ascendente', 
               'highlights': {}}

        for i in range(1, n):
            current_iterations += 1 # Contar sub-pasos
            yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 'i': i, 'j': -1, 
                   'key_val': None, 'key_original_idx': -1, 'status': f'Considerando A[{i}]={arr[i]}', 
                   'highlights': {'i': i}}
            
            elemento_clave = arr[i]
            key_original_idx = i 

            if elemento_clave < arr[i-1]: 
                yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 'i': i, 'j': -1, 
                       'key_val': elemento_clave, 'key_original_idx': key_original_idx, 
                       'status': f'Extrayendo {elemento_clave} de A[{i}]', 
                       'highlights': {'i': i, 'key_floating': key_original_idx}}

                j = i - 1
                while j >= 0 and arr[j] > elemento_clave:
                    current_iterations += 1
                    yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 'i': i, 'j': j, 
                           'key_val': elemento_clave, 'key_original_idx': key_original_idx, 
                           'status': f'Comparando A[{j}]={arr[j]} con {elemento_clave}', 
                           'highlights': {'i': i, 'j': j, 'key_floating': key_original_idx}}
                    
                    arr[j+1] = arr[j]
                    elementos_desplazados_en_ciclo = True
                    yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 'i': i, 'j': j, 
                           'key_val': elemento_clave, 'key_original_idx': key_original_idx, 
                           'status': f'Desplazando A[{j}]={arr[j+1]} a A[{j+1}]', 
                           'highlights': {'i': i, 'j': j, 'shifting_to': j+1, 'shifting_from': j, 'key_floating': key_original_idx}}
                    j -= 1
                
                arr[j+1] = elemento_clave
                current_iterations += 1
                yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 'i': i, 'j': j+1, 
                       'key_val': elemento_clave, 'key_original_idx': -1, 
                       'status': f'Insertando {elemento_clave} en A[{j+1}]', 
                       'highlights': {'i': i, 'insertion_at': j+1}}
        
        # --- Pasada de Flujo Descendente ---
        yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 'i': n, 'j': -1, 
               'key_val': None, 'key_original_idx': -1, 'status': 'Iniciando Pasada Descendente', 
               'highlights': {}}

        for i in range(n - 2, -1, -1):
            current_iterations += 1
            yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 'i': i, 'j': -1, 
                   'key_val': None, 'key_original_idx': -1, 'status': f'Considerando A[{i}]={arr[i]}', 
                   'highlights': {'i': i}}

            elemento_clave = arr[i]
            key_original_idx = i

            if i + 1 < n and elemento_clave > arr[i+1]: 
                yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 'i': i, 'j': -1, 
                       'key_val': elemento_clave, 'key_original_idx': key_original_idx, 
                       'status': f'Extrayendo {elemento_clave} de A[{i}]', 
                       'highlights': {'i': i, 'key_floating': key_original_idx}}
                
                j = i + 1
                while j < n and arr[j] < elemento_clave:
                    current_iterations += 1
                    yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 'i': i, 'j': j, 
                           'key_val': elemento_clave, 'key_original_idx': key_original_idx, 
                           'status': f'Comparando A[{j}]={arr[j]} con {elemento_clave}', 
                           'highlights': {'i': i, 'j': j, 'key_floating': key_original_idx}}
                    
                    arr[j-1] = arr[j]
                    elementos_desplazados_en_ciclo = True
                    yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 'i': i, 'j': j, 
                           'key_val': elemento_clave, 'key_original_idx': key_original_idx, 
                           'status': f'Desplazando A[{j}]={arr[j-1]} a A[{j-1}]', 
                           'highlights': {'i': i, 'j': j, 'shifting_to': j-1, 'shifting_from': j, 'key_floating': key_original_idx}}
                    j += 1
                
                arr[j-1] = elemento_clave
                current_iterations += 1
                yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 'i': i, 'j': j-1, 
                       'key_val': elemento_clave, 'key_original_idx': -1, 
                       'status': f'Insertando {elemento_clave} en A[{j-1}]', 
                       'highlights': {'i': i, 'insertion_at': j-1}}

        if not elementos_desplazados_en_ciclo:
            break 
    
    current_iterations += 1
    yield {'array': list(arr), 'pass_type': 'Finalizado', 'i': -1, 'j': -1, 
           'key_val': None, 'key_original_idx': -1, 'status': '¡Arreglo Ordenado!', 
           'highlights': {'all_sorted': True}}