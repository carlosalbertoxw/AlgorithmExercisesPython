# AlgorithmExercisesPython

[![Tests](https://github.com/carlosalbertoxw/AlgorithmExercisesPython/actions/workflows/tests.yml/badge.svg)](https://github.com/carlosalbertoxw/AlgorithmExercisesPython/actions/workflows/tests.yml)

Este repositorio contiene una colección de ejercicios de algoritmos resueltos en Python. Está diseñado para practicar lógica de programación, estructuras de datos y técnicas de resolución de problemas.

Los ejercicios están agrupados por categoría (técnica o estructura de datos), y cada uno vive en su propia carpeta con la solución y sus pruebas unitarias (pytest).

## Estructura

```
.
├── .github/workflows/tests.yml    # CI: corre pytest en cada push/PR
├── ejercicios/                    # Paquete Python con todos los ejercicios
│   ├── arrays_hashing/            # Categoría
│   │   └── two_sum/               # Ejercicio
│   │       ├── two_sum.py         # Solución
│   │       └── test_two_sum.py    # Pruebas
│   ├── stacks/
│   │   └── is_valid/
│   │       ├── is_valid.py
│   │       └── test_is_valid.py
│   └── comun/                     # Código compartido entre ejercicios
│       └── estructuras.py         # ListNode, TreeNode
├── pyproject.toml                 # Configuración de pytest
└── README.md
```

Cada carpeta dentro de `ejercicios/` lleva un `__init__.py` (omitidos en el árbol): `ejercicios` es un paquete Python, lo que permite compartir código entre ejercicios y evita colisiones de nombres al correr pytest.

## Ejercicios

### Arrays y Hashing

| Ejercicio | Problema | Técnica | Complejidad |
|---|---|---|---|
| [two_sum](ejercicios/arrays_hashing/two_sum/two_sum.py) | [Two Sum (LeetCode #1)](https://leetcode.com/problems/two-sum/) | Hash map en una pasada | O(n) tiempo, O(n) espacio |

### Stacks (pilas)

| Ejercicio | Problema | Técnica | Complejidad |
|---|---|---|---|
| [is_valid](ejercicios/stacks/is_valid/is_valid.py) | [Valid Parentheses (LeetCode #20)](https://leetcode.com/problems/valid-parentheses/) | Pila (stack) | O(n) tiempo, O(n) espacio |

## Correr las pruebas

### Con Docker (sin instalar Python)

Desde la raíz del repo:

```bash
docker run --rm -v "$PWD:/app" -w /app python:3 sh -c "pip install -q pytest && pytest"
```

En PowerShell (Windows):

```powershell
docker run --rm -v "${PWD}:/app" -w /app python:3 sh -c "pip install -q pytest && pytest"
```

### Con Python local

Requiere Python 3.9+.

```bash
pip install pytest
pytest
```

`pyproject.toml` ya apunta pytest a la carpeta `ejercicios/`, así que basta con ejecutar `pytest` desde la raíz.

## Agregar un nuevo ejercicio

1. Elige la categoría en `ejercicios/` que corresponda a la técnica del problema (o crea una nueva si no existe). Categorías sugeridas, siguiendo los temas clásicos de LeetCode/NeetCode:

   `arrays_hashing` · `two_pointers` · `sliding_window` · `stacks` · `binary_search` · `linked_lists` · `trees` · `heaps` · `backtracking` · `graphs` · `dynamic_programming` · `greedy` · `intervals` · `math_geometry` · `bit_manipulation`

2. Dentro de la categoría, crea una carpeta con el nombre del ejercicio, por ejemplo `ejercicios/two_pointers/valid_palindrome/`. Si la categoría es nueva, agrega un `__init__.py` vacío tanto a la categoría como a la carpeta del ejercicio.
3. Crea la solución (`valid_palindrome.py`) con un docstring que indique el problema, la técnica usada y su complejidad.
4. Crea las pruebas en un archivo `test_valid_palindrome.py` usando el import absoluto desde el paquete:

   ```python
   from ejercicios.two_pointers.valid_palindrome.valid_palindrome import valid_palindrome

   def test_basico():
       assert valid_palindrome("anita lava la tina") == True
   ```

   Si el ejercicio usa listas enlazadas o árboles, importa las estructuras compartidas en lugar de redefinirlas:

   ```python
   from ejercicios.comun.estructuras import ListNode, TreeNode
   ```

5. Corre `pytest` desde la raíz para verificar, y agrega el ejercicio a la tabla de su categoría en este README (crea la sección si es una categoría nueva). El CI de GitHub Actions correrá las pruebas automáticamente en cada push.
