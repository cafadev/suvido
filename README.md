# Django project template

Esta es la plantilla estándar de un proyecto en Django, la misma tiene las configuraciones básicas para asegurar un deploy en un Shared Host.

Para poder ejecutar correctamente este template, asegúrese de crear un entorno virtual con la herramienta de su elección: Anaconda Navigator, Virtualenv o PyLenv. Se recomienda la versión 3.8 de python.

Una vez creado y activado el entorno virtual instale todas las dependencias del proyecto ejecutando

`pip install -r requirements`.

# Crear el archivo .env

El archivo .env deberá contener las variables de entorno que necesitará el proyecto para la correcta ejecución tanto en un ambiente de desarrollo así como en producción, este archivo debe contener las siguientes variables:

#### DEBUG

Este valor debe de ser `True` cuando el proyecto se encuentra en desarrollo localmente, no olvide cambiar su valor a `False` cuando el proyecto vaya ser puesto en producción

#### HOST_PATH

El HOST_PATH es el subdirectorio donde se va encontrar almacenado el proyecto en el servidor de producción, por ejemplo, si el proyecto se encuentra almacenado en el subdirectorio `django-project/django-project`, la dirección del mismo se verá de la siguiente manera `https://example.com/django-project/django-project`. por ende la variable debe ser `HOST_PATH=django-project/django-project`.

Observe que el valor de la variable NO debe contener una pleca al principio ni al final de la misma.

#### HOST_USER

Esta variable contiene el nombre de usuario dentro de la carpeta `/home`, este también suele ser el nombre de usuario con el que accede al CPanel.

### Variables de configuración de Base de datos

Las siguientes variables se encargan de la conexión con la base de datos:

- **DATABASE_ENGINE**: Este es el motor de base de datos que se utilizara en el proyecto.
- **DATABASE_NAME**: El nombre de la base de datos a utilizar
- **DATABASE_USER**: Usuario para acceder a la base de datos
- **DATABASE_HOST**: Host donde se encuentra la base de datos, por lo general es localhost
- **DATABASE_PORT**: Puerto de acceso a la base de datos, usualmente 3306

### CORS_ALLOWED_ORIGINS

En esta variable de entorno se especifican los dominios o sitios que podrán tener acceso al API, si o si debe incluir el dominio del sitio donde va estar almacenado nuestro proyecto

al finalizar la declaración el archivo debería ser similar a:

`DEBUG=True`

`HOST_PATH=`

`HOST_USER=`

`DATABASE_ENGINE=django.db.backends.mysql`

`DATABASE_NAME=django`

`DATABASE_USER=root`

`DATABASE_HOST=localhost`

`DATABASE_PORT=3306`

`CORS_ALLOWED_ORIGINS=https://<domain>`

No olvide que las variables dentro del archivo .env cambiaran según el ambiente donde se encuentre el proyecto (desarrollo o en producción).
