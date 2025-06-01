# GeoFlux Sorter

GeoFlux Sorter es una implementación de un algoritmo de ordenamiento bidireccional con capacidades de visualización. Este proyecto proporciona tanto la funcionalidad de ordenamiento como herramientas para visualizar el proceso de ordenamiento paso a paso.

## Tabla de Contenidos
- [GeoFlux Sorter](#geoflux-sorter)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción del Algoritmo](#descripción-del-algoritmo)
    - [Funcionamiento](#funcionamiento)
    - [Pseudocódigo](#pseudocódigo)
  - [Características](#características)
  - [Instalación](#instalación)
    - [Prerrequisitos](#prerrequisitos)
    - [Pasos de instalación](#pasos-de-instalación)
  - [Uso](#uso)
    - [Uso básico](#uso-básico)
    - [Generador para visualización paso a paso](#generador-para-visualización-paso-a-paso)
    - [Creación de animación](#creación-de-animación)
  - [Ejemplos](#ejemplos)
    - [Ejecutar ejemplos](#ejecutar-ejemplos)
  - [Rendimiento](#rendimiento)
  - [Visualización](#visualización)
    - [Personalización de visualizaciones](#personalización-de-visualizaciones)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Implementación Técnica](#implementación-técnica)
    - [Componentes Principales](#componentes-principales)
    - [Detalles del Algoritmo](#detalles-del-algoritmo)
  - [Contribuir](#contribuir)
    - [Áreas para mejorar](#áreas-para-mejorar)
  - [Licencia](#licencia)

## Descripción del Algoritmo

GeoFlux Sort es un algoritmo de ordenamiento bidireccional que combina conceptos de varios algoritmos clásicos, pero con un enfoque innovador de ordenamiento por grupos o "migraciones", similar a cómo se mueven grupos de elementos en la naturaleza.

### Funcionamiento

El algoritmo realiza múltiples pasadas sobre el arreglo, alternando entre dos tipos de operaciones:

1. **Flujo Ascendente**: Los grupos de elementos pequeños "migran" hacia la izquierda del arreglo.
2. **Flujo Descendente**: Los grupos de elementos grandes "migran" hacia la derecha del arreglo.

El algoritmo identifica grupos de elementos con valores similares y los mueve como unidades, ordenándolos internamente durante el proceso. Este enfoque es especialmente eficiente para datos con distribuciones no uniformes o que presentan "clusters" naturales.

Este proceso continúa hasta que no se realiza ningún cambio durante un ciclo completo, lo que indica que el arreglo está completamente ordenado.

### Pseudocódigo

```
PROCEDURE GeoFluxSort(array)
    SI longitud(array) <= 1 ENTONCES
        RETORNAR
    FIN SI

    umbral_similitud ← 5  # Ajustar según las características de los datos
    elementos_desplazados_en_ciclo ← VERDADERO

    MIENTRAS elementos_desplazados_en_ciclo HACER
        elementos_desplazados_en_ciclo ← FALSO
        
        // Pasada de Flujo Ascendente (grupos hacia la izquierda)
        i ← 1
        MIENTRAS i < longitud(array) HACER
            // Identificar un grupo de elementos similares
            grupo_inicio ← i
            grupo_fin ← i
            
            // Buscar el final del grupo actual
            MIENTRAS grupo_fin + 1 < longitud(array) Y 
                   abs(array[grupo_fin + 1] - array[grupo_inicio]) <= umbral_similitud HACER
                grupo_fin ← grupo_fin + 1
            FIN MIENTRAS
            
            // Verificar si el grupo debe moverse hacia la izquierda
            SI grupo_inicio > 0 Y array[grupo_inicio] < array[grupo_inicio - 1] ENTONCES
                // Extraer y ordenar el grupo
                grupo_valores ← array[grupo_inicio:grupo_fin + 1]
                ordenar(grupo_valores)
                
                // Encontrar punto de inserción para el grupo
                j ← grupo_inicio - 1
                MIENTRAS j >= 0 Y array[j] > grupo_valores[0] HACER
                    j ← j - 1
                FIN MIENTRAS
                punto_insercion ← j + 1
                
                // Reorganizar el arreglo para insertar el grupo
                [Implementación detallada omitida]
                
                elementos_desplazados_en_ciclo ← VERDADERO
            FIN SI
            
            i ← grupo_fin + 1
        FIN MIENTRAS
        
        // Pasada de Flujo Descendente (grupos hacia la derecha)
        [Implementación similar a la pasada ascendente pero en dirección contraria]
    FIN MIENTRAS
FIN PROCEDURE
```

## Características

- **Ordenamiento In-Place**: Modifica el arreglo directamente sin necesitar memoria adicional proporcional al tamaño de la entrada.
- **Estabilidad**: No garantiza la preservación del orden relativo de elementos con valores iguales.
- **Ordenamiento por Grupos**: Identifica y mueve grupos de elementos similares como unidades.
- **Visualización**: Incluye herramientas para crear animaciones del proceso de ordenamiento.
- **Análisis de Rendimiento**: Herramientas para benchmark y comparación con otros algoritmos.

## Instalación

### Prerrequisitos
- Python 3.6 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. Clona este repositorio:
```bash
git clone https://github.com/andresazcona/geoflux_sorter_project
cd geoflux_sorter_project
```

2. Crea un entorno virtual (recomendado):
```bash
python -m venv venv
```

3. Activa el entorno virtual:
   - En Windows (CMD): `venv\Scripts\activate.bat`
   - En Windows (PowerShell): `.\venv\Scripts\Activate.ps1`
   - En Unix/MacOS: `source venv/bin/activate`

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Uso básico

```python
from geoflux_sorter import geoflux_sort

# Crear una lista para ordenar
my_list = [5, 2, 9, 1, 5, 6]

# Ordenar la lista (in-place)
geoflux_sort(my_list)

print(my_list)  # Resultado: [1, 2, 5, 5, 6, 9]
```

### Generador para visualización paso a paso

```python
from geoflux_sorter import geoflux_sort_generator

# Crear una lista para ordenar
my_list = [5, 2, 9, 1, 5, 6]

# Obtener un generador para seguir el proceso paso a paso
for state in geoflux_sort_generator(my_list):
    print(state['array'], f"- {state['status']}")
```

### Creación de animación

```python
from geoflux_sorter import create_geoflux_animation

# Crear una lista para ordenar
my_list = [5, 2, 9, 1, 5, 6]

# Crear y mostrar una animación del proceso de ordenamiento
animation = create_geoflux_animation(my_list, interval=200)
```

## Ejemplos

El proyecto incluye ejemplos prácticos en la carpeta `examples/`:

- `run_sort_example.py`: Ejemplo básico de uso del algoritmo.
- `run_animation_example.py`: Ejemplo de la visualización del algoritmo.
- `benchmark_sort.py`: Comparativa de rendimiento con otros algoritmos.

### Ejecutar ejemplos

```bash
# Ejemplo básico de ordenamiento
python examples/run_sort_example.py

# Visualización del algoritmo
python examples/run_animation_example.py

# Benchmark de rendimiento
python examples/benchmark_sort.py
```

## Rendimiento

El rendimiento de GeoFlux Sort varía según el tipo y tamaño de los datos:

- **Mejor caso**: O(n) para arreglos ya ordenados.
- **Caso promedio**: O(n²), similar a insertion sort.
- **Peor caso**: O(n²), típicamente para arreglos invertidos.

El enfoque de migración por grupos puede mejorar el rendimiento en datos que contienen naturalmente clusters de valores similares, ya que permite mover múltiples elementos en una sola operación.

Las pruebas de benchmark muestran que GeoFlux Sort es menos eficiente que el `sorted()` nativo de Python para grandes conjuntos de datos, pero su principal utilidad es educativa y para visualización.

Resultados representativos de benchmark:

+----------+--------------------+----------------------+-----------------------+-------------------+---------------------+----------------------+
|   Tamaño | GeoFlux (Random)   | GeoFlux (Ordenado)   | GeoFlux (Invertido)   | Python (Random)   | Python (Ordenado)   | Python (Invertido)   |
+==========+====================+======================+=======================+===================+=====================+======================+
|      100 | 0.000288s          | 0.000021s            | 0.000129s             | 0.000008s         | 0.000001s           | 0.000000s            |
+----------+--------------------+----------------------+-----------------------+-------------------+---------------------+----------------------+
|      500 | 0.004669s          | 0.000094s            | 0.000579s             | 0.000032s         | 0.000002s           | 0.000002s            |
+----------+--------------------+----------------------+-----------------------+-------------------+---------------------+----------------------+
|     1000 | 0.021862s          | 0.000189s            | 0.001184s             | 0.000076s         | 0.000005s           | 0.000006s            |
+----------+--------------------+----------------------+-----------------------+-------------------+---------------------+----------------------+
|     2000 | 0.087482s          | 0.000378s            | 0.002480s             | 0.000159s         | 0.000010s           | 0.000010s            |
+----------+--------------------+----------------------+-----------------------+-------------------+---------------------+----------------------+
|     5000 | 0.554990s          | 0.000990s            | 0.006474s             | 0.000426s         | 0.000023s           | 0.000025s            |
+----------+--------------------+----------------------+-----------------------+-------------------+---------------------+----------------------+

## Visualización

Una de las principales características de GeoFlux Sorter es su capacidad para visualizar el proceso de ordenamiento. La visualización usa matplotlib para crear una animación paso a paso, mostrando:

- El estado actual del arreglo.
- Los grupos de elementos que se están identificando.
- Los grupos que se están moviendo como unidades.
- El progreso general del ordenamiento.

La visualización es particularmente efectiva para observar cómo los grupos de elementos migran a través del arreglo, de manera similar a patrones de migración en la naturaleza.

### Personalización de visualizaciones

La función `create_geoflux_animation` permite personalizar varios aspectos:

```python
create_geoflux_animation(
    initial_data,     # Datos a ordenar
    interval=300,     # Intervalo entre frames (ms)
    save_to_file=None # Guardar como archivo (requiere ffmpeg)
)
```

## Estructura del Proyecto

```
geoflux_sorter_project/
├── geoflux_sorter/         # Paquete principal
│   ├── __init__.py         # Exporta funciones principales
│   ├── algorithm.py        # Implementación del algoritmo
│   └── animator.py         # Visualización y animación
├── tests/                  # Tests unitarios
│   ├── __init__.py
│   └── test_algorithm.py   # Tests del algoritmo
├── examples/               # Ejemplos de uso
│   ├── run_sort_example.py
│   ├── run_animation_example.py
│   └── benchmark_sort.py
├── requirements.txt        # Dependencias
└── README.md               # Este archivo
```

## Implementación Técnica

### Componentes Principales

1. **Algoritmo de ordenamiento**
   - `geoflux_sort`: Función principal que implementa el algoritmo de migración por grupos.
   - `geoflux_sort_generator`: Versión generadora que expone el estado en cada paso.

2. **Sistema de animación**
   - `create_geoflux_animation`: Crea y muestra/guarda animaciones del proceso.
   - `update_plot`: Actualiza cada frame de la animación, con soporte para visualizar grupos.

### Detalles del Algoritmo

El algoritmo GeoFlux Sort con migración por grupos combina características de:
- **Insertion sort**: Para la inserción de elementos en su posición correcta.
- **Bubble sort**: En la forma de "burbujear" elementos en ambas direcciones.
- **Bucket sort/Bin sort**: En la forma de agrupar elementos similares.

Los aspectos clave del algoritmo son:
1. **Identificación de grupos**: Detecta elementos con valores similares usando un umbral adaptativo.
2. **Ordenamiento de grupos**: Ordena cada grupo internamente antes de insertarlo.
3. **Migración bidireccional**: Los grupos pequeños migran hacia la izquierda y los grandes hacia la derecha.

Este enfoque de migración grupal puede ser más eficiente que algoritmos tradicionales en ciertos escenarios, particularmente con datos que tienen agrupaciones naturales.

## Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Haz fork del proyecto.
2. Crea una rama para tu característica (`git checkout -b feature/amazing-feature`).
3. Realiza tus cambios y haz commit (`git commit -m 'Add amazing feature'`).
4. Sube tu rama (`git push origin feature/amazing-feature`).
5. Abre un Pull Request.

### Áreas para mejorar
- Optimización del umbral de similitud para identificar grupos de manera más efectiva.
- Implementación de estrategias adaptativas para ajustar el umbral según las características de los datos.
- Mejoras en la visualización de grupos y migraciones.
- Ampliación de casos de prueba específicos para el comportamiento de grupos.
- Documentación adicional y ejemplos sobre escenarios donde la migración por grupos es especialmente eficiente.

## Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).