# Clase agrupaciones, agregaciones y combinación de DataFrame

import pandas as pd

# Ejemplo hipotético de un DataFrame
data = {
    'Producto': ['Manzana', 'Pera', 'Manzana', 'Naranja', 'Pera', 'Naranja'],
    'Categoría': ['Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta'],
    'Ventas': [10, 20, 15, 5, 12, 25]
}

df = pd.DataFrame(data)

# Agrupar por 'Producto' y calcular el total de ventas
resumen = df.groupby('Producto')['Ventas'].sum()
print(f"Ventas totales por productos: {resumen}")

# Agregación múltiples
# En caso de ver varias estadísticas a la vez (ejemplo: suma y promedio)
resumen_multiple = df.groupby('Producto')['Ventas'].agg([
    'sum', 'mean', 'count'])
print(f"Resumen Múltiple: {resumen_multiple}")

# Unir múltiples DataFrame
# merge() Simula un “join” de SQL: combinas dos DataFrames en base a una columna común (llave primaria).
clientes = pd.DataFrame({
    'IdCliente': [1, 2, 3],
    'Nombre': ['Juan', 'María', 'Pedro']
})

pedidos = pd.DataFrame({
    'IdPedido': [101, 102, 103],
    'IdCliente': [1, 2, 1],
    'Monto': [50, 100, 70]
})

# On='IdCliente" indica que la unión se hace usando la columna IdCliente que existe en ambos DataFrame
df_merged = pd.merge(pedidos, clientes, on='IdCliente')
print(f"Pedidos con información de cliente: {df_merged}")

# concat() Une DataFrames uno debajo de otro (apilamiento vertical) o lado a lado (apilamiento horizontal, si configuras axis=1).
df_a = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df_b = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

df_concat = pd.concat([df_a, df_b])  # Une verticalmente
print(f"Concatenación Vertical: {df_concat}")
