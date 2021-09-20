# Tasks

Requisito: tener instalado npm, xampp y python para utilizar el proyecto.

Las versiones utilizadas son:
-xampp v3.2.4  
 -python v3.8.5

1. Una vez instalado lo previo,en la carpeta del repositorio

   pip install requirements.txt

   Este comando instalará todas las dependencias que necesite el proyecto.

2. para activar el entorno virtual deberá escribir
   ". venv/Scripts/activate" para windows
   ". venv/bin/activate" para linux

3. activar en el xampp, el modulo apache y mysql y,
   mediante el localhost crear una base de datos con el nombre "tasks"
   \*direccion de ejemplo: http://localhost:82/phpmyadmin/

4. python run.py para iniciar la aplicacion.
   dirigirse a la direccion que figura en la consola

5. para consumir las apis de la aplicacion desde vuejs, deberá ubicarse dentro de:
   carpetaDelProyecto/web

6. luego deberá ejecutar

   npm install -g @vue/cli

   o

   yarn global add @vue/cli

7. para instalar las dependencias
   npm/yarn install

8. npm/yarn run serve

   abrir el navegador con la url indicada.
   ejemplo: http://localhost:5000/

9. Para finalizar, escriba en consola deactivate para desactivar el entorno
   y pare las tareas de xampp.
