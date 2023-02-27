# CRUD-DJANGO
Este es un CRUD basico de usuarios realizado con DJANGO 4.1.1
////////////////////////////////////////
Este archivo contiene informacion sobre la instalacion y ejecucion del crud
Gabriel Rodriguez


Es un crud Basico de usuarios Realizado en DJANGO 4.1.1

Previa instalacion python3 y pip

pip install Django==4.1.7
python -m django --version



previa instalacion python3 y pip

pip install Django==4.1.7
python -m django --version


////crear projecto
///dentro de la carpeta creada en Python

////creamos un proyecto donde crearemos las aplicaciones
django-admin startproject sistema

//ir a la carpeta donde esta el manage.py y correr 
python3 manage.py runserver
///esto arranca el servidor 


si puede ver este mensaje en su consola o visual studio code
Django version 4.1.7, using settings 'sistema.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

La instalacion esta correcta

Crear aplicacion
python manage.py startapp usuarios

debe instalar PyMySQL en python
ejecute Python3 -m pip install PyMySQL

debe instalar Pillow 9.4.0 (imagenes)

ejecute pip install pillow


Debe tener configurado un servidor web local con apache-mysql como xaamp, wamp, laragon

puede crear la estructura de bases de datos segun el modelo de la aplicacion 

o bien puede correr en phpmyadmin la estructura mysql adjuntada en crud.sql


copie la carpeta a su carpeta python local

en el archivo setting cambie los datos a su configuracion mysql


y ejecute el manage.py runserver de la carpeta sistemas 

