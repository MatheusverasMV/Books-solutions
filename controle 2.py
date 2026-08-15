import pandas as pd

lista = [
    498, 501, 500, 503, 499, 502,
    500, 497, 501, 502, 499, 500,
    501, 498, 500, 502, 499, 503
]

df = pd.DataFrame(lista, columns=['Valores'])
print(df.describe())
print(f"Amplitude: {df['Valores'].max() - df['Valores'].min()}")