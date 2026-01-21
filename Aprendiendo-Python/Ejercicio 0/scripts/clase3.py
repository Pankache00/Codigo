import pandas as pd

# Cargar el CSV
# pd.read_csv('ruta_del_archivo.csv') Carga el contenido del archivo en un DataFrame.
df = pd.read_csv('data/iris.csv')

# Mostrar las primeras 5 filas
# df.head() Muestra las primeras 5 filas por defecto.
print(f"Primeras 5 filas del Dataframe: {df.head()} ")

# Mostrar información general del DataFrame
# df.info() Da información sobre las columnas, el tipo de datos y el conteo de valores no nulos.
print(f"Información del DataFrame: {df.info}")

# Mostrar estadísticas descriptivas
# df.describe() proporciona estadísticas descriptivas de las columnas numéricas.
print(f"Estadísticas descriptivas: {df.describe()}")

# Selección de columnas y filtrados de filas

# Seleccionar una columna por su nombre original
columna_unica = df['sepal_length']

# Varias Columnas
subset_columnas = df[['sepal_length', 'species']]


# Filtrado de filas (por ejemplo, sepal.length mayor a 5.5)
filtro = df[df['sepal_length'] > 5.0]
print(filtro.head())

# Usar más de 1 filtro o condiciones
filtro_combinado = df[(df['sepal_length'] > 5.0) & (df['species'] == 'setosa')]
print(filtro_combinado)

# Manejo de datos faltantes
# Muestra cuántos valores faltantes hay por columnas
print(df.isna().sum())

# Eliminar filas con valores faltantes
df_sin_na = df.dropna()

# Rellenar los valores faltantes con la media de la columna
# En caso de tener el archivo con solo valores númericos usariamos "df.filled = df.fillna(df.mean())"
# Pero en este caso algunas columnas contienen texto (String), por lo cual nos daría error al ejecutar así haremos la siguiente...
df_filled = df.fillna(df.select_dtypes(include='number').mean())
print(df_filled)
