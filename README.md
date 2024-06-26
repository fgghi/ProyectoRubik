### Proyecto Rubik

## 1. Autor
**Nombre completo:** Sergio Bustamante

## 2. ¿Que es?

- Este proyecto implementa un solucionador de cubos de Rubik utilizando el algoritmo de búsqueda IDA* (Iterative Deepening A*) en Python. También incluye una visualización del cubo utilizando la librería Matplotlib.

#### 3. Requerimientos del Entorno

- Python 3.x
- NumPy
- Matplotlib

#### 4. Uso

1. **Formato de codificación para cargar el estado de un cubo desde el archivo de texto:**
   - El archivo de texto debe contener la codificación del estado del cubo de Rubik. Cada línea del archivo representa una fila del cubo. Por ejemplo, una fila del cubo se puede codificar como "wwg".
   Ejemplo:
   "www
    www
    www
    ooo
    ooo
    ooo
    yyy
    yyy
    yyy
    rrr
    rrr
    rrr
    bbb
    bbb
    bbb
    ggg
    ggg
    ggg"

2. **Instrucciones para ejecutar el programa:**
   - Coloca el archivo de texto cube.txt.
   - Ejecuta el script Python.
   - El programa imprimirá el estado inicial del cubo cargado desde el archivo de texto, luego calculará una solución utilizando el algoritmo IDA*, y finalmente imprimirá la solución paso a paso.
   - Además, el programa visualizará el cubo de Rubik utilizando Matplotlib.

#### 5. Diseño e Implementación

- **Modelo del Problema:** El problema se modela como un cubo de Rubik  3x3. Cada cara del cubo tiene un color, y el objetivo es encontrar una secuencia de movimientos que resuelva el cubo, es decir, que lleve todas las caras a tener un solo color por cara.

- **Algoritmo y Heurística:** Se utiliza el algoritmo IDA* junto con una heurística basada en la distancia Manhattan entre el estado actual del cubo y el estado objetivo. Esta heurística es admisible y consistente, garantizando la optimalidad del algoritmo.

    **IDA (Iterative Deepening A*):**
        El IDA* es una variante del algoritmo A* que utiliza búsqueda en profundidad con un límite iterativo para encontrar la solución óptima en un espacio de búsqueda con complejidad exponencial. Utiliza una heurística para estimar el costo restante desde un estado dado hasta el estado objetivo y realiza una búsqueda exhaustiva dentro de un límite de profundidad iterativo en este caso 10.

    **¿Porque se usa?**
        El IDA* se elige porque garantiza encontrar la solución óptima en un espacio de búsqueda exponencial como el cubo de Rubik. Utiliza menos memoria que el A* convencional al mantener solo un camino en la pila de recursión, lo que lo hace adecuado para problemas con grandes espacios de estados como el cubo de Rubik.

    **Heurística de Distancia Manhattan:**
        La heurística de la distancia Manhattan calcula la suma de las distancias Manhattan entre las posiciones actuales de cada cubo entre el cubo y sus posiciones objetivo. La distancia Manhattan es la suma de las diferencias absolutas de las coordenadas en cada dimensión. En el caso del cubo de Rubik, se calcula la distancia entre la posición actual de cada pieza del cubo y su posición objetivo.

    **¿Porque se usa?**
        La distancia Manhattan se utiliza como heurística porque es admisible y consistente en el contexto del cubo de Rubik. Lo usamos ya que es consistente, lo que significa que la diferencia de la heurística entre dos estados adyacentes es menor o igual al costo real de llegar de un estado al otro. Esto garantiza la optimizacion del algoritmo IDA* cuando se utiliza esta heurística.

#### Trabajo Futuro

- Mejorar el tiempo que le toma al proyecto terminar.
- Terminar el proceso de graficacion en matplotlib, actualmente debido a ser una matriz 3x3 solo puede llevar 3 colores y no grafica de forma satisfactoria.
- Optimizar la visualización del cubo para mejorar la experiencia del usuario.
- Buscar representar el cubo en un espacio 3d y mostrar los movimientos a hacer en una grabacion repetible o gif (para ahorrar espacio).
