

Crear un entorno virtual:

python -m venv .mod3

Activar entorno virtual:

* Windows powershell: .mod3\Scripts\activate
* Bash: source .mod3/Scripts/activate

Para instalar paquetes:

pip install -r requirements.txt

## EJERCICIO MÓDULO 3

* m1_python/m1_nombre_apellido.ipynb
* m2_numpy/m2_nombre_apellido.ipynb
* m3_datascience/m3_nombre_apellido.ipynb
* m4_sql/m4_nombre_apellido.ipynb + sql

Slack poner nombre y apellido, foto.



## EJERCICIO MÓDULO 3:

Uso de Pandas y Seaborn.

IMPORTANTE: cargar el dataset desde CSV

* Carga con Pandas: pd.read_csv

* Limpieza de nulos (limpiar valores NaN):
    * Nulos en columnas continuas: mediana, media
    * Nulos en columnas categóricas: moda, un valor fijo

* Cambio de tipo de dato: .astype()

* Limpieza de valores error: 
    * llegue un valor incorrecto, por ejemplo una columna número le llega una interrogación

* Encoding: texto a numérico
    * Uso de la función get_dummies() para encoding one_hot

* Uso de función map o apply

* Ordenar por dos columnas con sort_values()

* Agrupaciones con groupby y visualizarla

* Seaborn EDAS:
    * univariantes:
        * histogramas y curvas de densidad
        * boxplot
        * countplot
    * bivariantes y multivariantes
        * scatterplot con hue, con size, con style
        * Calcular correlación con Pandas y mostrarla con seaborn
    * Combinarlas con filtros

* Outliers: Visualización y filtrado

* asimetría, curtosis y transformar datos con logaritmo o raíz cuadrada