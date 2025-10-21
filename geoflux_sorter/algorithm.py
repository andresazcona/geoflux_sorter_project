def geoflux_sort(arr):
    """
    Ordena un arreglo in-place utilizando el algoritmo GeoFlux Sort.
    
    GeoFlux Sort es un algoritmo bidireccional que identifica grupos de elementos
    similares y los migra como unidades hacia sus posiciones correctas.
    
    Args:
        arr (list): Arreglo de elementos comparables a ordenar in-place.
        
    Returns:
        None: El arreglo se modifica directamente.
        
    Complejidad Temporal:
        - Mejor caso: O(n) para arreglos ya ordenados
        - Caso promedio: O(n²)
        - Peor caso: O(n²)
        
    Complejidad Espacial:
        - O(1) auxiliar (ordenamiento in-place)
        
    Ejemplo:
        >>> datos = [5, 2, 9, 1, 5, 6]
        >>> geoflux_sort(datos)
        >>> print(datos)
        [1, 2, 5, 5, 6, 9]
    """
    n = len(arr)
    
    # Caso base: arreglos de 0 o 1 elemento ya están ordenados
    if n <= 1:
        return
    
    # Optimización: detección temprana de arreglos ya ordenados
    # Realiza una pasada O(n) para verificar si el arreglo está ordenado
    is_sorted = True
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            is_sorted = False
            break
    if is_sorted:
        return
    
    # Optimización: usar insertion sort para arreglos pequeños
    # Insertion sort es más eficiente que GeoFlux para n <= 20
    if n <= 20:
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return
    
    # Calcular umbral adaptativo para determinar similitud entre elementos
    # El umbral se ajusta automáticamente según el rango de valores
    rango = max(arr) - min(arr)
    
    # Si todos los elementos son iguales, el arreglo ya está ordenado
    if rango == 0:
        return
    
    # Umbral de similitud: 5% del rango de valores
    # Elementos cuya diferencia sea menor al umbral se consideran "similares"
    umbral_similitud = rango * 0.05
    
    # Bucle principal: continúa mientras haya elementos que necesiten moverse
    elementos_desplazados_en_ciclo = True
    
    while elementos_desplazados_en_ciclo:
        elementos_desplazados_en_ciclo = False
        
        # Optimización: identificar y saltar secciones ya ordenadas
        # Encuentra el punto hasta donde el arreglo está ordenado desde el inicio
        seccion_ordenada_inicio = 0
        while seccion_ordenada_inicio + 1 < n and arr[seccion_ordenada_inicio] <= arr[seccion_ordenada_inicio + 1]:
            seccion_ordenada_inicio += 1
        
        # Encuentra el punto desde donde el arreglo está ordenado hasta el final
        seccion_ordenada_fin = n - 1
        while seccion_ordenada_fin > 0 and arr[seccion_ordenada_fin - 1] <= arr[seccion_ordenada_fin]:
            seccion_ordenada_fin -= 1
        
        # Si las secciones ordenadas se solapan, el arreglo completo está ordenado
        if seccion_ordenada_inicio >= seccion_ordenada_fin:
            return

        # === FASE 1: FLUJO ASCENDENTE ===
        # Migra grupos de elementos pequeños hacia la izquierda del arreglo
        
        # Comenzar después de la sección ya ordenada al inicio
        i = max(1, seccion_ordenada_inicio + 1)
        
        while i < seccion_ordenada_fin + 1:
            # Identificar un grupo de elementos con valores similares
            grupo_inicio = i
            grupo_fin = i
            valor_referencia = arr[i]
            
            # Expandir el grupo mientras los elementos sean similares al valor de referencia
            # Limitar el tamaño máximo del grupo a 50 elementos para eficiencia
            j = i + 1
            max_grupo_size = min(50, n - i)
            
            while j < i + max_grupo_size and j < n and abs(arr[j] - valor_referencia) <= umbral_similitud:
                grupo_fin = j
                j += 1
            
            # Determinar si el grupo debe migrar hacia la izquierda
            # Condición: el primer elemento del grupo es menor que el elemento anterior
            if grupo_inicio > 0 and arr[grupo_inicio] < arr[grupo_inicio - 1]:
                # Extraer y ordenar internamente el grupo
                grupo_valores = sorted(arr[grupo_inicio:grupo_fin + 1])
                
                # Obtener el valor mínimo del grupo para comparaciones
                min_valor = grupo_valores[0]
                
                # Encontrar la posición de inserción del grupo
                # Buscar hacia atrás hasta encontrar un elemento menor o igual
                j = grupo_inicio - 1
                while j >= 0 and arr[j] > min_valor:
                    j -= 1
                
                # La posición de inserción es justo después del último elemento menor
                punto_insercion = j + 1
                
                # Guardar los elementos que serán desplazados por el grupo
                elementos_a_desplazar = arr[punto_insercion:grupo_inicio]
                
                # Reconstruir el segmento: grupo ordenado + elementos desplazados
                nuevo_segmento = grupo_valores + elementos_a_desplazar
                
                # Aplicar los cambios al arreglo original
                for idx, val in enumerate(nuevo_segmento):
                    arr[punto_insercion + idx] = val
                
                # Marcar que se realizaron cambios en este ciclo
                elementos_desplazados_en_ciclo = True
            
            # Avanzar al siguiente grupo (después del grupo actual)
            i = grupo_fin + 1
        
        # === FASE 2: FLUJO DESCENDENTE ===
        # Migra grupos de elementos grandes hacia la derecha del arreglo
        
        # Comenzar antes de la sección ya ordenada al final
        i = min(n - 2, seccion_ordenada_fin - 1)
        
        while i >= seccion_ordenada_inicio:
            # Identificar un grupo de elementos con valores similares
            grupo_inicio = i
            grupo_fin = i
            valor_referencia = arr[i]
            
            # Expandir el grupo hacia la izquierda mientras los elementos sean similares
            # Limitar el tamaño máximo del grupo a 50 elementos
            j = i - 1
            max_grupo_size = min(50, i + 1)
            
            while j >= i - max_grupo_size and j >= 0 and abs(arr[j] - valor_referencia) <= umbral_similitud:
                grupo_inicio = j
                j -= 1
            
            # Determinar si el grupo debe migrar hacia la derecha
            # Condición: el último elemento del grupo es mayor que el elemento siguiente
            if grupo_fin + 1 < n and arr[grupo_fin] > arr[grupo_fin + 1]:
                # Extraer y ordenar internamente el grupo
                grupo_valores = sorted(arr[grupo_inicio:grupo_fin + 1])
                
                # Obtener el valor máximo del grupo para comparaciones
                max_valor = grupo_valores[-1]
                
                # Encontrar la posición final para el grupo
                # Buscar hacia adelante hasta encontrar un elemento mayor o igual
                j = grupo_fin + 1
                while j < n and arr[j] < max_valor:
                    j += 1
                
                # Guardar los elementos que serán desplazados por el grupo
                elementos_a_desplazar = arr[grupo_fin + 1:j]
                
                # Reconstruir el segmento: elementos desplazados + grupo ordenado
                nuevo_segmento = elementos_a_desplazar + grupo_valores
                
                # Aplicar los cambios al arreglo original
                for idx, val in enumerate(nuevo_segmento):
                    arr[grupo_inicio + idx] = val
                
                # Marcar que se realizaron cambios en este ciclo
                elementos_desplazados_en_ciclo = True
            
            # Retroceder al siguiente grupo (antes del grupo actual)
            i = grupo_inicio - 1

def geoflux_sort_generator(arr_original):
    """
    Generador que ejecuta GeoFlux Sort paso a paso, cediendo el estado en cada iteración.
    
    Esta versión permite observar el progreso del algoritmo en cada paso,
    ideal para visualizaciones y depuración.
    
    Args:
        arr_original (list): Arreglo original a ordenar.
        
    Yields:
        dict: Diccionario con información del estado actual:
            - 'array': Copia del arreglo en el estado actual
            - 'pass_type': Tipo de pasada ('Flujo Ascendente', 'Flujo Descendente', 'Finalizado')
            - 'status': Descripción textual de la operación actual
            - 'highlights': Diccionario con índices a resaltar en visualizaciones
            
    Ejemplo:
        >>> datos = [5, 2, 9, 1]
        >>> for estado in geoflux_sort_generator(datos):
        ...     print(f"{estado['array']} - {estado['status']}")
    """
    # Crear una copia del arreglo para no modificar el original
    arr = list(arr_original)
    n = len(arr)
    
    # Caso base: arreglos de 0 o 1 elemento
    if n <= 1:
        yield {
            'array': list(arr),
            'pass_type': 'Finalizado',
            'status': 'Arreglo muy pequeño, ya ordenado',
            'highlights': {'all_sorted': True}
        }
        return
    
    # Verificar si el arreglo ya está ordenado
    is_sorted = True
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            is_sorted = False
            break
    
    if is_sorted:
        yield {
            'array': list(arr),
            'pass_type': 'Finalizado',
            'status': 'Arreglo ya ordenado',
            'highlights': {'all_sorted': True}
        }
        return
    
    # Calcular umbral adaptativo de similitud
    rango = max(arr) - min(arr)
    umbral_similitud = max(1, rango * 0.05)
    
    # Límite de seguridad para evitar bucles infinitos
    max_iterations = n * n // 2 + 5
    current_iterations = 0
    
    # Bucle principal del algoritmo
    elementos_desplazados_en_ciclo = True
    
    while elementos_desplazados_en_ciclo:
        current_iterations += 1
        
        # Verificación de seguridad contra bucles infinitos
        if current_iterations > max_iterations:
            yield {
                'array': list(arr),
                'pass_type': 'Detenido',
                'status': 'Parada por seguridad (max_iterations)',
                'highlights': {}
            }
            return
        
        elementos_desplazados_en_ciclo = False
        
        # Detectar secciones ya ordenadas para optimizar el recorrido
        seccion_ordenada_inicio = 0
        while seccion_ordenada_inicio + 1 < n and arr[seccion_ordenada_inicio] <= arr[seccion_ordenada_inicio + 1]:
            seccion_ordenada_inicio += 1
        
        seccion_ordenada_fin = n - 1
        while seccion_ordenada_fin > 0 and arr[seccion_ordenada_fin - 1] <= arr[seccion_ordenada_fin]:
            seccion_ordenada_fin -= 1
        
        # Si todo el arreglo está ordenado, finalizar
        if seccion_ordenada_inicio >= seccion_ordenada_fin:
            yield {
                'array': list(arr),
                'pass_type': 'Finalizado',
                'status': 'Arreglo Ordenado',
                'highlights': {'all_sorted': True}
            }
            return
        
        # === FASE 1: FLUJO ASCENDENTE ===
        yield {
            'array': list(arr),
            'pass_type': 'Flujo Ascendente',
            'status': 'Iniciando Pasada Ascendente de Grupos',
            'highlights': {}
        }
        
        i = max(1, seccion_ordenada_inicio + 1)
        
        while i < seccion_ordenada_fin + 1:
            # Identificar grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            valor_referencia = arr[i]
            
            # Expandir el grupo mientras los elementos sean similares
            j = i + 1
            max_grupo_size = min(50, n - i)
            
            while j < i + max_grupo_size and j < n and abs(arr[j] - valor_referencia) <= umbral_similitud:
                grupo_fin = j
                j += 1
            
            # Visualizar el grupo identificado
            grupo_highlights = {idx: 'grupo' for idx in range(grupo_inicio, grupo_fin + 1)}
            yield {
                'array': list(arr),
                'pass_type': 'Flujo Ascendente',
                'status': f'Identificando grupo desde A[{grupo_inicio}] hasta A[{grupo_fin}]',
                'highlights': grupo_highlights
            }
            
            # Verificar si el grupo debe migrar hacia la izquierda
            if grupo_inicio > 0 and arr[grupo_inicio] < arr[grupo_inicio - 1]:
                # Extraer y guardar el grupo antes de ordenarlo
                grupo_valores = arr[grupo_inicio:grupo_fin + 1]
                grupo_valores_original = list(grupo_valores)
                grupo_valores.sort()
                
                yield {
                    'array': list(arr),
                    'pass_type': 'Flujo Ascendente',
                    'status': f'Extrayendo grupo {grupo_valores_original} para ordenamiento',
                    'highlights': grupo_highlights
                }
                
                # Valor mínimo del grupo para encontrar punto de inserción
                min_valor = grupo_valores[0]
                
                # Buscar hacia atrás para encontrar el punto de inserción
                j = grupo_inicio - 1
                while j >= 0 and arr[j] > min_valor:
                    yield {
                        'array': list(arr),
                        'pass_type': 'Flujo Ascendente',
                        'status': f'Comparando A[{j}]={arr[j]} con valor mínimo del grupo {min_valor}',
                        'highlights': {**grupo_highlights, 'j': j}
                    }
                    j -= 1
                
                # El punto de inserción está después del último elemento menor
                punto_insercion = j + 1
                
                yield {
                    'array': list(arr),
                    'pass_type': 'Flujo Ascendente',
                    'status': f'Punto de inserción para el grupo: {punto_insercion}',
                    'highlights': {**grupo_highlights, 'insertion_at': punto_insercion}
                }
                
                # Guardar elementos que serán desplazados
                elementos_a_desplazar = arr[punto_insercion:grupo_inicio]
                
                # Reconstruir el segmento
                nuevo_segmento = grupo_valores + elementos_a_desplazar
                
                # Aplicar cambios al arreglo
                for idx, val in enumerate(nuevo_segmento):
                    arr[punto_insercion + idx] = val
                
                # Mostrar el resultado de la migración
                yield {
                    'array': list(arr),
                    'pass_type': 'Flujo Ascendente',
                    'status': 'Grupo movido a nueva posición y ordenado internamente',
                    'highlights': {idx: 'moved_group' for idx in range(punto_insercion, punto_insercion + len(grupo_valores))}
                }
                
                # Marcar que hubo cambios
                elementos_desplazados_en_ciclo = True
            
            # Avanzar al siguiente grupo
            i = grupo_fin + 1
        
        # === FASE 2: FLUJO DESCENDENTE ===
        yield {
            'array': list(arr),
            'pass_type': 'Flujo Descendente',
            'status': 'Iniciando Pasada Descendente de Grupos',
            'highlights': {}
        }
        
        i = min(n - 2, seccion_ordenada_fin - 1)
        
        while i >= seccion_ordenada_inicio:
            # Identificar grupo de elementos similares
            grupo_inicio = i
            grupo_fin = i
            valor_referencia = arr[i]
            
            # Expandir el grupo hacia la izquierda
            j = i - 1
            max_grupo_size = min(50, i + 1)
            
            while j >= i - max_grupo_size and j >= 0 and abs(arr[j] - valor_referencia) <= umbral_similitud:
                grupo_inicio = j
                j -= 1
            
            # Visualizar el grupo identificado
            grupo_highlights = {idx: 'grupo' for idx in range(grupo_inicio, grupo_fin + 1)}
            yield {
                'array': list(arr),
                'pass_type': 'Flujo Descendente',
                'status': f'Identificando grupo desde A[{grupo_inicio}] hasta A[{grupo_fin}]',
                'highlights': grupo_highlights
            }
            
            # Verificar si el grupo debe migrar hacia la derecha
            if grupo_fin + 1 < n and arr[grupo_fin] > arr[grupo_fin + 1]:
                # Extraer y guardar el grupo antes de ordenarlo
                grupo_valores = arr[grupo_inicio:grupo_fin + 1]
                grupo_valores_original = list(grupo_valores)
                grupo_valores.sort()
                
                yield {
                    'array': list(arr),
                    'pass_type': 'Flujo Descendente',
                    'status': f'Extrayendo grupo {grupo_valores_original} para ordenamiento',
                    'highlights': grupo_highlights
                }
                
                # Valor máximo del grupo para encontrar punto de inserción
                max_valor = grupo_valores[-1]
                
                # Buscar hacia adelante para encontrar el punto final
                j = grupo_fin + 1
                while j < n and arr[j] < max_valor:
                    yield {
                        'array': list(arr),
                        'pass_type': 'Flujo Descendente',
                        'status': f'Comparando A[{j}]={arr[j]} con valor máximo del grupo {max_valor}',
                        'highlights': {**grupo_highlights, 'j': j}
                    }
                    j += 1
                
                yield {
                    'array': list(arr),
                    'pass_type': 'Flujo Descendente',
                    'status': f'Punto final para el grupo: {j}',
                    'highlights': {**grupo_highlights}
                }
                
                # Guardar elementos que serán desplazados
                elementos_a_desplazar = arr[grupo_fin + 1:j]
                
                # Reconstruir el segmento
                nuevo_segmento = elementos_a_desplazar + grupo_valores
                
                # Aplicar cambios al arreglo
                for idx, val in enumerate(nuevo_segmento):
                    arr[grupo_inicio + idx] = val
                
                # Mostrar el resultado de la migración
                inicio_grupo_movido = grupo_inicio + len(elementos_a_desplazar)
                fin_grupo_movido = inicio_grupo_movido + len(grupo_valores)
                
                yield {
                    'array': list(arr),
                    'pass_type': 'Flujo Descendente',
                    'status': 'Grupo movido a nueva posición y ordenado internamente',
                    'highlights': {idx: 'moved_group' for idx in range(inicio_grupo_movido, fin_grupo_movido)}
                }
                
                # Marcar que hubo cambios
                elementos_desplazados_en_ciclo = True
            
            # Retroceder al siguiente grupo
            i = grupo_inicio - 1
    
    # Finalización: el arreglo está completamente ordenado
    yield {
        'array': list(arr),
        'pass_type': 'Finalizado',
        'status': 'Arreglo Ordenado',
        'highlights': {'all_sorted': True}
    }