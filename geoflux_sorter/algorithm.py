def geoflux_sort(arr):
    """
    Ordena un arreglo en su lugar utilizando el algoritmo GeoFlux Sort optimizado
    con enfoque en grupos de elementos similares.
    """
    n = len(arr)
    
    # 1. Optimización: casos base (arrays pequeños o ya ordenados)
    if n <= 1:
        return
        
    # 2. Optimización: detección rápida de arrays ya ordenados
    is_sorted = True
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            is_sorted = False
            break
    if is_sorted:
        return
    
    # 3. Optimización: para arreglos pequeños, usar insertion sort directamente
    if n <= 20:
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return
    
    # 4. Optimización: umbral adaptativo para la similitud
    rango = max(arr) - min(arr)
    if rango == 0:  # Todos los elementos son iguales
        return
    
    # Calcular un umbral adaptativo basado en el rango de los datos
    umbral_similitud = rango * 0.05  # 5% del rango
    
    elementos_desplazados_en_ciclo = True
    while elementos_desplazados_en_ciclo:
        elementos_desplazados_en_ciclo = False
        
        # 5. Optimización: detección de secciones ya ordenadas
        seccion_ordenada_inicio = 0
        while seccion_ordenada_inicio + 1 < n and arr[seccion_ordenada_inicio] <= arr[seccion_ordenada_inicio + 1]:
            seccion_ordenada_inicio += 1
            
        seccion_ordenada_fin = n - 1
        while seccion_ordenada_fin > 0 and arr[seccion_ordenada_fin - 1] <= arr[seccion_ordenada_fin]:
            seccion_ordenada_fin -= 1
            
        # Si todo está ordenado, terminar
        if seccion_ordenada_inicio >= seccion_ordenada_fin:
            return

        # --- Pasada de Flujo Ascendente (grupos hacia la izquierda) ---
        i = max(1, seccion_ordenada_inicio + 1)
        while i < seccion_ordenada_fin + 1:
            # Identificar un grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            valor_referencia = arr[i]  # 6. Optimización: usar valor de referencia 
            
            # Buscar el final del grupo actual con límite para evitar recorrer todo el arreglo
            j = i + 1
            max_grupo_size = min(50, n - i)  # Limitar tamaño máximo de grupo
            while j < i + max_grupo_size and j < n and abs(arr[j] - valor_referencia) <= umbral_similitud:
                grupo_fin = j
                j += 1
            
            # Verificar si el grupo debe moverse hacia la izquierda
            if grupo_inicio > 0 and arr[grupo_inicio] < arr[grupo_inicio - 1]:
                # 7. Optimización: ordenar y extraer el grupo en una operación
                grupo_valores = sorted(arr[grupo_inicio:grupo_fin + 1])
                
                # Pre-calcular el valor mínimo para comparaciones
                min_valor = grupo_valores[0]
                
                # Encontrar punto de inserción para el grupo
                j = grupo_inicio - 1
                while j >= 0 and arr[j] > min_valor:
                    j -= 1
                
                # Punto de inserción es j+1
                punto_insercion = j + 1
                
                # Preparar los elementos a desplazar
                elementos_a_desplazar = arr[punto_insercion:grupo_inicio]
                
                # 7. Optimización: uso de slicing para operaciones en bloque
                # Crear el nuevo segmento combinado
                nuevo_segmento = grupo_valores + elementos_a_desplazar
                
                # Reemplazar el segmento completo en una sola operación
                for idx, val in enumerate(nuevo_segmento):
                    arr[punto_insercion + idx] = val
                
                elementos_desplazados_en_ciclo = True
            
            # Avanzar al siguiente índice después del grupo actual
            i = grupo_fin + 1
        
        # --- Pasada de Flujo Descendente (grupos hacia la derecha) ---
        i = min(n - 2, seccion_ordenada_fin - 1)
        while i >= seccion_ordenada_inicio:
            # Identificar un grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            valor_referencia = arr[i]  # 6. Optimización: usar valor de referencia
            
            # Buscar el inicio del grupo actual con límite
            j = i - 1
            max_grupo_size = min(50, i + 1)  # Limitar tamaño máximo de grupo
            while j >= i - max_grupo_size and j >= 0 and abs(arr[j] - valor_referencia) <= umbral_similitud:
                grupo_inicio = j
                j -= 1
                
            # Verificar si el grupo debe moverse hacia la derecha
            if grupo_fin + 1 < n and arr[grupo_fin] > arr[grupo_fin + 1]:
                # 7. Optimización: ordenar y extraer el grupo en una operación
                grupo_valores = sorted(arr[grupo_inicio:grupo_fin + 1])
                
                # Pre-calcular el valor máximo para comparaciones
                max_valor = grupo_valores[-1]
                
                # Encontrar punto final para el grupo
                j = grupo_fin + 1
                while j < n and arr[j] < max_valor:
                    j += 1
                
                # Preparar los elementos a desplazar
                elementos_a_desplazar = arr[grupo_fin + 1:j]
                
                # 7. Optimización: uso de slicing para operaciones en bloque
                # Crear el nuevo segmento combinado
                nuevo_segmento = elementos_a_desplazar + grupo_valores
                
                # Reemplazar el segmento completo en una sola operación
                for idx, val in enumerate(nuevo_segmento):
                    arr[grupo_inicio + idx] = val
                
                elementos_desplazados_en_ciclo = True
                
            # Retroceder al siguiente índice antes del grupo actual
            i = grupo_inicio - 1

def geoflux_sort_generator(arr_original):
    """
    Generador para el algoritmo GeoFlux Sort con enfoque de grupos,
    cediendo el estado del arreglo y la información de operaciones.
    Incluye optimizaciones para mejorar rendimiento.
    """
    arr = list(arr_original)
    n = len(arr)
    
    # Caso base
    if n <= 1:
        yield {'array': list(arr), 'pass_type': 'Finalizado', 'status': 'Arreglo muy pequeño, ya ordenado',
               'highlights': {'all_sorted': True}}
        return
    
    # Optimización: detección rápida de arrays ya ordenados
    is_sorted = True
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            is_sorted = False
            break
    
    if is_sorted:
        yield {'array': list(arr), 'pass_type': 'Finalizado', 'status': 'Arreglo ya ordenado',
              'highlights': {'all_sorted': True}}
        return
    
    # Optimización: umbral adaptativo para similitud
    rango = max(arr) - min(arr)
    umbral_similitud = max(1, rango * 0.05)  # 5% del rango, mínimo 1
    
    max_iterations = n * n // 2 + 5  # Límite más ajustado
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
        
        # Optimización: detección de secciones ya ordenadas
        seccion_ordenada_inicio = 0
        while seccion_ordenada_inicio + 1 < n and arr[seccion_ordenada_inicio] <= arr[seccion_ordenada_inicio + 1]:
            seccion_ordenada_inicio += 1
            
        seccion_ordenada_fin = n - 1
        while seccion_ordenada_fin > 0 and arr[seccion_ordenada_fin - 1] <= arr[seccion_ordenada_fin]:
            seccion_ordenada_fin -= 1
            
        # Si todo está ordenado, terminar
        if seccion_ordenada_inicio >= seccion_ordenada_fin:
            yield {'array': list(arr), 'pass_type': 'Finalizado', 
                   'status': '¡Arreglo Ordenado!', 
                   'highlights': {'all_sorted': True}}
            return
        
        # --- Pasada de Flujo Ascendente (grupos hacia la izquierda) ---
        yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 
               'status': 'Iniciando Pasada Ascendente de Grupos', 
               'highlights': {}}
        
        i = max(1, seccion_ordenada_inicio + 1)
        while i < seccion_ordenada_fin + 1:
            # Identificar un grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            valor_referencia = arr[i]
            
            # Buscar el final del grupo actual con límite
            j = i + 1
            max_grupo_size = min(50, n - i)  # Limitar tamaño máximo de grupo
            while j < i + max_grupo_size and j < n and abs(arr[j] - valor_referencia) <= umbral_similitud:
                grupo_fin = j
                j += 1
            
            # Visualización: Identificando grupo
            grupo_highlights = {idx: 'grupo' for idx in range(grupo_inicio, grupo_fin + 1)}
            yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 
                   'status': f'Identificando grupo desde A[{grupo_inicio}] hasta A[{grupo_fin}]',
                   'highlights': grupo_highlights}
            
            # Verificar si el grupo debe moverse hacia la izquierda
            if grupo_inicio > 0 and arr[grupo_inicio] < arr[grupo_inicio - 1]:
                # Extraer grupo
                grupo_valores = arr[grupo_inicio:grupo_fin + 1]
                grupo_valores_original = list(grupo_valores)
                grupo_valores.sort()  # Ordenar el grupo internamente
                
                yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 
                       'status': f'Extrayendo grupo {grupo_valores_original} para ordenamiento',
                       'highlights': grupo_highlights}
                
                # Pre-calcular el valor mínimo
                min_valor = grupo_valores[0]
                
                # Encontrar punto de inserción para el grupo
                j = grupo_inicio - 1
                while j >= 0 and arr[j] > min_valor:
                    yield {'array': list(arr), 'pass_type': 'Flujo Ascendente', 
                           'status': f'Comparando A[{j}]={arr[j]} con valor mínimo del grupo {min_valor}',
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
                
                # Crear el nuevo segmento combinado
                nuevo_segmento = grupo_valores + elementos_a_desplazar
                
                # Reemplazar el segmento completo
                for idx, val in enumerate(nuevo_segmento):
                    arr[punto_insercion + idx] = val
                
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
        
        i = min(n - 2, seccion_ordenada_fin - 1)
        while i >= seccion_ordenada_inicio:
            # Identificar un grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            valor_referencia = arr[i]
            
            # Buscar el inicio del grupo actual con límite
            j = i - 1
            max_grupo_size = min(50, i + 1)  # Limitar tamaño máximo de grupo
            while j >= i - max_grupo_size and j >= 0 and abs(arr[j] - valor_referencia) <= umbral_similitud:
                grupo_inicio = j
                j -= 1
                
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
                
                # Pre-calcular el valor máximo
                max_valor = grupo_valores[-1]
                
                # Encontrar punto final para el grupo
                j = grupo_fin + 1
                while j < n and arr[j] < max_valor:
                    yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 
                           'status': f'Comparando A[{j}]={arr[j]} con valor máximo del grupo {max_valor}',
                           'highlights': {**grupo_highlights, 'j': j}}
                    j += 1
                
                yield {'array': list(arr), 'pass_type': 'Flujo Descendente', 
                       'status': f'Punto final para el grupo: {j}',
                       'highlights': {**grupo_highlights}}
                
                # Mover elementos entre grupo_fin+1 y j
                elementos_a_desplazar = arr[grupo_fin + 1:j]
                
                # Hacer una copia del arreglo antes de modificarlo
                arr_antes = list(arr)
                
                # Crear el nuevo segmento combinado
                nuevo_segmento = elementos_a_desplazar + grupo_valores
                
                # Reemplazar el segmento completo
                for idx, val in enumerate(nuevo_segmento):
                    arr[grupo_inicio + idx] = val
                
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