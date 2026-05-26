import pandas as pd

# Solo pones el nombre exacto del archivo entre comillas
df=pd.read_csv('Intel_CPUs.csv')

print("OKEY! Archivo cargado correctamente")

# Mostrando las primeras filas del dataframe
print(df.head())

# Filtrando por año 2022
#resultado = df[df['year'] == 2022]

Resultado = df['Product_Collection'].count()
print(f'Cantidad total de procesadores Intel: {Resultado}')

Suma = df['nb_of_Cores'].sum()
print(f'Suma total de Nucleos: {Suma}')

print(" ")
print("--- Analisis Avanzado de Datos ---")

filtro_avanzado = df['Product_Collection'].str.startswith('7th', na = False)
df_filtrado = df[filtro_avanzado]
print(df_filtrado)

