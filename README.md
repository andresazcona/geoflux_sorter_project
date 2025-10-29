# GeoFlux Sorter

<div align="center">

**A bidirectional sorting algorithm with group migration and interactive visualization**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/andresazcona/geoflux_sorter_project)

</div>

---

## Table of Contents

- [Description](#description)
- [Publications](#publications)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Examples](#examples)
- [The Algorithm](#the-algorithm)
- [Performance Analysis](#performance-analysis)
- [Visualization](#visualization)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Description

**GeoFlux Sorter** is an experimental sorting algorithm that implements a bidirectional approach based on **group migration**. Inspired by natural migration patterns, the algorithm identifies clusters of similar elements and moves them as cohesive units toward their correct positions.

### What Makes It Unique?

- **Group Sorting**: Identifies and moves sets of similar elements as units, not element by element
- **Bidirectional Flow**: Alternates between migrating small elements to the left and large elements to the right
- **Adaptive Threshold**: Automatically adjusts the definition of "similarity" based on data characteristics
- **Integrated Visualization**: Allows observation of the sorting process in real-time

---
## Publications

- Technical article: "GeoFlux Sort: A bidirectional adaptive algorithm for natural data ordering" — Medium.
  Link: https://medium.com/@andresazcona/geoflux-sort-a-bidirectional-adaptive-algorithm-for-natural-data-ordering-5dc8d625e0fd

---

## Key Features

| Feature | Description |
|---------|-------------|
| **In-Place Sorting** | Modifies the array directly, without additional memory |
| **Interactive Visualization** | Step-by-step animations of the sorting process |
| **Smart Optimizations** | Detection of sorted sections and base cases |
| **Test Suite** | Complete unit tests and benchmarks |
| **Performance Analysis** | Comparisons with Python standard algorithms |
| **Customizable** | Control over animation speed and style |

---

## Installation

### Prerequisites

- **Python 3.6+** installed on your system
- **pip** (Python package manager)

### Installation Steps

**1. Clone the repository**
```bash
git clone https://github.com/andresazcona/geoflux_sorter_project.git
cd geoflux_sorter_project
```

**2. Create a virtual environment** (recommended)
```bash
python -m venv venv
```

**3. Activate the virtual environment**
```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate.bat

# Unix/MacOS
source venv/bin/activate
```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

Ready to use!

---

## Quick Start

### Basic Sorting

```python
from geoflux_sorter import geoflux_sort

# Create an unsorted list
data = [64, 34, 25, 12, 22, 11, 90]

# Sort in-place
geoflux_sort(data)

print(data)  # [11, 12, 22, 25, 34, 64, 90]
```

### Step-by-Step Visualization

```python
from geoflux_sorter import geoflux_sort_generator

data = [5, 2, 9, 1, 5, 6]

# Observe each step of the algorithm
for step in geoflux_sort_generator(data):
    print(f"{step['array']} - {step['status']}")
```

### Create Animation

```python
from geoflux_sorter import create_geoflux_animation
import random

# Generate random data
data = random.sample(range(1, 51), 20)

# Create and display animation
animation = create_geoflux_animation(data, interval=200)
```

---

## Examples

The project includes ready-to-run examples in the `examples/` folder:

| File | Description |
|------|-------------|
| `run_sort_example.py` | Demonstrates sorting with various test cases |
| `run_animation_example.py` | Creates an animated visualization of the algorithm |
| `benchmark_sort.py` | Compares performance with other algorithms |

### Running Examples

```bash
# Basic example
python examples/run_sort_example.py

# Animated visualization
python examples/run_animation_example.py

# Performance benchmark
python examples/benchmark_sort.py
```

---

## The Algorithm

### How It Works

GeoFlux Sort implements a bidirectional sorting process inspired by natural migrations:

#### Main Cycle

The algorithm performs complete cycles until no more changes are required:

1. **Group Detection**: Identifies clusters of elements with similar values
2. **Ascending Flow**: Migrates groups of small values to the left
3. **Descending Flow**: Migrates groups of large values to the right
4. **Repeat**: Continues until the array is completely sorted

#### Key Optimizations

- **Adaptive Threshold**: Automatically calculates the similarity threshold (5% of range)
- **Early Detection**: Identifies already sorted arrays in O(n)
- **Insertion Sort for Small Cases**: Uses more efficient algorithm for n ≤ 20
- **Skip Sorted Sections**: Avoids processing already sorted segments
- **Group Size Limit**: Prevents excessively large groups

### Pseudocode

```plaintext
FUNCTION GeoFluxSort(array):
    n ← length(array)
    
    // Base cases and optimizations
    IF n ≤ 1 THEN RETURN
    IF array_is_sorted(array) THEN RETURN
    IF n ≤ 20 THEN insertion_sort(array); RETURN
    
    // Calculate adaptive threshold
    range ← maximum(array) - minimum(array)
    similarity_threshold ← range × 0.05
    
    elements_moved ← TRUE
    
    WHILE elements_moved DO:
        elements_moved ← FALSE
        
        // Detect already sorted sections
        sorted_start ← detect_sorted_start(array)
        sorted_end ← detect_sorted_end(array)
        
        // === ASCENDING FLOW ===
        i ← sorted_start + 1
        WHILE i < sorted_end DO:
            // Identify group of similar elements
            group ← identify_group(array, i, similarity_threshold)
            
            // If group should migrate left
            IF array[group.start] < array[group.start - 1] THEN:
                group_values ← sort(array[group.start:group.end])
                insertion_point ← find_insertion_point(array, group_values[0])
                
                // Move group to new position
                insert_group(array, group_values, insertion_point)
                elements_moved ← TRUE
            END IF
            
            i ← group.end + 1
        END WHILE
        
        // === DESCENDING FLOW ===
        i ← sorted_end - 1
        WHILE i > sorted_start DO:
            // Identify group of similar elements
            group ← identify_reverse_group(array, i, similarity_threshold)
            
            // If group should migrate right
            IF array[group.start] > array[group.start + 1] THEN:
                group_values ← sort(array[group.start:group.end])
                insertion_point ← find_right_insertion_point(array, group_values[-1])
                
                // Move group to new position
                insert_group(array, group_values, insertion_point)
                elements_moved ← TRUE
            END IF
            
            i ← group.start - 1
        END WHILE
    END WHILE
END FUNCTION
```

### Comparison with Other Algorithms

GeoFlux Sort combines features from several classic algorithms:

| Algorithm | Influence on GeoFlux |
|-----------|---------------------|
| **Insertion Sort** | Insertion of groups in correct positions |
| **Bubble Sort** | Bidirectional flow of elements |
| **Cocktail Sort** | Alternating passes in both directions |
| **Bucket Sort** | Grouping of similar elements |

**Main Advantage**: Improved efficiency on data with natural clusters of similar values.

---

## Performance Analysis

### Time Complexity

| Scenario | Complexity | Description |
|----------|------------|-------------|
| **Best Case** | O(n) | Already sorted array |
| **Average Case** | O(n²) | Random data |
| **Worst Case** | O(n²) | Array in reverse order |

### Space Complexity

- **Auxiliary Space**: O(1) - In-place sorting
- **Total Space**: O(n) - Size of input array

### Benchmark Results

Performance comparison with Python's native `sorted()`:

```
┌─────────┬──────────────────┬────────────────────┬──────────────────────┐
│ Size    │ GeoFlux (Random) │ GeoFlux (Sorted)   │ Python sorted()      │
├─────────┼──────────────────┼────────────────────┼──────────────────────┤
│    100  │   0.000288s      │   0.000021s        │   0.000008s          │
│    500  │   0.004669s      │   0.000094s        │   0.000032s          │
│  1,000  │   0.021862s      │   0.000189s        │   0.000076s          │
│  2,000  │   0.087482s      │   0.000378s        │   0.000159s          │
│  5,000  │   0.554990s      │   0.000990s        │   0.000426s          │
└─────────┴──────────────────┴────────────────────┴──────────────────────┘
```

### Observations

- **Excellent** for small arrays (n < 100) or partially sorted
- **Less efficient** than TimSort (Python native) for large random sets
- **Educational value** significant for understanding sorting algorithms
- **Ideal** for visualization due to its iterative and visual nature

---

## Visualization

One of the standout features of GeoFlux Sorter is its real-time visualization capability of the sorting process.

### Visualization Features

The animation shows:

- **Array State**: Bars representing each element
- **Identified Groups**: Clusters of similar elements highlighted
- **Group Migration**: Movement of complete groups
- **Progress**: Indicator of sorting status

### Customization

```python
from geoflux_sorter import create_geoflux_animation

create_geoflux_animation(
    initial_data,           # List of data to sort
    interval=300,           # Interval between frames (ms)
    save_to_file=None       # Path to save (requires ffmpeg)
)
```

### Visualization Example

```python
import random
from geoflux_sorter import create_geoflux_animation

# Generate random data
data = random.sample(range(1, 101), 30)

# Create animation with update every 200ms
animation = create_geoflux_animation(data, interval=200)

# Animation will display automatically
```

**Note**: To save animations as video, `ffmpeg` must be installed on the system.

---

## Project Structure

```
geoflux_sorter_project/
│
├── geoflux_sorter/          # Main package
│   ├── __init__.py             # Exports public API
│   ├── algorithm.py            # GeoFlux Sort algorithm implementation
│   └── animator.py             # Visualization and animation system
│
├── examples/                # Usage examples
│   ├── run_sort_example.py     # Basic algorithm demonstration
│   ├── run_animation_example.py # Visualization example
│   └── benchmark_sort.py       # Performance comparison
│
├── tests/                   # Test suite
│   ├── test_algorithm.py       # Algorithm unit tests
│   ├── benchmark_compare.py    # Comparative benchmarks
│   └── bottleneck_test.py      # Bottleneck analysis
│
├── README.md                # This documentation
├── requirements.txt         # Project dependencies
└── .gitignore              # Files ignored by Git
```

### Main Modules

#### `geoflux_sorter/algorithm.py`

Contains the algorithm implementation:

- `geoflux_sort(arr)`: Main sorting function
- `geoflux_sort_generator(arr)`: Generator for step-by-step tracking

#### `geoflux_sorter/animator.py`

Handles visualization:

- `create_geoflux_animation(data, interval, save_to_file)`: Creates animations
- Support for exporting to video (with ffmpeg)

---

## Contributing

Contributions are welcome! This project is open to improvements and new ideas.

### How to Contribute

1. **Fork** the project
2. **Create a branch** for your feature
   ```bash
   git checkout -b feature/new-feature
   ```
3. **Make your changes** and commit
   ```bash
   git commit -m 'Add new feature'
   ```
4. **Push** to your branch
   ```bash
   git push origin feature/new-feature
   ```
5. **Open a Pull Request**

### Areas for Improvement

Suggested contributions:

- [ ] **Threshold Optimization**: More sophisticated algorithms for determining similarity
- [ ] **Data Analysis**: Automatic characterization of distribution type
- [ ] **Enhanced Visualization**: More styles and rendering options
- [ ] **Additional Tests**: Edge cases and mathematical properties
- [ ] **Documentation**: More examples and tutorials
- [ ] **Parallelization**: Concurrent implementation for large datasets
- [ ] **Implementation in Other Languages**: C++, Rust, JavaScript, etc.

### Code of Conduct

- Be respectful and constructive
- Write clean and documented code
- Include tests for new functionalities
- Update documentation as needed

---

## License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Andrés Azcona

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

## Acknowledgments

- Inspired by natural migration patterns
- Built with Python and Matplotlib
- Thanks to the open-source community

---

<div align="center">

**If you find this project useful, please consider giving it a star on GitHub**

Developed with love by [Andrés Azcona](https://github.com/andresazcona)

</div>