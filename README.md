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

GeoFlux Sort es un algoritmo de ordenamiento bidireccional que combina conceptos de varios algoritmos clásicos, principalmente insertion sort, pero operando en ambas direcciones.

### Funcionamiento

El algoritmo realiza múltiples pasadas sobre el arreglo, alternando entre dos tipos de operaciones:

1. **Flujo Ascendente**: Los elementos pequeños "fluyen" hacia la izquierda del arreglo.
2. **Flujo Descendente**: Los elementos grandes "fluyen" hacia la derecha del arreglo.

Este proceso continúa hasta que no se realiza ningún cambio durante un ciclo completo, lo que indica que el arreglo está completamente ordenado.

### Pseudocódigo

```
PROCEDURE GeoFluxSort(array)

  n = longitud de array

  SI n <= 1 ENTONCES RETORNAR // No necesita ordenarse

  elementos_desplazados_en_ciclo = VERDADERO

  MIENTRAS elementos_desplazados_en_ciclo HACER

    elementos_desplazados_en_ciclo = FALSO

    // --- Pasada de Flujo Ascendente (Elementos pequeños "fluyen" hacia la izquierda) ---
    PARA i DESDE 1 HASTA n-1 HACER
      elemento_clave = array[i]
      
      // Solo iniciar el "flujo" si el elemento_clave es menor que su vecino izquierdo
      SI elemento_clave < array[i-1] ENTONCES
        j = i - 1
        // Desplazar elementos mayores hacia la derecha para hacer espacio
        MIENTRAS j >= 0 Y array[j] > elemento_clave HACER
          array[j+1] = array[j]
          j = j - 1
        FIN MIENTRAS
        array[j+1] = elemento_clave // Insertar el elemento_clave en su posición correcta
        elementos_desplazados_en_ciclo = VERDADERO
      FIN SI
    FIN PARA

    // --- Pasada de Flujo Descendente (Elementos grandes "fluyen" hacia la derecha) ---
    PARA i DESDE n-2 HACIA ABAJO HASTA 0 HACER // Iterar desde el penúltimo hasta el primero
      elemento_clave = array[i]

      // Solo iniciar el "flujo" si el elemento_clave es mayor que su vecino derecho
      SI elemento_clave > array[i+1] ENTONCES
        j = i + 1
        // Desplazar elementos menores hacia la izquierda para hacer espacio
        MIENTRAS j < n Y array[j] < elemento_clave HACER
          array[j-1] = array[j]
          j = j + 1
        FIN MIENTRAS
        array[j-1] = elemento_clave // Insertar el elemento_clave en su posición correcta
        elementos_desplazados_en_ciclo = VERDADERO
      FIN SI
    FIN PARA

  FIN MIENTRAS

FIN PROCEDURA
```

## Características

- **Ordenamiento In-Place**: Modifica el arreglo directamente sin necesitar memoria adicional proporcional al tamaño de la entrada.
- **Estabilidad**: No garantiza la preservación del orden relativo de elementos con valores iguales.
- **Visualización**: Incluye herramientas para crear animaciones del proceso de ordenamiento.
- **Análisis de Rendimiento**: Herramientas para benchmark y comparación con otros algoritmos.

## Instalación

### Prerrequisitos
- Python 3.6 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. Clona este repositorio:
```bash
git clone https://github.com/usuario/geoflux_sorter_project.git
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

Las pruebas de benchmark muestran que GeoFlux Sort es menos eficiente que el `sorted()` nativo de Python para grandes conjuntos de datos, pero su principal utilidad es educativa y para visualización.

Resultados representativos de benchmark:

| Tamaño | GeoFlux (Random) | GeoFlux (Ordenado) | GeoFlux (Invertido) | Python (Random) | Python (Ordenado) | Python (Invertido) |
|--------|------------------|--------------------|--------------------|----------------|-------------------|-------------------|
| 100    | 0.000317s        | 0.000010s          | 0.000307s          | 0.000010s      | 0.000001s         | 0.000001s         |
| 500    | 0.004750s        | 0.000055s          | 0.006307s          | 0.000036s      | 0.000003s         | 0.000003s         |
| 1000   | 0.018730s        | 0.000100s          | 0.028682s          | 0.000079s      | 0.000005s         | 0.000005s         |
| 2000   | 0.064139s        | 0.000186s          | 0.121810s          | 0.000165s      | 0.000009s         | 0.000010s         |
| 5000   | 0.441502s        | 0.000503s          | 0.778414s          | 0.000437s      | 0.000023s         | 0.000025s         |

## Visualización

Una de las principales características de GeoFlux Sorter es su capacidad para visualizar el proceso de ordenamiento. La visualización usa matplotlib para crear una animación paso a paso, mostrando:

- El estado actual del arreglo.
- Los elementos que se están comparando.
- Los elementos que se están moviendo.
- El progreso general del ordenamiento.

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
   - `geoflux_sort`: Función principal que implementa el algoritmo.
   - `geoflux_sort_generator`: Versión generadora que expone el estado en cada paso.

2. **Sistema de animación**
   - `create_geoflux_animation`: Crea y muestra/guarda animaciones del proceso.
   - `update_plot`: Actualiza cada frame de la animación.

### Detalles del Algoritmo

El algoritmo GeoFlux Sort combina características de:
- **Insertion sort**: Para la inserción de elementos en su posición correcta.
- **Bubble sort**: En la forma de "burbujear" elementos en ambas direcciones.

La bidireccionalidad del algoritmo tiene como objetivo:
1. Mover elementos pequeños hacia el inicio del arreglo.
2. Mover elementos grandes hacia el final del arreglo.

Este enfoque puede ser más eficiente que algoritmos unidireccionales en ciertos casos, especialmente cuando hay elementos que están muy lejos de su posición final.

## Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Haz fork del proyecto.
2. Crea una rama para tu característica (`git checkout -b feature/amazing-feature`).
3. Realiza tus cambios y haz commit (`git commit -m 'Add amazing feature'`).
4. Sube tu rama (`git push origin feature/amazing-feature`).
5. Abre un Pull Request.

### Áreas para mejorar
- Optimización del rendimiento del algoritmo.
- Mejoras en la visualización y animación.
- Ampliación de casos de prueba.
- Documentación adicional y ejemplos.

## Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).