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

Fecha entrega M7: miércoles 05/03/2025 23:59:59 Hora peninsular

Tutoría: martes 04/03/2025 - 16:00 a 18:00 en el mismo enlace zoom

Formato entrega:

* Carpeta modulo_7_Emilio_Fernández_evaluable en el repositorio github que ya tenéis.
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

Métricas

Modelado predictivo:

* Análisis de datos, business intelligence, backend
    * Preguntas de negocio.
    * Conexión a base de datos: Desde python o desde clientes UI como workbench o desde consola CLI.
    * Entender el esquema de la base de datos.
    * Ver qué consultas existen ya, vistas.
    * Realizar consultas SQL para obtener información que responda a las preguntas de negocio.
    * Administrador de base de datos: Entender muy bien el esquema, optimizarlo, crear índices, crear particiones, mejorar consultas para hacerlas más rápidas.

* EDAs

* Modelo regresión
    * 1. Entrenamiento X_train, Y_train
        *Fit
    * 2. Validación X_test, Y_text - Se obtienen  unas predicciones
        * Predict --> y_pred que comparamos a y_ytest
        * Métricas que se obtienen a partir de comparar y_test (valores reales) con y_pred
            * R2, MAE, MSE, RMSE, MAPE
    * 3. Entrenar con todos los datos disponibles:
        * Entrenar con X, Y (sin train ni el test)
    * 4. Exportar y desplegar el modelo

* Modelo clasificación

* Imputer: Simpleimputer, KNNImputer, IterativeImputer
    *Rellenar nulos para no tener que borrar esas filas o columnas

* Modelo:
    * Regresión: Regresiones, KNN, SVM
    * Clasificación: Regresión logística, KNN, SVMç

* Imputer para nulos se aplicaría a toda la X:
* Si hay particionamiento:
    * imputer.fit_transform(X_train)
    * imputer.transform(X_text)
    * Media:
        * X_train tiene menos datos
        * X
        * Evitamos cálculos sobre X_test para evitar introducir sesgos según el entrenamiento del modelo o del pipeline.

* Porcentaje de nulos %
    * Opción 1: Ver porqué se producen
        * Si los datos dan algún error que se pueda solucionar o inferir a partir del contexto, rellenando con algún dato acordado u obtenido de entender el tipo de problema.
    * Opción 2: Son nulos y no tienen solución
        * 5%-10%: Imputación simple con Simpleimputer con moda, media, mediana
        * 10%-30%: Impurtación avanzada con KNNImputer o IterativeImputer, manejo de fechas o transformación de datos personalizado apply()
        * 40%-50%: Se descarta esa columna o fila.
        * imbalanced-learn: SMOTE y técnicas ya más específicas para desbalanceo en clasificación.

* Encoding:
    * OrdinalEncoder: Si hay un orden natural:
        * Estudios:
        * Corte de diamante: malo, bueno, excelente
        * Café: acidez baja, media, alta
        * Se usa en la entrada X
    * OneHotEncoder: Si no hay un orden natural:
        * Ciudad
        * Color: azul, verde, rojo
        * Café: Honduras, Costa Rica, Brasil
        * Se usa en la entrada X
        * Desventaja: Puede crear muchas columnas si por ejemplo tenemos 50 categorías.
        Se puede acompañar de PCA a SelectKBest (Feature Selection Reducción de dimensionalidad).
    * LabelEncoder:
        * Se aplica sobre la columna "label", es decir, "y" para codificarla a numérico para poderla entrenar.

* Pipeline Column Transformer
    * X_train y X_test o nuevas X que se usen para predecir, todas deberían tener el mismo número y orden de columnas para que coincidan.
    * make:column_transformer(StandardScaler(), [0, 1, 2])
    * make:column_transformer(StandardScaler(), numerical_cols)

* Power BI:
    * HAB tienen un módulo de power bi en gitlab

M7:
* Al pulsar el botón generar predicción automáticamente aparece el botón para volcar a CSV, una vez pulsado el botón del CSV desaparezca

* Streamlit: streamlit.io
* Dash: https://github.com/plotly/dash
* Gradio: https://github.com/gradio-app/gradio

* Fijarse:
    * Fechas de actualización, últimos commits
    * Fechas de release
    * Comunidad activa, número de contributos, gente que lo usa, estrellas github...