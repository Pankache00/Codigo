# Portafolio de Ciencia de Datos

Este portafolio documenta mi proceso de aprendizaje en Python, Pandas y otras herramientas para el análisis de datos. En él encontrarás ejemplos prácticos con datasets reales y sintéticos, mostrando paso a paso cómo importar datos, explorar, limpiar, filtrar, y realizar análisis básicos.

---

## 🚀 **Estructura del Proyecto**

La estructura básica del portafolio es la siguiente:

- 📂 **data/**: Contiene los datasets (ej. `iris.csv`, `tips.csv`, `ventas.csv`) usados en los ejemplos.
- 📂 **notebooks/**: Aquí se agregarán cuadernos Jupyter (`.ipynb`) con análisis interactivos.
- 📂 **scripts/**: Archivos `.py` con el código fuente de cada ejemplo.
- 📄 **README.md**: Describe el objetivo del portafolio, la organización, y las instrucciones para cada ejemplo.

---

## 📚 **Ejemplos Incluidos**

1. [Ejemplo 1: Creación y Exploración de DataFrame](#ejemplo-1)
2. [Ejemplo 2: Operaciones con Series](#ejemplo-2)
3. [Ejemplo 3: Exploración de Dataset Real](#ejemplo-3)
4. [Ejemplo 4: Manejo de Valores Faltantes](#ejemplo-4)
5. [Ejemplo 5: Análisis y Visualización de Ventas](#ejemplo-5)
6. [Ejemplo 6: Ejercicio Integrador - Análisis de Ventas](#ejemplo-6)

---

### Ejemplo 1: Creación y Exploración de DataFrame

📁 **Archivo:** `scripts/ejemplo_1.py`

🔍 **Descripción:**

- Crea un `DataFrame` a partir de un diccionario.
- Imprime el DataFrame completo.
- Calcula la media de la columna `'Edad'`.
- Utiliza `df.describe()` para obtener estadísticas descriptivas.

🎯 **Objetivo:**  
Introducir la creación y manipulación básica de un DataFrame, así como la obtención de estadísticas descriptivas iniciales.

💻 **Ejecución:**

```bash
python scripts/ejemplo_1.py
```

---

### Ejemplo 2: Operaciones con Series

📁 **Archivo:** `scripts/ejemplo_2.py`

🔍 **Descripción:**

- Crea una Serie a partir de una lista.
- Calcula el valor máximo, mínimo y la media de la Serie.
- Introduce operaciones básicas con Series en Pandas.

🎯 **Objetivo:**  
Familiarizarse con las Series en Pandas y realizar operaciones básicas de análisis de datos.

💻 **Ejecución:**

```bash
python scripts/ejemplo_2.py
```

---

### Ejemplo 3: Exploración de Dataset Real

📁 **Archivo:** `scripts/ejemplo_3.py`

🔍 **Descripción:**

- Carga el dataset `iris.csv`.
- Imprime las primeras 10 filas con `df.head(10)`.
- Obtiene información general con `df.info()`.
- Calcula estadísticas descriptivas con `df.describe()`.

🎯 **Objetivo:**  
Explorar un dataset real y aprender a inspeccionar su estructura y contenido con métodos de Pandas.

💻 **Ejecución:**

```bash
python scripts/ejemplo_3.py
```

---

### Ejemplo 4: Manejo de Valores Faltantes

📁 **Archivo:** `scripts/ejemplo_4.py`

🔍 **Descripción:**

- Trabaja con el dataset `tips.csv`.
- Filtra filas según condiciones específicas.
- Calcula valores faltantes con `df.isna().sum()`.
- Elimina valores faltantes con `df.dropna()`.

🎯 **Objetivo:**  
Aprender a manejar valores faltantes y filtrar información en un DataFrame.

💻 **Ejecución:**

```bash
python scripts/ejemplo_4.py
```

---

### Ejemplo 5: Análisis y Visualización de Ventas

📁 **Archivo:** `scripts/ejemplo_5.py`

🔍 **Descripción:**

Este ejemplo analiza un conjunto ficticio de productos y ventas. Incluye:

- Ordenamiento por ventas en orden descendente.
- Eliminación de duplicados.
- Agrupación de datos con cálculos de suma, media y conteo.
- Reemplazo de valores específicos en el DataFrame.
- Visualización con gráficos:
  - **Gráfico de Barras**: Ventas totales por producto.
  - **Gráfico de Líneas**: Tendencia acumulada de ventas por producto.

🎯 **Objetivo:**  
Explorar técnicas básicas de análisis y visualización de datos usando Pandas y Matplotlib.

💻 **Ejecución:**

```bash
python scripts/ejemplo_5.py
```

**Nota:**  
Los gráficos se muestran en pantalla, pero no se guardan como archivos de imagen.

---

### Ejemplo 6: Ejercicio Integrador - Análisis de Ventas

📁 **Archivo:** `scripts/ejemplo_6.py`

🔍 **Descripción:**

Este ejercicio integrador realiza un análisis completo de un conjunto ficticio de datos de ventas. Incluye:

- Manipulación de datos: ordenamiento, eliminación de duplicados, filtrado.
- Agrupación y estadísticas: suma, media, y conteo por producto.
- Análisis temporal: conversión de fechas y cálculo de ventas acumuladas.
- Visualización: gráficos de barras y líneas para interpretar las tendencias.

🎯 **Objetivo:**  
Consolidar conceptos básicos y avanzados de análisis de datos con Pandas y visualización con Matplotlib.

💻 **Ejecución:**

```bash
python scripts/ejemplo_6.py
```

---

## 🌟 **Nota Final**

A medida que continúe mi aprendizaje, se agregarán más ejemplos con datasets variados, análisis más complejos (como agrupamiento, fusiones de DataFrames, visualizaciones, y técnicas de limpieza avanzadas), así como el uso de otras librerías del ecosistema de Python para la ciencia de datos.

¡Gracias por revisar este portafolio! 😊
