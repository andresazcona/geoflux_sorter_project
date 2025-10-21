# GeoFlux Sorter

<div align="center">

**Un algoritmo de ordenamiento bidireccional con migración por grupos y visualización interactiva**

[![Python Version](https://img.shields.io/badge/python-.6%B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-.0.0-green.svg)](https://github.com/andresazcona/geoflux_sorter_project)

</div>

---

##  Tabla de Contenidos

- [Descripción](#-descripción)
- [Características Principales](#-características-principales)
- [Instalación](#-instalación)
- [Uso Rápido](#-uso-rápido)
- [Ejemplos](#-ejemplos)
- [El Algoritmo](#-el-algoritmo)
- [Análisis de Rendimiento](#-análisis-de-rendimiento)
- [Visualización](#-visualización)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

---

##  Descripción

**GeoFlux Sorter** es un algoritmo de ordenamiento experimental que implementa un enfoque bidireccional basado en **migración por grupos**. Inspirado en patrones de migración naturales, el algoritmo identifica clusters de elementos similares y los mueve como unidades cohesivas hacia sus posiciones correctas.

### ¿Qué lo hace único?

- **Ordenamiento por Grupos**: Identifica y mueve conjuntos de elementos similares como unidades, no elemento por elemento
- **Flujo Bidireccional**: Alterna entre migrar elementos pequeños hacia la izquierda y grandes hacia la derecha
- **Umbral Adaptativo**: Ajusta automáticamente la definición de "similitud" según las características de los datos
- **Visualización Integrada**: Permite observar el proceso de ordenamiento en tiempo real

---

## ✨ Características Principales

| Característica | Descripción |
|----------------|-------------|
|  **Ordenamiento In-Place** | Modifica el arreglo directamente, sin memoria adicional |
|  **Visualización Interactiva** | Animaciones paso a paso del proceso de ordenamiento |
| ⚡ **Optimizaciones Inteligentes** | Detección de secciones ordenadas y casos base |
|  **Suite de Pruebas** | Tests unitarios y benchmarks completos |
|  **Análisis de Rendimiento** | Comparativas con algoritmos estándar de Python |
|  **Personalizable** | Control sobre velocidad y estilo de animaciones |

---

##  Instalación

### Prerrequisitos

- **Python .6+** instalado en tu sistema
- **pip** (gestor de paquetes de Python)

### Pasos de Instalación

️⃣ **Clona el repositorio**
```bash
git clone https://github.com/andresazcona/geoflux_sorter_project.git
cd geoflux_sorter_project
```

️⃣ **Crea un entorno virtual** (recomendado)
```bash
python -m venv venv
```

️⃣ **Activa el entorno virtual**
```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps

# Windows (CMD)
venv\Scripts\activate.bat

# Unix/MacOS
source venv/bin/activate
```

️⃣ **Instala las dependencias**
```bash
pip install -r requirements.txt
```

✅ ¡Listo para usar!

---

##  Uso Rápido

### Ordenamiento Básico

```python
from geoflux_sorter import geoflux_sort

# Crear una lista desordenada
datos = [6, , 5, , , , 90]

# Ordenar in-place
geoflux_sort(datos)

print(datos)  # [, , , 5, , 6, 90]
```

### Visualización Paso a Paso

```python
from geoflux_sorter import geoflux_sort_generator

datos = [5, , 9, , 5, 6]

# Observar cada paso del algoritmo
for paso in geoflux_sort_generator(datos):
    print(f"{paso['array']} - {paso['status']}")
```

### Crear Animación

```python
from geoflux_sorter import create_geoflux_animation
import random

# Generar datos aleatorios
datos = random.sample(range(, 5), 0)

# Crear y mostrar animación
animacion = create_geoflux_animation(datos, interval=00)
```

---

##  Ejemplos

El proyecto incluye ejemplos listos para ejecutar en la carpeta `examples/`:

| Archivo | Descripción |
|---------|-------------|
| `run_sort_example.py` | Demuestra el ordenamiento con varios casos de prueba |
| `run_animation_example.py` | Crea una visualización animada del algoritmo |
| `benchmark_sort.py` | Compara rendimiento con otros algoritmos |

### Ejecutar Ejemplos

```bash
# Ejemplo básico
python examples/run_sort_example.py

# Visualización animada
python examples/run_animation_example.py

# Benchmark de rendimiento
python examples/benchmark_sort.py
```

---

##  El Algoritmo

### Cómo Funciona

GeoFlux Sort implementa un proceso de ordenamiento bidireccional inspirado en migraciones naturales:

####  Ciclo Principal

El algoritmo realiza ciclos completos hasta que no se requieren más cambios:

. **Detección de Grupos**: Identifica clusters de elementos con valores similares
. **Flujo Ascendente** ⬅️: Migra grupos de valores pequeños hacia la izquierda
. **Flujo Descendente** ➡️: Migra grupos de valores grandes hacia la derecha
. **Repetir**: Continúa hasta que el arreglo esté completamente ordenado

####  Optimizaciones Clave

- ✅ **Umbral Adaptativo**: Calcula automáticamente el umbral de similitud (5% del rango)
- ✅ **Detección Temprana**: Identifica arreglos ya ordenados en O(n)
- ✅ **Insertion Sort para Casos Pequeños**: Usa algoritmo más eficiente para n ≤ 0
- ✅ **Salto de Secciones Ordenadas**: Evita procesar segmentos ya ordenados
- ✅ **Límite de Tamaño de Grupo**: Previene grupos excesivamente grandes

### Pseudocódigo

```plaintext
FUNCIÓN GeoFluxSort(arreglo):
    n ← longitud(arreglo)
    
    // Casos base y optimizaciones
    SI n ≤  ENTONCES RETORNAR
    SI arreglo_está_ordenado(arreglo) ENTONCES RETORNAR
    SI n ≤ 0 ENTONCES insertion_sort(arreglo); RETORNAR
    
    // Calcular umbral adaptativo
    rango ← máximo(arreglo) - mínimo(arreglo)
    umbral_similitud ← rango × 0.05
    
    elementos_movidos ← VERDADERO
    
    MIENTRAS elementos_movidos HACER:
        elementos_movidos ← FALSO
        
        // Detectar secciones ya ordenadas
        inicio_ordenado ← detectar_inicio_ordenado(arreglo)
        fin_ordenado ← detectar_fin_ordenado(arreglo)
        
        // === FLUJO ASCENDENTE (⬅️) ===
        i ← inicio_ordenado + 
        MIENTRAS i < fin_ordenado HACER:
            // Identificar grupo de elementos similares
            grupo ← identificar_grupo(arreglo, i, umbral_similitud)
            
            // Si el grupo debe migrar hacia la izquierda
            SI arreglo[grupo.inicio] < arreglo[grupo.inicio - ] ENTONCES:
                valores_grupo ← ordenar(arreglo[grupo.inicio:grupo.fin])
                punto_inserción ← encontrar_punto_inserción(arreglo, valores_grupo[0])
                
                // Mover grupo a su nueva posición
                insertar_grupo(arreglo, valores_grupo, punto_inserción)
                elementos_movidos ← VERDADERO
            FIN SI
            
            i ← grupo.fin + 
        FIN MIENTRAS
        
        // === FLUJO DESCENDENTE (➡️) ===
        i ← fin_ordenado - 
        MIENTRAS i > inicio_ordenado HACER:
            // Identificar grupo de elementos similares
            grupo ← identificar_grupo_reverso(arreglo, i, umbral_similitud)
            
            // Si el grupo debe migrar hacia la derecha
            SI arreglo[grupo.inicio] > arreglo[grupo.inicio + ] ENTONCES:
                valores_grupo ← ordenar(arreglo[grupo.inicio:grupo.fin])
                punto_inserción ← encontrar_punto_inserción_derecha(arreglo, valores_grupo[-])
                
                // Mover grupo a su nueva posición
                insertar_grupo(arreglo, valores_grupo, punto_inserción)
                elementos_movidos ← VERDADERO
            FIN SI
            
            i ← grupo.inicio - 
        FIN MIENTRAS
    FIN MIENTRAS
FIN FUNCIÓN
```

### Comparación con Otros Algoritmos

GeoFlux Sort combina características de varios algoritmos clásicos:

| Algoritmo | Influencia en GeoFlux |
|-----------|----------------------|
| **Insertion Sort** | Inserción de grupos en posiciones correctas |
| **Bubble Sort** | Flujo bidireccional de elementos |
| **Cocktail Sort** | Pasadas alternadas en ambas direcciones |
| **Bucket Sort** | Agrupación de elementos similares |

**Ventaja Principal**: Eficiencia mejorada en datos con clusters naturales de valores similares.

---

##  Análisis de Rendimiento

### Complejidad Temporal

| Escenario | Complejidad | Descripción |
|-----------|-------------|-------------|
| **Mejor Caso** | O(n) | Arreglo ya ordenado |
| **Caso Promedio** | O(n²) | Datos aleatorios |
| **Peor Caso** | O(n²) | Arreglo en orden inverso |

### Complejidad Espacial

- **Espacio Auxiliar**: O() - Ordenamiento in-place
- **Espacio Total**: O(n) - Tamaño del arreglo de entrada

### Resultados de Benchmark

Comparativa de rendimiento con el `sorted()` nativo de Python:

```
┌─────────┬──────────────────┬────────────────────┬──────────────────────┐
│ Tamaño  │ GeoFlux (Random) │ GeoFlux (Ordenado) │ Python sorted()      │
├─────────┼──────────────────┼────────────────────┼──────────────────────┤
│    00  │   0.00088s      │   0.0000s        │   0.000008s          │
│    500  │   0.00669s      │   0.00009s        │   0.0000s          │
│  ,000  │   0.086s      │   0.00089s        │   0.000076s          │
│  ,000  │   0.0878s      │   0.00078s        │   0.00059s          │
│  5,000  │   0.55990s      │   0.000990s        │   0.0006s          │
└─────────┴──────────────────┴────────────────────┴──────────────────────┘
```

###  Observaciones

- ✅ **Excelente** para arreglos pequeños (n < 00) o parcialmente ordenados
- ⚠️ **Menos eficiente** que TimSort (Python nativo) para grandes conjuntos aleatorios
-  **Valor educativo** significativo para entender algoritmos de ordenamiento
-  **Ideal** para visualización debido a su naturaleza iterativa y visual

---

##  Visualización

Una de las características más destacadas de GeoFlux Sorter es su capacidad de visualización en tiempo real del proceso de ordenamiento.

###  Características de Visualización

La animación muestra:

-  **Estado del Arreglo**: Barras que representan cada elemento
-  **Grupos Identificados**: Clusters de elementos similares resaltados
-  **Migración de Grupos**: Movimiento de grupos completos
-  **Progreso**: Indicador del estado del ordenamiento

### Personalización

```python
from geoflux_sorter import create_geoflux_animation

create_geoflux_animation(
    initial_data,           # Lista de datos a ordenar
    interval=00,           # Intervalo entre frames (ms)
    save_to_file=None       # Ruta para guardar (requiere ffmpeg)
)
```

### Ejemplo de Visualización

```python
import random
from geoflux_sorter import create_geoflux_animation

# Generar datos aleatorios
datos = random.sample(range(, 0), 0)

# Crear animación con actualización cada 00ms
animacion = create_geoflux_animation(datos, interval=00)

# La animación se mostrará automáticamente
```

**Nota**: Para guardar animaciones como video se requiere `ffmpeg` instalado en el sistema.

---

##  Estructura del Proyecto

```
geoflux_sorter_project/
│
├──  geoflux_sorter/          # Paquete principal
│   ├── __init__.py             # Exporta la API pública
│   ├── algorithm.py            # Implementación del algoritmo GeoFlux Sort
│   └── animator.py             # Sistema de visualización y animación
│
├──  examples/                # Ejemplos de uso
│   ├── run_sort_example.py     # Demostración básica del algoritmo
│   ├── run_animation_example.py # Ejemplo de visualización
│   └── benchmark_sort.py       # Comparativa de rendimiento
│
├──  tests/                   # Suite de pruebas
│   ├── test_algorithm.py       # Tests unitarios del algoritmo
│   ├── benchmark_compare.py    # Benchmarks comparativos
│   └── bottleneck_test.py      # Análisis de cuellos de botella
│
├──  README.md                # Esta documentación
├──  requirements.txt         # Dependencias del proyecto
└──  .gitignore              # Archivos ignorados por Git
```

### Módulos Principales

#### `geoflux_sorter/algorithm.py`

Contiene la implementación del algoritmo:

- `geoflux_sort(arr)`: Función principal de ordenamiento
- `geoflux_sort_generator(arr)`: Generador para seguimiento paso a paso

#### `geoflux_sorter/animator.py`

Maneja la visualización:

- `create_geoflux_animation(data, interval, save_to_file)`: Crea animaciones
- Soporte para exportar a video (con ffmpeg)

---

##  Contribuir

¡Las contribuciones son bienvenidas! Este proyecto está abierto a mejoras y nuevas ideas.

### Cómo Contribuir

.  **Fork** el proyecto
.  **Crea una rama** para tu feature
   ```bash
   git checkout -b feature/nueva-caracteristica
   ```
. ✍️ **Realiza tus cambios** y haz commit
   ```bash
   git commit -m 'Añadir nueva característica'
   ```
.  **Push** a tu rama
   ```bash
   git push origin feature/nueva-caracteristica
   ```
5.  **Abre un Pull Request**

###  Áreas de Mejora

Contribuciones sugeridas:

- [ ] **Optimización del Umbral**: Algoritmos más sofisticados para determinar similitud
- [ ] **Análisis de Datos**: Caracterización automática del tipo de distribución
- [ ] **Visualización Mejorada**: Más estilos y opciones de renderizado
- [ ] **Tests Adicionales**: Casos edge y propiedades matemáticas
- [ ] **Documentación**: Más ejemplos y tutoriales
- [ ] **Paralelización**: Implementación concurrente para grandes datasets
- [ ] **Implementación en Otros Lenguajes**: C++, Rust, JavaScript, etc.

###  Código de Conducta

- Se respetuoso y constructivo
- Escribe código limpio y documentado
- Incluye tests para nuevas funcionalidades
- Actualiza la documentación según sea necesario

---

##  Licencia

Este proyecto está licenciado bajo la **MIT License**.

```
MIT License

Copyright (c) 05 Andrés Azcona

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

##  Agradecimientos

- Inspirado en patrones naturales de migración
- Construido con Python y Matplotlib
- Gracias a la comunidad de código abierto

---

<div align="center">

**⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub**

Desarrollado con ❤️ por [Andrés Azcona](https://github.com/andresazcona)

</div>