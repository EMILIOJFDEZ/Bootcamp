import os
import streamlit as st
import joblib
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Clasificación de diamantes", page_icon="icons/clasificacion.png")

# Redirigir a la página principal
if st.button('Ir a inicio'):
    st.switch_page('app.py')

# Cargar el archivo CSS
with open("styles.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Redirigir al inicio
if st.button('Ir a inicio'):
    st.experimental_rerun()

# Función para cargar el modelo
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models', 'pipeline_clasificacion.joblib')
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.error(f"El archivo {model_path} no existe.")
        return None

# Función para cargar los datos
@st.cache_resource
def load_data():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
    return pd.read_csv(url)

# Cargar datos y modelo
model = load_model()
df = load_data()

# Título de la aplicación
st.title('Clasificación de diamantes')

# Formulario de entrada para los datos
st.header('Introduce datos para la predicción')
with st.form("Diamonds_form"):
    # Campos de entrada con valores predeterminados
    inputs = {
        'carat': st.number_input('Introduce el total de carat', 0.0, 10.0, df['carat'].mean(), 0.01),
        'color': st.selectbox('Introduce el color', df['color'].unique().tolist()),
        'clarity': st.selectbox('Introduce el tipo de claridad', df['clarity'].unique().tolist()),
        'depth': st.number_input('Introduce la profundidad total', df['depth'].min(), df['depth'].max(), df['depth'].mean(), 0.01),
        'table': st.number_input('Introduce el tamaño de mesa total', df['table'].min(), df['table'].max(), df['table'].mean(), 0.01),
        'price': st.number_input('Introduce el precio total', 0, 20000, int(df['price'].mode().iloc[0]), 1),
        'x': st.number_input('Introduce el valor de x', df['x'].min(), df['x'].max(), df['x'].mean(), 0.01),
        'y': st.number_input('Introduce el valor de y', df['y'].min(), df['y'].max(), df['y'].mean(), 0.01),
        'z': st.number_input('Introduce el valor de z', df['z'].min(), df['z'].max(), df['z'].mean(), 0.01),
    }
    submit_button = st.form_submit_button("Generar predicción")

# Si el usuario presiona el botón de enviar
if submit_button and model:
    # Crear DataFrame con los valores introducidos
    X_input = pd.DataFrame(inputs, index=[0])
    
    # Realizar la predicción y obtener la probabilidad
    prediction = model.predict(X_input)
    probability = model.predict_proba(X_input).max() * 100

    # Mostrar resultados
    c1, c2 = st.columns(2)
    c1.metric('Tipo de corte estimado', value=prediction[0])
    c2.metric('Probabilidad', value=f'{probability:.2f} %')