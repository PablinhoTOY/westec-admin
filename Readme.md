## Westec 

En este repositorio se encontrará el código para el nuevo Westec Services admin desarrollado por Santiago Alvarez y Pablo Lizana

## Configuracion de FLASK

Estos son los pasos y comandos que debes correr al momento de clonar el proyecto

Sobre la carpeta /be
- Crear un virtual Enviorement en la raiz de la ruta con el comando **python -m venv nombre_del_venv**
- Situarse sobre la ruta del Virtual Enviorement con el comando **venv/Scripts/activate**
- Instalar las dependencias del proyecto Flask con el comando **pip install -r req.txt** ##Corregir##
- Crear un archivo .env en la raíz de be.
- Dentro del archivo insertar la siguiente variable: SKEY = 'valorrandom'
- Correr el comando **py app.py** para iniciar el proyecto Flask
  
Ya se debería tener el Flask corriendo  (normalmente por el puerto 5000 => http://localhost:5000).

## Configuracion de FLASK
Sobre la carpeta /be y con el venv activo
- De ser necesario, borrar la carpeta migrations (solo si no te corre la migracion bien)
- Correr el comando **flask db init** para preparar la migracion.
- Correr el comando **flask db migrate** para correr la migracion
- Correr el comando **flask db upgrade** para actualizacion los datos migrados.
- Correr el comando **flask seed** para insertar datos iniciales. Estos pueden ser editados en el archivo Seed Inicial.

## Configuracion del Front (vue js)

Estos son los pasos y comandos que debes correr al momento de clonar el proyecto

Sobre la carpeta /fe
- Correr el comando **npm i** para instalar todas las dependencias node modules.
- Correr el comando **npm run dev** para preparar los componentes vue js y permanecer escuchando los cambios sobre los componentes vue js

Ya se debería tener el vue JS configurado y ejecutando (normalmente por el puerto 8080 => http://localhost:8080).

