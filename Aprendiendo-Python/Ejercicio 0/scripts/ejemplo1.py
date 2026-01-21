# Ejercicios Nivel 1: Fundamentos de Python y Pandas

import pandas as pd

# Crear un diccionario con datos simples
data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [23, 30, 35, 28],
    'Ciudad': ['Santiago', 'Valparaíso', 'Concepción', 'La Serena']
}

# Convertir el diccionario en un DataFrame
df = pd.DataFrame(data)

# Imprimir el DataFrame completo
print("DataFrame completo:")
print(df)

# Calcular la media de la columna 'Edad'
promedio_edad = df['Edad'].mean()
print(f"El promedio de edad es: {promedio_edad}")

# Extra... df.describe()

df = pd.DataFrame(data)
print(df.describe())
