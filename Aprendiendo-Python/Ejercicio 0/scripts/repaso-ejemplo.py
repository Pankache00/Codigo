import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Producto': ['Laptop', 'Tablet', 'Smartphone', 'Laptop', 'Tablet', 'Smartphone', 'Laptop'],
    'Ventas': [1500, 800, 1200, 1800, 900, 1500, 2000],
    'Categoría': ['Electrónica', 'Electrónica', 'Electrónica', 'Electrónica', 'Electrónica', 'Electrónica', 'Electrónica'],
    'Fecha': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05', '2025-01-06', '2025-01-07']
}

df = pd.DataFrame(data)
print(df)

orden_descendente = df.sort_values(by='Ventas', ascending=False)
print(f"\nEl orden descendente de de ventas es: \n {orden_descendente}")

eliminar_duplicado = df.drop_duplicates(subset='Producto')
print(f"\nEliminado los Productos duplicados: \n {eliminar_duplicado}")

df['VentasAcumuladas'] = df.groupby('Producto')['Ventas'].cumsum()

df['Fecha'] = pd.to_datetime(df['Fecha'])

ventas_totales = df.groupby('Producto')['Ventas'].sum()
ventas_totales.plot(kind='bar', title='Ventas Totales por Producto', xlabel='Producto', ylabel='Ventas Totales', color='skyblue')
for idx, val in enumerate(ventas_totales):
    plt.text(idx, val, str(val), ha='center', va='bottom')


plt.figure(figsize=(10, 8))
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
