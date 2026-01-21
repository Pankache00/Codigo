# Crees una lista de números(por ejemplo, temperaturas) y la conviertas en una Serie de Pandas.
# Calcules el valor máximo, mínimo y la media de la Serie.
# Imprimas los resultados.
# Tarea 2:
# Agrega una breve descripción de ejemplo_2.py en el README indicando qué hace el script.

# Tarea 3 (Opcional):
# Investiga el método df.describe() y pruébalo con el DataFrame del ejemplo_1.py(puedes agregarlo al mismo script o crear uno nuevo). Explica en el README qué información proporciona df.describe().

import pandas as pd

temperaturas = [14, 15, 14, 16, 15, 16, 18]  # Lista de temperaturas

# Máximo, Mínimo y Media
# transformamos la lista en una serie
serie_temperatura = pd.Series(temperaturas)

promedio = serie_temperatura.mean()  # Media
minimo = serie_temperatura.min()    # Mínimo
maximo = serie_temperatura.max()  # Máximo

print(promedio)
print(minimo)
print(maximo)
