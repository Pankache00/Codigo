# Ordenamiento, Limpieza Avanzada y Visualización Básica
# Objetivos
# Aprender a ordenar datos en un DataFrame.
# Realizar operaciones de limpieza avanzada.
# Introducir la visualización básica de datos usando Pandas.

import pandas as pd
import matplotlib.pyplot as plt

# Ordenamiento de datos

# Crear un DataFrame simple
data = {
    'Producto': ['Manzana', 'Pera', 'Naranja', 'Manzana', 'Naranja'],
    'Ventas': [15, 20, 10, 25, 30]
}
df = pd.DataFrame(data)

# Ordenar por la columna 'Ventas' en orden ascendente
ordenado = df.sort_values(by='Ventas')
print(f"Ordenado por Ventas Ascendentes: \n{ordenado}")

# Ordenar por 'Ventas' en orden descendente
ordenado_desc = df.sort_values(by='Ventas', ascending=False)
print(f"\nOrdenado por Ventas Descendentes: \n{ordenado_desc} ")

# Limpieza Avanzada
# A veces un dataset tiene datos repetidos, y puedes eliminarlos con drop_duplicates().
df_sin_duplicados = df.drop_duplicates()
print(f"\n Sin duplicados: \n{df_sin_duplicados}")

# Reemplazar Valores
# Puedes reemplazar valores específicos en el DataFrame con replace().
# Reemplazar valores en la columna 'Producto'
df_reemplazar = df.replace({'Manzana': 'Apple'})
print(f"\n Reemplazo de Producto 'Manzana' por 'Apple': \n{df_reemplazar}")

# Eliminar Filas o Columnas
# Usa drop() para eliminar filas o columnas.
df_sin_columna = df.drop(columns=['Ventas'])
print(f"\n Sin columna 'Ventas: \n{df_sin_columna}")

# Ejemplo de Gráfica de Barras
# Pandas tiene métodos integrados para visualización básica utilizando Matplotlib.

# Crear un gráfico de barras con los datos de Ventas
plt.figure()  # Crear una nueva figura para el gráfico
df.groupby('Producto')['Ventas'].sum().plot(
    kind='bar', title='Ventas por Producto')
plt.show()  # Mostrar el gráfico de barras

# Crear un gráfico de líneas
plt.figure()  # Crear una nueva figura para el gráfico
df.groupby('Producto')['Ventas'].sum().plot(
    kind='line', title='Tendencia de Ventas')
plt.show()  # Mostrar el gráfico de barras
