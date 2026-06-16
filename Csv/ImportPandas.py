import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Cargo los datos
df = pd.read_csv('Intel_CPUs.csv')

print("OKEY! Archivo cargado correctamente")

print(" ")
print("--- Analisis Avanzado de Datos ---")

# Logica de filtrado: procesadores de 7ma generacion
filtro_avanzado = df['Product_Collection'].str.startswith('7th', na=False)
df_filtrado = df[filtro_avanzado]
print(df_filtrado[['Product_Collection', 'Vertical_Segment', 'nb_of_Cores']].to_string())

# Suma de nucleos en la 7ma generacion
suma_nucleos = df_filtrado['nb_of_Cores'].sum()

print("\n----- Reporte Automatizado -----")
print(f"Nucleos relevados en procesadores 7th Gen: {suma_nucleos}")

# Condicional segun cantidad de nucleos
if limite_alto := (suma_nucleos > 150):
    print("¡Alerta! El total de nucleos supera el limite establecido.")
    print("Requiere revision inmediata.")
elif suma_nucleos < 80:
    print("Aviso: cantidad de nucleos baja para esta generacion.")
    print("Monitorear disponibilidad de modelos.")
else:
    print("Cantidad de nucleos estable, sin alertas por el momento.")

# Procesadores con mas de 4 nucleos (todo el dataset)
filtro_numero = df['nb_of_Cores'] > 4
df_muchos_nucleos = df[filtro_numero]
print(f"\nProcesadores con mas de 4 nucleos: {len(df_muchos_nucleos)}")
print(df_muchos_nucleos[['Product_Collection', 'nb_of_Cores']].head(10).to_string())

# ------------------------------------------
# Grafico de distribucion por cantidad de nucleos
# ------------------------------------------
print("\n[Generando GRAFICO de Distribucion de Nucleos]")
sns.set_theme(style="whitegrid")
df_grafico = df[df['nb_of_Cores'] < 26]
plt.figure(figsize=(10, 5))
sns.countplot(data=df_grafico, x='nb_of_Cores', hue='nb_of_Cores', palette='viridis', legend=False)
plt.title('Distribución de Procesadores Intel por Cantidad de Núcleos', fontsize=14)
plt.xlabel('Número de Núcleos (Cores)')
plt.ylabel('Cantidad de Modelos')
plt.tight_layout()
plt.savefig('grafico_distribucion_nucleos.png', dpi=300)
print("\n¡Hecho! El grafico se guardo correctamente en tu carpeta.")
plt.show()