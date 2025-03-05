import os
import streamlit as st
import joblib
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import LabelEncoder
st.set_page_config(
    page_title='Clasificación', 
    page_icon=os.path.join("icons", "clasificacion.png")
)
with open("styles.css", "r") as f:
    css_content = f.read()
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
if st.button('Ir a inicio'):
    st.switch_page('app.py')
@st.cache_resource
def load_model():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.normpath(os.path.join(project_dir, '..', 'models'))
    model_path = os.path.join(model_dir, 'pipeline_clasificacion.joblib')
    print(f"Cargando el modelo desde: {model_path}")
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        raise FileNotFoundError(f"El archivo {model_path} no existe.")
@st.cache_resource
def load_data():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
    return pd.read_csv(url)
st.title('Clasificación')
model = load_model()
df = load_data()
st.header('Introduce datos para la predicción')
with st.form("Diamonds_form"):
    carat_value = st.number_input(
                    'Introduce el total de carat', 
                    min_value=0.0, max_value=10.0, 
                    value=df['carat'].mean(), 
                    step=0.01
    )
    color_value = st.selectbox('Introduce el color', df['color'].unique().tolist())
    clarity_value = st.selectbox('Introduce el tipo de claridad', df['clarity'].unique().tolist())
    depth_value = st.number_input(
                    'Introduce la profundidad total', 
                    min_value=df['depth'].min(), max_value=df['depth'].max(), 
                    value=df['depth'].mean(), 
                    step=0.01
    )
    table_value = st.number_input(
                    'Introduce el tamaño de mesa total', 
                    min_value=df['table'].min(), max_value=df['table'].max(), 
                    value=df['table'].mean(), 
                    step=0.01
    )
    price_value = st.number_input(
                    'Introduce el precio total', 
                    min_value=0, max_value=20000, 
                    value=int(df['price'].mode().iloc[0]), 
                    step=1
    )
    x_value = st.number_input(
                    'Introduce el valor de x', 
                    min_value=df['x'].min(), max_value=df['x'].max(), 
                    value=df['x'].mean(), 
                    step=0.01
    )
    y_value = st.number_input(
                    'Introduce el valor de y', 
                    min_value=df['y'].min(), max_value=df['y'].max(), 
                    value=df['y'].mean(), 
                    step=0.01
    )
    z_value = st.number_input(
                    'Introduce el valor de z', 
                    min_value=df['z'].min(), max_value=df['z'].max(), 
                    value=df['z'].mean(), 
                    step=0.01
    )
    submit_button = st.form_submit_button("Generar predicción")
    if submit_button:
        X_input = pd.DataFrame({
            'carat': [carat_value],
            'color': [color_value],
            'clarity': [clarity_value],
            'depth': [depth_value],
            'table': [table_value],
            'price': [price_value],
            'x':[x_value],
            'y':[y_value],
            'z':[z_value],                 
        })
        prediction = model.predict(X_input)
        probability = model.predict_proba(X_input).max() * 100
        col1, col2 = st.columns(2)
        col1.metric('Tipo de corte estimado', value=prediction[0])
        col2.metric('Probabilidad', value=f'{probability:.2f} %')