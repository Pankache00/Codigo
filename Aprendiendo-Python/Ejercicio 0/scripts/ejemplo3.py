import pandas as pd

df = pd.read_csv('data/tips.csv')

# Imprimir las 10 primeras filas
print(df.head(10))

# Imprime la información general
print(df.info())

# Imprimir las estadísticas descriptivas
print(df.describe())

# Selección y Filtrado
subset_columnas = df[['total_bill', 'day']]
print(subset_columnas)

# Filtrando total_bill > 20
filtro = df[df['total_bill'] > 20]
print(filtro)

# Imprimos la cantidad de valores faltantes (NaN) existentes por columna
print(df.isna().sum())

# Nuevo DataFrame sin valores faltantes (NaN)
print(df.dropna())
