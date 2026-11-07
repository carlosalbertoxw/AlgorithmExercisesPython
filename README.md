# AlgorithmExercisesPython

[![Tests](https://github.com/carlosalbertoxw/AlgorithmExercisesPython/actions/workflows/tests.yml/badge.svg)](https://github.com/carlosalbertoxw/AlgorithmExercisesPython/actions/workflows/tests.yml)

Este repositorio contiene una colección de ejercicios de algoritmos resueltos en Python. Está diseñado para practicar lógica de programación, estructuras de datos y técnicas de resolución de problemas.

Los ejercicios están agrupados por categoría (siguiendo los temas de [NeetCode](https://neetcode.io/roadmap)), y cada uno vive en su propia carpeta con la solución y sus pruebas unitarias (pytest). Los ejemplos `>>>` de los docstrings también se ejecutan como pruebas (doctests).

## Estructura

```
.
├── .github/
│   ├── workflows/tests.yml        # CI: ruff + pytest en cada push/PR
│   └── dependabot.yml             # Actualizaciones automáticas de dependencias
├── exercises/                     # Paquete Python con todos los ejercicios
│   ├── arrays_hashing/            # Categoría
│   │   └── two_sum/               # Ejercicio
│   │       ├── two_sum.py         # Solución
│   │       └── test_two_sum.py    # Pruebas
│   ├── stacks/
│   │   └── valid_parentheses/
│   │       ├── valid_parentheses.py
│   │       └── test_valid_parentheses.py
│   └── common/                    # Código compartido entre ejercicios
│       └── structures.py          # ListNode, TreeNode
├── pyproject.toml                 # Dependencias de desarrollo y configuración de pytest/ruff
└── README.md
```

Cada carpeta dentro de `exercises/` lleva un `__init__.py` (omitidos en el árbol): `exercises` es un paquete Python, lo que permite compartir código entre ejercicios y evita colisiones de nombres al correr pytest.

## Ejercicios

### Arrays y Hashing

| Ejercicio | Problema | Técnica | Complejidad |
|---|---|---|---|
| [two_sum](exercises/arrays_hashing/two_sum/two_sum.py) | [Two Sum (LeetCode #1)](https://leetcode.com/problems/two-sum/) | Hash map en una pasada | O(n) tiempo, O(n) espacio |

### Stacks (pilas)

| Ejercicio | Problema | Técnica | Complejidad |
|---|---|---|---|
| [valid_parentheses](exercises/stacks/valid_parentheses/valid_parentheses.py) | [Valid Parentheses (LeetCode #20)](https://leetcode.com/problems/valid-parentheses/) | Pila (stack) | O(n) tiempo, O(n) espacio |

## Correr las pruebas

### Con Docker (sin instalar Python)

Desde la raíz del repo:

```bash
docker run --rm -v "$PWD:/app" -w /app python:3.14 sh -c "pip install -q --group dev && pytest"
```

En PowerShell (Windows):

```powershell
docker run --rm -v "${PWD}:/app" -w /app python:3.14 sh -c "pip install -q --group dev && pytest"
```

### Con Python local

Requiere Python 3.12+ y pip 25.1+ (para `--group`).

```bash
pip install --group dev
pytest              # pruebas + doctests
ruff check .        # lint
ruff format .       # formato
```

`pyproject.toml` ya apunta pytest a la carpeta `exercises/` y activa los doctests, así que basta con ejecutar `pytest` desde la raíz.

## Agregar un nuevo ejercicio

1. Elige la categoría en `exercises/` que corresponda a la técnica del problema (o crea una nueva si no existe). Categorías sugeridas, siguiendo los temas clásicos de LeetCode/NeetCode:

   `arrays_hashing` · `two_pointers` · `sliding_window` · `stacks` · `binary_search` · `linked_lists` · `trees` · `heaps` · `backtracking` · `graphs` · `dynamic_programming` · `greedy` · `intervals` · `math_geometry` · `bit_manipulation`

2. Dentro de la categoría, crea una carpeta con el nombre del problema, por ejemplo `exercises/two_pointers/valid_palindrome/`. Agrega un `__init__.py` vacío a la carpeta del ejercicio (y a la categoría, si es nueva).
3. Crea la solución (`valid_palindrome.py`) con un docstring que indique el problema, la técnica usada, su complejidad y un ejemplo `>>>`.
4. Crea las pruebas en un archivo `test_valid_palindrome.py` usando el import absoluto desde el paquete y `pytest.mark.parametrize` para agrupar casos:

   ```python
   import pytest

   from exercises.two_pointers.valid_palindrome.valid_palindrome import is_palindrome


   @pytest.mark.parametrize("s", ["anita lava la tina", "oso"])
   def test_palindromes(s: str) -> None:
       assert is_palindrome(s)
   ```

   Si el ejercicio usa listas enlazadas o árboles, importa las estructuras compartidas en lugar de redefinirlas (ambas tienen `from_list` para construirlas en los tests):

   ```python
   from exercises.common.structures import ListNode, TreeNode
   ```

5. Corre `pytest` y `ruff check .` desde la raíz para verificar, y agrega el ejercicio a la tabla de su categoría en este README (crea la sección si es una categoría nueva). El CI de GitHub Actions correrá lint y pruebas automáticamente en cada push.

## Licencia

[MIT](LICENSE)
