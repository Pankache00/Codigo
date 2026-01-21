# Operaciones Avanzadas en Pandas

#1.- Fusión (merge) de DataFrame
# La fusión permite combinar dos DataFrames basados en una o más columnas comunes.

import pandas as pd

# Datos de ventas
data_ventas = {
    'Producto': ['Laptop', 'Tablet', 'Smartphone', 'Monitor', 'Teclado'],
    'Ventas': [1500, 800, 1200, 500, 300],
    'Fecha': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}
df_ventas = pd.DataFrame(data_ventas)

# Datos de proveedores
data_proveedores = {
    'Producto': ['Laptop', 'Tablet', 'Smartphone', 'Monitor', 'Teclado'],
    'Proveedor': ['TechCorp', 'GadgetHub', 'SmartWorld', 'ScreenMasters', 'KeyFactory'],
    'Costo': [1000, 500, 800, 300, 200]
}
df_proveedores = pd.DataFrame (data_proveedores)

#on='Producto': Fusiona ambos DataFrames usando la columna Producto como clave común.
#Si las columnas no coinciden exactamente, puedes usar left_on y right_on para especificar columnas diferentes.

# Fusionar ambos DataFrames
df_merged = pd.merge(df_ventas, df_proveedores, on='Producto')
print("Fusión de DataFrame:\n", df_merged)

#2.- Concantenar DataFrames apilándolos vertical u horizontal

#Datos Adicionales
data_extra = {
    'Producto': ['Mouse', 'Parlantes'],
    'Ventas': [200, 400],
    'Fecha': ['2025-01-06', '2025-01-07']
}
data_extra = pd.DataFrame(data_extra)