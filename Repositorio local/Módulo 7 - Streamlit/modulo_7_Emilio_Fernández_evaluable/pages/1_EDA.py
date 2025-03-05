import os
import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Análisis de datos (EDA)", page_icon="icons/EDA.png")

# Redirigir a la página principal
if st.button('Ir a inicio'):
    st.switch_page('app.py')

# Estilos CSS
with open("styles.css", "r") as file:
    st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

# Título
st.title('Exploración de Datos (EDA)')

# Carga de datos y función de caché
@st.cache_resource
def load_data():
    return sns.load_dataset('diamonds').dropna()

# Cargar los datos
df = load_data()

# Filtros globales
st.header('Filtros Globales')
st.markdown("**Categóricos**")
categoricals = {col: df[col].unique() for col in ['color', 'cut', 'clarity']}
selected_filters = {
    'color': st.multiselect('Selecciona los colores de diamante', options=categoricals['color'], default=categoricals['color']),
    'cut': st.multiselect('Selecciona el tipo de corte', options=categoricals['cut'], default=categoricals['cut']),
    'clarity': st.multiselect('Selecciona la claridad de los diamantes', options=categoricals['clarity'], default=categoricals['clarity'])
}

st.markdown("**Numéricos**")
numeric_filters = {
    'price': st.slider('Rango de precios de los diamantes:', min_value=int(df['price'].min()), max_value=int(df['price'].max()), value=(int(df['price'].min()), int(df['price'].max()))),
    'carat': st.slider('Rango de peso (carat):', min_value=float(df['carat'].min()), max_value=float(df['carat'].max()), value=(float(df['carat'].min()), float(df['carat'].max()))),
    'depth': st.slider('Rango de profundidad:', min_value=float(df['depth'].min()), max_value=float(df['depth'].max()), value=(float(df['depth'].min()), float(df['depth'].max()))),
    'table': st.slider('Rango de tamaño de mesa:', min_value=float(df['table'].min()), max_value=float(df['table'].max()), value=(float(df['table'].min()), float(df['table'].max())))
}

# Filtrado de datos
df_filtered = df[
    (df['cut'].isin(selected_filters['cut'])) &
    (df['color'].isin(selected_filters['color'])) &
    (df['clarity'].isin(selected_filters['clarity'])) &
    (df['price'].between(*numeric_filters['price'])) &
    (df['carat'].between(*numeric_filters['carat'])) &
    (df['depth'].between(*numeric_filters['depth'])) &
    (df['table'].between(*numeric_filters['table']))
]

# Mostrar filtros aplicados y datos
st.dataframe(df_filtered)
st.write(f'Número de filas antes de aplicar filtros: **{df.shape[0]}**')
st.write(f'Número de filas después de aplicar filtros: **{df_filtered.shape[0]}**')
st.write(f'Filas eliminadas: **{df.shape[0] - df_filtered.shape[0]}**')

# Visualizaciones
st.header("Visualizaciones")
tabs = st.tabs(["Gráficos con Seaborn", "Gráficos Interactivos con Plotly", "Gráficos con Matplotlib"])

# Gráficos con Seaborn
with tabs[0]:
    st.subheader("Distribución de Precios")
    fig_seaborn_1, ax_seaborn_1 = plt.subplots(figsize=(6,4))
    sns.histplot(df_filtered['price'], kde=True, ax=ax_seaborn_1, color='orange')
    ax_seaborn_1.set_title('Distribución de Precio')
    st.pyplot(fig_seaborn_1)

    st.subheader("Mapa de Calor de Correlaciones")
    fig_seaborn_2, ax_seaborn_2 = plt.subplots(figsize=(6,4))
    sns.heatmap(df_filtered.corr(numeric_only=True), annot=True, cmap='viridis', ax=ax_seaborn_2)
    ax_seaborn_2.set_title('Correlación entre Variables')
    st.pyplot(fig_seaborn_2)

# Gráficos Interactivos con Plotly
with tabs[1]:
    st.subheader("Precio Promedio por Peso")
    df_grouped = df_filtered.groupby('price', as_index=False)['carat'].mean()
    st.plotly_chart(px.bar(df_grouped, x='price', y='carat', color='price', title="Precio medio por peso"))

    st.subheader("Relación entre Profundidad y Mesa por Corte")
    st.plotly_chart(px.scatter(df_filtered, x='depth', y='table', color='price', facet_col='cut', title="Profundidad vs Mesa por Corte"))

    st.subheader("Relación entre Clarity y Cut")
    st.plotly_chart(px.scatter(df_filtered, x='clarity', y='cut', color='price', size='carat', title="Clarity vs Cut"))

# Gráficos con Matplotlib
with tabs[2]:
    st.subheader("Histograma de Precios")
    fig_matplotlib_1, ax_matplotlib_1 = plt.subplots(figsize=(12,6))
    ax_matplotlib_1.hist(df_filtered['price'], bins=20, color='skyblue', edgecolor='black')
    ax_matplotlib_1.set_title('Distribución de Precios')
    ax_matplotlib_1.set_xlabel('Precio')
    ax_matplotlib_1.set_ylabel('Frecuencia')
    st.pyplot(fig_matplotlib_1)

    st.subheader("Boxplot de Precios")
    fig_matplotlib_2, ax_matplotlib_2 = plt.subplots(figsize=(12,6))
    ax_matplotlib_2.boxplot(df_filtered['price'], showmeans=True)
    ax_matplotlib_2.set_title('Distribución de Precios')
    ax_matplotlib_2.set_ylabel('Precio')
    st.pyplot(fig_matplotlib_2)

    st.subheader("Relación entre Precio y Color")
    fig_matplotlib_3, ax_matplotlib_3 = plt.subplots(figsize=(12,6))
    class_cut = {'Ideal': 'blue', 'Very Good': 'green', 'Premium': 'red', 'Good': 'yellow', 'Fair': 'orange'}
    for cut_type, col in class_cut.items():
        ax_matplotlib_3.scatter(df_filtered[df_filtered['cut'] == cut_type]['price'], df_filtered[df_filtered['cut'] == cut_type]['color'], color=col, label=cut_type)
    ax_matplotlib_3.set_xlabel('Precio')
    ax_matplotlib_3.set_ylabel('Color')
    ax_matplotlib_3.set_title('Relación Precio vs Color')
    ax_matplotlib_3.legend()
    ax_matplotlib_3.grid(True)
    st.pyplot(fig_matplotlib_3)

# Descarga de datos
st.header('Descargar Datos')
c1, c2 = st.columns(2)
with c1:
    st.download_button('Descargar Datos Originales', data=df.to_csv(index=False), file_name='diamonds_original.csv', mime='text/csv')
with c2:
    st.download_button('Descargar Datos Filtrados', data=df_filtered.to_csv(index=False), file_name='diamonds_filtrado.csv', mime='text/csv')