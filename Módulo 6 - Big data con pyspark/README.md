
## Instalación Docker

https://www.loom.com/share/416ba4172ac04ac9b5ab047e20f594fa?t=16

Docker es una herramienta de virtualización para creación de imágenes y contenedores. Un contenedor será un sistema operativo empaquetado con todas las herramientas para ejecutar algo, una aplicación, un software.

Por ejemplo:

* MySQL
* MongoDB
* Python jupyter
* Python jupyter con pyspark

Instalar Docker:

https://docs.docker.com/desktop/setup/install/windows-install/

https://learn.microsoft.com/en-us/windows/wsl/install

a) Habilitar Hyper-V. A través del Panel de Control → Programas → Activar o desactivar las características de Windows → Marcar la casilla de Hyper-V:
    * Virtual Machine Platform
    * Subsistema de Windows para Linux
    * Plataforma del hipervisor de Windows

b) Habilitar WSL2. En PowerShell como administrador, ejecutar wsl --install para instalar la versión más reciente de WSL2.

wsl --install

wsl --list --online

wsl --install -d Ubuntu-24.04

wsl --update

Pedirá nombre usuario y contraseña, que tenemos que crear nuevos desde cero y anotarlos.

Reiniciar el ordenador

Descargar e instalar Docker desktop. 

https://www.docker.com/products/docker-desktop/

Dejamos marcadas: 

* Use WSL2 instead of Hyper-V
* Create shortcut icon

MAC:

https://docs.docker.com/desktop/setup/install/mac-install/

brew install --cask docker 

o instalar directamente docker desktop

## Probar docker

Primero abrir la aplicación Docker Desktop.

docker run hello-world

Si todo va bien sale esto:

Hello from Docker!
This message shows that your installation appears to be working correctly.

## Reinstalar ubuntu si hay problemas

wsl --list --verbose

wsl --unregister Ubuntu-22.04


## Crear contendor Apache Spark

En la misma cmd o bash donde funcione el docker ps, probamos a ejecutar este comando:

docker run -it --name pyspark -p 8888:8888 jupyter/pyspark-notebook

pesa como 5 GB.

Una vez ya creado, si queremos volver a abrir otro día el pyspark hay que ejecutar:

docker start pyspark

Para entrar podemos abrir el navegador y escribir:

http://127.0.0.1:8888/lab?token=9aac6b3af75fa484a16bfb3cceae82c75c12b507aea26f55 

Esa url la vemos en los logs del contenedor


## Reinstalar:

en powershell como admin:

dism.exe /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux /norestart
dism.exe /online /disable-feature /featurename:VirtualMachinePlatform /norestart
dism.exe /online /disable-feature /featurename:HypervisorPlatform /norestart

Reiniciar 

wsl --unregister Ubuntu-24.04

Abre C:\Users\TU_USUARIO\AppData\Local\Packages
Busca una carpeta con un nombre similar a CanonicalGroupLimited...Ubuntu...
Elimínala.

dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
dism.exe /online /enable-feature /featurename:HypervisorPlatform /all /norestart

Reiniciar

wsl --install

después en powershell:

sc query LxssManager
net start LxssManager

wsl --set-default-version 2

docker desktop

## En caso de que docker desktop no funcione

Abrir ubuntu

https://docs.docker.com/engine/install/ubuntu/

sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo docker run hello-world



## Conectar desde Visual Studio Code

docker logs -f pyspark

http://127.0.0.1:8888/lab?token=4bbb2671e6bebd174b73388a8a427e9ac9bf3c563d6e59a8

Crear un nuevo archivo entorno.ipynb  en Visual Studio Code

Select Kernel:

* Select Existing jupyter environment

## dos formas de acceder:

* opción 1: http://127.0.0.1:8888/lab?token=4bbb2671e6bebd174b73388a8a427e9ac9bf3c563d6e59a8
* opción 2: conectar desde visual studio code seleccionando Existing jupyter server

Al reiniciar el contenedor docker es posible que el token de jupyter lab cambie y tengamos que cambiar la conexión desde visual studio code.

## Docker Hub (opcional)

https://hub.docker.com/

Repositorio de imágenes docker, similar a GitHub pero para imágenes de docker.

https://hub.docker.com/_/mysql

Vamos a probar a crear un contenedor MySQL.

Comando de consola descargar imagen:

docker pull mysql:8.0.41

Comando de consola crear contenedor:

docker run -d --name mysql8 -p 3307:3306 -e MYSQL_ROOT_PASSWORD=admin -e MYSQL_DATABASE=testing_db mysql:8.0.41

Probar a conectar con MySQL Workbench desde puerto 3307 y ver que aparece la base de datos testing_db.

Ver stats con el comando:

docker stats

## EJERCICIO M6

Dataset: diamonds

* PARTE 1 (10 %) Carga de datos de diamonds desde CSV con schema: https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv

* PARTE 2 (40 %) Pipeline regresión price con preprocesados
  * Imputer, StringIndexer, OneHotEncoder, MinMaxScaler o StandardScaler, VectorAssembler

* PARTE 3 (40 %) Pipeline clasificación multiclase sobre variable cut con preprocesados
  * Imputer, StringIndexer, OneHotEncoder, MinMaxScaler o StandardScaler, VectorAssembler

* PARTE 4 (10 %) Gridsearch con CrossValidation sobre cualquiera de los pipelines

Los modelos, se puede utilizar RandomForest para los dos por ejemplo o el que se quiera. Ejemplo RandomForestRegressor para regresión y MultiLayerPerceptronClassifier para clasificación.

m6_nombre_apellido.ipynb

Entrega: 02/03/2025

Usar pyspark MLlib y dataframes de pyspark. Seguir el notebook 08.pipelines.ipynb