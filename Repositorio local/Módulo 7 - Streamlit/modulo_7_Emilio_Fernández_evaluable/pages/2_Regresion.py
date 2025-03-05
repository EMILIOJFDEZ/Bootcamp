import os
import joblib
import pandas as pd
import streamlit as st
st.set_page_config(
    page_title="Predicción del precio de Diamantes",
    page_icon="icons/regresion.png"
)
if st.button('Ir a inicio'):
    st.switch_page('app.py')
def cargar_estilos():
    with open("styles.css", "r") as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)
cargar_estilos()
@st.cache_resource
def cargar_modelo():
    ruta_modelo = os.path.join(os.path.dirname(__file__), '..', 'models', 'pipeline_regresion.joblib')
    if os.path.exists(ruta_modelo):
        return joblib.load(ruta_modelo)
    st.error(f"Modelo no encontrado: {ruta_modelo}")
    return None
@st.cache_resource
def cargar_datos():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
    return pd.read_csv(url)
datos_diamantes = cargar_datos()
modelo_regresion = cargar_modelo()
promedio_precio = datos_diamantes['price'].mean()
st.title("Predicción del Precio de Diamantes")
st.header("Introduce las características del diamante")
def crear_formulario():
    with st.form("formulario_prediccion"):
        peso_carat = st.number_input("Peso (carat)", 0.0, 10.0, datos_diamantes['carat'].mean(), step=0.01)
        tipo_corte = st.selectbox("Corte", datos_diamantes['cut'].unique())
        tipo_color = st.selectbox("Color", datos_diamantes['color'].unique())
        tipo_claridad = st.selectbox("Claridad", datos_diamantes['clarity'].unique())
        porcentaje_profundidad = st.number_input("Profundidad (%)", datos_diamantes['depth'].min(), datos_diamantes['depth'].max(), datos_diamantes['depth'].mean(), step=0.01)
        porcentaje_tabla = st.number_input("Tabla (%)", datos_diamantes['table'].min(), datos_diamantes['table'].max(), datos_diamantes['table'].mean(), step=0.01)
        dimension_x = st.number_input("Dimensión X (mm)", datos_diamantes['x'].min(), datos_diamantes['x'].max(), datos_diamantes['x'].mean(), step=0.01)
        dimension_y = st.number_input("Dimensión Y (mm)", datos_diamantes['y'].min(), datos_diamantes['y'].max(), datos_diamantes['y'].mean(), step=0.01)
        dimension_z = st.number_input("Dimensión Z (mm)", datos_diamantes['z'].min(), datos_diamantes['z'].max(), datos_diamantes['z'].mean(), step=0.01)
        enviar_formulario = st.form_submit_button("Predecir Precio")
        return enviar_formulario, peso_carat, tipo_corte, tipo_color, tipo_claridad, porcentaje_profundidad, porcentaje_tabla, dimension_x, dimension_y, dimension_z
enviar_formulario, peso_carat, tipo_corte, tipo_color, tipo_claridad, porcentaje_profundidad, porcentaje_tabla, dimension_x, dimension_y, dimension_z = crear_formulario()
if enviar_formulario and modelo_regresion:
    datos_nuevos = pd.DataFrame({
        'carat': [peso_carat], 'cut': [tipo_corte], 'color': [tipo_color], 'clarity': [tipo_claridad],
        'depth': [porcentaje_profundidad], 'table': [porcentaje_tabla], 'x': [dimension_x], 'y': [dimension_y], 'z': [dimension_z]
    })
    prediccion_precio = modelo_regresion.predict(datos_nuevos)[0]
    diferencia_precio = prediccion_precio - promedio_precio    
    c1, c2 = st.columns(2)
    c1.metric("Precio Estimado", f"{prediccion_precio:.2f} $", f"{diferencia_precio:.2f} $")
    c2.metric("Precio Medio", f"{promedio_precio:.2f} $")