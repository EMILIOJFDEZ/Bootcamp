# ENTORNO STREAMLIT

python -m venv .venv

En bash: source .venv/Scripts/activate
En Windows: .venv\Scripts\activate

pip install -r requirements.txt

pip install streamlit

## EJECUTAR ARCHIVOS STREAMLIT

Abrir terminal: Ctrl + ñ

Navegar hacia la carpeta donde esté el archivo de streamlit: cd clase/01.text

Ejecutar streamlit: streamlit run app.py

## API Streamlit

https://docs.streamlit.io/develop/quick-reference/cheat-sheet


* Write: st.write
* Text elements:
    * st.title
    * st.header
    * st.subheader
    * st.markdown
    * st.caption
    * st.code
    * st.divider
    * st.echo
    * st.latex
    * st.text
    * st.help
    * st.html

* Data elements:
    * st.dataframe
    * st.data_editor
    * st.table
    * st.metric
    * st.json

* Chart elements:
    * Nativos de Streamlit:
        * st.area_chart
        * st.bar_chart
        * st.line_chart
        * st.map
        * st.scatter_chart
    * Integraciones de librerías de visualización:
        * st.pyplot para ejecutar matplotlib y seaborn
        * st.plotly_chart para ejecutar plotly

* Layout y containers:
    * st.columns
    * st.container
    * st.dialog
    * st.empty
    * st.expander
    * st.form
    * st.popover
    * st.sidebar
    * st.tabs

* Input widgets:
    * Botones:
        * st.button
        * st.download_button
        * st.form_submit_button
        * st.link_button
        * st.page_link
    * Selección:
        * st.checkbox
        * st.color_picker
        * st.feedback
        * st.multiselect
        * st.pills
        * st.radio
        * st.segmented_control
        * st.selectbox
        * st.select_slider
        * st.toggle
    * Numérico:
        * st.number_input
        * st.slider
    * Fechas:
        * st.date_input
        * st.time_input
    * Texto:
        * st.text_input
        * st.text_area
        * st.chat_input
    * Multimedia:
        * st.file_uploader
        * st.audio_input
        * st.camera_input
        * st.data_editor


## EJERCICIO

Dataset: diamonds.

* PARTE 1 (30 %): Página 1 con EDA con seaborn y plotly con filtros globales
    * Gráficos univariantes: histograma, kdeplot, boxplot
    * Gráficos bivariantes: scatter
    * Gráficos multivariantes: heatmap, pairplot, scatter con hue o color 
    * Filtros globales categóricos y numéricos: un filtro para columna
* PARTE 2 (35 %): Página 2 Regresión con formulario sobre price + Pipeline ipynb
    * Regresión sobre columna price
    * pipeline_regresion.ipynb
    * pipeline_regresion.joblib
    * 2_Regresion.py con formulario de entrada para introducir datos y hacer prediccion y mostrar en st.metric
* PARTE 3 (35 %): Página 3 Clasificación con formulario sobre cut + Pipeline ipynb
    * Clasificación multiclase sobre columna cut (Usar LabelEncoder para cut)
    * pipeline_clasificacion.ipynb
    * pipeline_clasificacion.joblib
    * 3_Clasificacion.py con formulario de entrada para introducir datos y hacer prediccion y mostrar en st.metric
* Usar multipáginas
* Separar apartados con encabezados o container
* Mostrar predicciones usando st.metric
* Opcionalmente se pueden acumular predicciones en un dataframe y mostrar un botón de descargar dataframe en CSV.


Fecha entrega M7: miércoles 05/03/2025 23:59:59 Hora peninsular

Tutoría: martes 04/03/2025 - 16:00 a 18:00 en el mismo enlace zoom

Formato entrega:

* Nueva carpeta modulo_7_nombre_apellido_evaluable en el repositorio github que ya tenéis.
    * app.py (Home)
    * .streamlit/
    * pages/
        * 1_EDA.py
        * 2_Regresion.py
        * 3_Clasificacion.py
    * models/
        * pipeline_regresion.joblib
        * pipeline_clasificacion.joblib
    * notebooks/
        * pipeline_regresion.ipynb
        * pipeline_clasificacion.ipynb