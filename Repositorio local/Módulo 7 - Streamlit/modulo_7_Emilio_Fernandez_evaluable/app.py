import streamlit as st
import os
st.set_page_config(
    page_title='Inicio', 
    page_icon=os.path.join("icons", "home.png")
)
with open("styles.css", "r") as f:
    css_content = f.read()
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
st.title('Módulo 7: Streamlit')
st.write('''Ejercicio de evaluación.''')
image_path = os.path.join("icons", "fondo.jpg")
st.image(image_path)
c1, c2, c3 = st.columns(3)
with c1:
    if st.button('EDA'):
        st.switch_page('pages/1_EDA.py')
with c2:
    if st.button('Regresión'):
        st.switch_page('pages/2_Regresion.py')      
with c3:
    if st.button('Clasificación'):
        st.switch_page('pages/3_Clasificacion.py')