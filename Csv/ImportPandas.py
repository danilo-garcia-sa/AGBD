import pandas as pd

# Solo pones el nombre exacto del archivo entre comillas
df=pd.read_csv('Intel_CPUs.csv')

print("OKEY! Archivo cargado correctamente")

# # Mostrando las primeras filas del dataframe
# print(df.head())

# # Filtrando por año 2022
# #resultado = df[df['year'] == 2022]

# Resultado = df['Product_Collection'].count()
# print(f'Cantidad total de procesadores Intel: {Resultado}')

# Suma = df['nb_of_Cores'].sum()
# print(f'Suma total de Nucleos: {Suma}')

print(" ")
print("--- Analisis Avanzado de Datos ---")

filtro_avanzado = df['Product_Collection'].str.startswith('7th', na = False)
df_filtrado = df[filtro_avanzado]
print(df_filtrado)

sumo_nucleos = df_filtrado['nb_of_Cores'].sum()
print(f"Total de nucleos en procesadores 7th Gen: {sumo_nucleos}\n")

filtro_numero = df['nb_of_Cores'] > 4
df_muchos_nucleos = df[filtro_numero]
print(f"Procesadores con mas de 4 nucleos: {len(df_muchos_nucleos)}")
print(df_muchos_nucleos[['Product_Collection', 'nb_of_Cores']].head(10))