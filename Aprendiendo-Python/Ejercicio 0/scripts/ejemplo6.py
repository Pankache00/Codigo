# Ejercicio Integrador: Análisis de Ventas
# Objetivo
# Realizar un análisis completo de un conjunto de datos ficticio que simula registros de ventas. Aplicaremos técnicas como manipulación, agrupación, filtrado y visualización.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Producto': ['Manzana', 'Pera', 'Naranja', 'Manzana', 'Naranja', 'Durazno', 'Pera', 'Manzana', 'Naranja', 'Pera'],
    'Ventas': [15, 20, 10, 25, 30, 18, 22, 15, 40, 25],
    'Categoría': ['Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta'],
    'Fecha': ['2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09']
}

df = pd.DataFrame(data)

orden_descendente = df.sort_values(by='Ventas', ascending=False)
print(f"El orden descendente de Ventas es: \n{orden_descendente}")

eliminar_duplicados = df.drop_duplicates(subset='Producto')
print(f"\nDataFrame original: \n{df}")
print(f"\nProductos duplicados eliminados, tabla actualizada: \n{
      eliminar_duplicados}")

ventas_agrupadas = df.groupby('Producto')['Ventas'].agg([
    'sum', 'mean', 'count'])
print(f"\n Estadística agrupada por Productos: \n{ventas_agrupadas}")

filtro = df[df['Ventas'] > 20]
print(f"\n Las ventas mayores a 20 son: \n{filtro}")

# Convertir la columna 'Fecha' al formato datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Calcular las Ventas Acumuladas por Producto
df['VentasAcumuladas'] = df.groupby('Producto')['Ventas'].cumsum()

# Filtrar las ventas por fecha... Ventas realizadas después del 2024-01-05
ventas_despues = df[df['Fecha'] > '2024-01-05']
print(f"\nVentas realizadas después del 2024-01-05: \n{ventas_despues}")

# Gráfico de Barras: Ventas Totales por Producto
plt.figure(figsize=(8, 6))
df.groupby('Producto')['Ventas'].sum().plot(
    kind='bar', title='Ventas Totales por Producto', xlabel='Producto', ylabel='Ventas Totales', color='skyblue'
)
plt.show()

# Gráfico de Líneas: Tendencia Acumulada de Ventas por Fecha
plt.figure(figsize=(8, 6))
for producto in df['Producto'].unique():
    data_producto = df[df['Producto'] == producto]
    plt.plot(data_producto['Fecha'],
             data_producto['VentasAcumuladas'], label=producto)

plt.title('Tendencia Acumulada de Ventas por Fecha')
plt.xlabel('Fecha')
plt.ylabel('Ventas Acumuladas')
plt.legend(title='Producto')
plt.grid(True)
plt.show()
