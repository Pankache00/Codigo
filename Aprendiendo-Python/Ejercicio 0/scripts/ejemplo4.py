import pandas as pd

# Cargamos los csv que se encuentran en "data"
df = pd.read_csv('data/ventas.csv')

# Agrupar el DataFrame por columna Producto
agrupar = df.groupby('Producto')['Ventas'].agg(['sum', 'mean', 'count'])
print("Estadísticas agrupadas por producto: ")
print(agrupar)

# Combinación de DataFrames con clientes.csv y pedidos.csv
df_clientes = pd.read_csv('data/clientes.csv')
df_pedidos = pd.read_csv('data/pedidos.csv')
df_merged = pd.merge(df_clientes, df_pedidos, on='IdCliente')
print("Pedidos combinados con clientes: ")
print(df_merged)
