# ANÁLISIS DE DATOS - INTEL CPUs
# Ejercicios 1 a 15

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Intel_CPUs.csv')

# La columna de precio viene como texto ("$393.00 "), la convertimos a número.
# Algunas filas traen un RANGO ("$70.00 - $77.00"); en esos casos tomamos el promedio.
def limpiar_precio(valor):
    if pd.isna(valor):
        return np.nan
    numeros = [float(n.replace('$', '').replace(',', '').strip())
               for n in str(valor).split('-')]
    return sum(numeros) / len(numeros)

df['Recommended_Customer_Price'] = df['Recommended_Customer_Price'].apply(limpiar_precio)

filtro_avanzado = (df['Vertical_Segment'] == 'Desktop') & (df['nb_of_Cores'] >= 4)

# act 1
print('=' * 60)
print('act 1')
print('=' * 60)
filas, columnas = df.shape
print(f'✨ La tabla contiene {filas} filas y {columnas} columnas ✨\n')

# act 2
print('=' * 60)
print('act 2')
print('=' * 60)
filtro_exacto = df['Vertical_Segment'] == 'Desktop'
df_exacto = df[filtro_exacto]
print(f'Procesadores "Desktop": {len(df_exacto)} filas')
print(df_exacto[['Vertical_Segment', 'Processor_Number']].head(), '\n')


# act 3 
print('=' * 60)
print('act 3')
print('=' * 60)
df_parcial = df[df['Processor_Number'].str.startswith('i7', na=False)]
print(f'Procesadores cuyo número empieza con "i7": {len(df_parcial)} filas')
print(df_parcial[['Processor_Number', 'Vertical_Segment']].head(), '\n')

# act 4 
print('=' * 60)
print('act 4')
print('=' * 60)
df_seleccion = df_parcial[['Vertical_Segment', 'Recommended_Customer_Price']]
print(df_seleccion.head(), '\n')



# act 5
print('=' * 60)
print('act 5')
print('=' * 60)
resumen_agrupado = (
    df.groupby('Vertical_Segment')['Recommended_Customer_Price']
    .sum()
    .sort_values(ascending=False)
)
print(resumen_agrupado, '\n')

# act 6
print('=' * 60)
print('act 6')
print('=' * 60)
UMBRAL_CRITICO = 50000

if (suma_total := df_seleccion['Recommended_Customer_Price'].sum()) > UMBRAL_CRITICO:
    print(f'Suma total: ${suma_total:,.2f}  →  🔴 Prioridad Alta')
else:
    print(f'Suma total: ${suma_total:,.2f}  →  🟢 Estado Normal')
print()

# act 7
print('=' * 60)
print('act 7 - generando grafico_barras.png')
print('=' * 60)
plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x='Vertical_Segment',
    y='Recommended_Customer_Price',
    hue='Vertical_Segment',
    estimator=sum,
    errorbar=None,
    palette='viridis',
    legend=False
)
plt.title('Precio total por segmento (Vertical_Segment)', fontweight='bold')
plt.xlabel('Segmento')
plt.ylabel('Precio recomendado total (USD)')
plt.tight_layout()
plt.savefig('grafico_barras.png', dpi=150)
plt.close()
print('Gráfico guardado.\n')

# act 8 
print('=' * 60)
print('act 8 - generando grafico_torta.png')
print('=' * 60)
top_segmentos = resumen_agrupado.nlargest(4)

plt.figure(figsize=(6, 6))
plt.pie(
    top_segmentos.values,
    labels=top_segmentos.index,
    autopct='%1.1f%%',
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)
plt.title('Distribución del precio total (Top 4 segmentos)', fontweight='bold')
plt.tight_layout()
plt.savefig('grafico_torta.png', dpi=150)
plt.close()
print('Gráfico guardado.\n')

# act 9 
print('=' * 60)
print('act 9')
print('=' * 60)
condicion_extra = df['Recommended_Customer_Price'] > 300

resultado_loc = df.loc[
    filtro_avanzado & condicion_extra,
    ['Processor_Number', 'Recommended_Customer_Price', 'nb_of_Cores']
]
print(resultado_loc.head())
print(f'\nFilas seleccionadas: {len(resultado_loc)}\n')

# act 10 
print('=' * 60)
print('act 10')
print('=' * 60)
print('Nulos por columna (solo columnas con al menos 1 nulo):')
nulos = df.isnull().sum()
print(nulos[nulos > 0], '\n')

df_con_nulos = df.copy()
print(f'Nulos en Recommended_Customer_Price: {df_con_nulos["Recommended_Customer_Price"].isnull().sum()}')

df_sin_nulos = df_con_nulos.dropna(subset=['Recommended_Customer_Price'])

media = df_con_nulos['Recommended_Customer_Price'].mean()
df_rellenado = df_con_nulos.fillna({'Recommended_Customer_Price': round(media, 2)})

print(f'\nOriginal:   {len(df_con_nulos)} filas')
print(f'Con dropna: {len(df_sin_nulos)} filas  (se eliminaron filas)')
print(f'Con fillna: {len(df_rellenado)} filas  (se rellenaron los huecos)\n')

# act 11
print('=' * 60)
print('act 11 - generando grafico_lineas.png')
print('=' * 60)
agrupado_lineas = (
    df.groupby('Vertical_Segment')['Recommended_Customer_Price']
    .mean()
    .sort_values()
)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(agrupado_lineas.index, agrupado_lineas.values, marker='o',
        color='#2E75B6', linewidth=2, markersize=8)

idx_max = agrupado_lineas.idxmax()
val_max = agrupado_lineas.max()

ax.annotate(
    f'Máximo: ${val_max:,.0f}',
    xy=(idx_max, val_max),
    xytext=(0, val_max * 0.85),
    arrowprops=dict(arrowstyle='->', color='red'),
    fontsize=11, color='red', fontweight='bold'
)

ax.set_title('Precio promedio por segmento', fontsize=14, fontweight='bold')
ax.set_xlabel('Segmento')
ax.set_ylabel('Precio promedio (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('grafico_lineas.png', dpi=150)
plt.close()
print('Gráfico guardado.\n')

# act 12
print('=' * 60)
print('act 12')
print('=' * 60)
resultado_original = df[filtro_avanzado]

valor_limite = 4 
resultado_query = df.query('nb_of_Cores >= @valor_limite and Vertical_Segment == "Desktop"')

print('Con corchetes:', len(resultado_original), 'filas')
print('Con .query():', len(resultado_query), 'filas')
print('¿Son iguales?', resultado_original.equals(resultado_query), '\n')

# act 13
print('=' * 60)
print('act 13')
print('=' * 60)
categorias_elegidas = ['Desktop', 'Mobile']
df_incluidos = df[df['Vertical_Segment'].isin(categorias_elegidas)]
df_excluidos = df[~df['Vertical_Segment'].isin(categorias_elegidas)]

print(f'Filas incluidas ({len(df_incluidos)}): Desktop + Mobile')
print(f'Filas excluidas ({len(df_excluidos)}): el resto (Server, Embedded)')

total = len(df)
suma = len(df_incluidos) + len(df_excluidos)
print(f'\nTotal original: {total}  |  Incluidos + Excluidos: {suma}')
print(f'¿Coinciden? {total == suma}\n')

# act 14
print('=' * 60)
print('act 14')
print('=' * 60)
print('=== DataFrame completo ===')
print(df['Vertical_Segment'].value_counts())
print('Valores unicos:', df['Vertical_Segment'].unique())
print('Cantidad de categorias:', df['Vertical_Segment'].nunique())
print('Porcentajes:')
print((df['Vertical_Segment'].value_counts(normalize=True) * 100).round(1))

df_filtrado = df[filtro_avanzado]
print('\n=== DataFrame filtrado ===')
print(df_filtrado['Vertical_Segment'].value_counts())
print('Valores unicos:', df_filtrado['Vertical_Segment'].unique())
print('Cantidad de categorias:', df_filtrado['Vertical_Segment'].nunique())
print()

# act 15
print('=' * 60)
print('act 15 - generando heatmap_correlacion.png')
print('=' * 60)

df_filtrado.to_csv('mi_resultado_filtrado.csv', index=False)
print(f'Archivo exportado: {len(df_filtrado)} filas guardadas en mi_resultado_filtrado.csv')

correlacion = df.corr(numeric_only=True)
print('\nMatriz de correlación (recorte):')
print(correlacion.round(2).iloc[:5, :5])

plt.figure(figsize=(10, 8))
sns.heatmap(
    correlacion,
    annot=False,
    fmt='.2f',
    cmap='coolwarm',
    linewidths=0.5,
    vmin=-1, vmax=1
)
plt.title('Correlacion entre variables numericas — Intel CPUs', fontweight='bold')
plt.tight_layout()
plt.savefig('heatmap_correlacion.png', dpi=150)
plt.close()
print('Grafico guardado.')

mask = np.triu(np.ones(correlacion.shape), k=0).astype(bool)
correlacion_sin_diag = correlacion.where(~mask)

par_max = correlacion_sin_diag.stack().idxmax()
par_min = correlacion_sin_diag.stack().idxmin()
print(f'\nPar más correlacionado:   {par_max[0]} ↔ {par_max[1]}')
print(f'Par menos correlacionado: {par_min[0]} ↔ {par_min[1]}')

print('\n' + '=' * 60)
print('ANÁLISIS COMPLETO')
print('=' * 60)