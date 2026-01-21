# Tarea: Análisis y Visualización de Datos con Pandas y Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Producto': ['Manzana', 'Pera', 'Naranja', 'Manzana', 'Naranja', 'Durazno', 'Pera'],
    'Ventas': [15, 20, 10, 25, 30, 18, 22],
    'Categoría': ['Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta']
}

df = pd.DataFrame(data)

# Ordenar el DataFrame por la columna 'Ventas' en orden descendete
orden_descente = df.sort_values(by='Ventas', ascending=False)
print(f"Orden de Ventas Descendente: \n{orden_descente}")

# Eliminar duplicados y mostrar resultado
eliminar_duplicados = df.drop_duplicates()
print(f"\n Sin duplicados: \n{eliminar_duplicados}")

# Agrupar por Producto y calculando suma, media y conteo de registros de 'Ventas'
agrupar = df.groupby('Producto')['Ventas'].agg(['sum', 'mean', 'count'])
print(f"\n Estadísticas agrupadas por productos: \n{agrupar}")

# Reemplazar valores
df_reemplazar = df.replace({'Manzana': 'Apple'})
print(f"\n Cambiar Manzana por Apple: \n{df_reemplazar}")

# Volumen total de ventas, agrupadas por productos y sumar las ventas
ventas_agrupadas = df.groupby('Producto')['Ventas'].sum().reset_index()
print(f"\n El volumen de ventas es: \n{ventas_agrupadas}")

# Visualización de Datos

# Calcular la suma acumulada de Ventas para cada Producto
df['VentasAcumuladas'] = df.groupby('Producto')['Ventas'].cumsum()

# Gráfico de Líneas con las ventas acumuladas
plt.figure()
df.groupby('Producto')['VentasAcumuladas'].max().plot(
    kind='line', title='Tendencia Acumulada de Ventas', xlabel='Producto', ylabel='Ventas Acumuladas')
plt.show()

# Gráfico de Barras
plt.figure()
df.groupby('Producto')['Ventas'].sum().plot(
    kind='bar', title='Ventas por Producto', xlabel='Producto', ylabel='Ventas')
plt.show()
