'''
Terminal
-----------
Comandos de inicio:

ls # Listar archivos
cd Desktop # Cambiar de directorio
cd .. # Regresar un directorio
mkdir "HelloGit" # Crear directorio
touch 'hellogit.py' # Crear archivo
git init # Inicializar en este directorio el contexto git. Se crea una carpeta oculta .git (no tocar)
# Se crea algo llamao "master" que es la rama principal
# El codigo que creamos va a tener diferentes flujos , y cada rama (flujo) va a tener un nombre diferente

git branch -m main # Cambiar el nombre de la rama principal
git status # Ver el estado de los archivos
# aparece el fichero en el que estamos pero dice que no hay 'commits'. No tiene guardado el archivo de ninguna forma en git.
# Ahora mismo estamos trabajando en local. No estamos trabajando en la nube.

-----------
Añadir un archivo a la zona de preparación (staging):
git add hellogit.py # Añadir un archivo a la zona de preparación. Aun no tengo commits, pero ya tenemos un archivo.
-----------
Crear un commit (hacer una fotografia):
git commit # Guardar el archivo en git. Se crea un 'commit' que es un punto de guardado.
# Se abre un editor de texto para escribir un mensaje. Es obligatorio escribir un mensaje para identificar el commit.

git commit -m "Mensaje" # Hacer un commit con un mensaje directamente
# Cada commit tiene un identificador único. Es un código de 40 caracteres que identifica el commit.

git log # Ver los commits que hemos hecho
git log --graph # Ver los commits que hemos hecho de forma gráfica. Para salir pulsar 'q'.
git log --graph --pretty=oneline # Ver los commits que hemos hecho en una sola linea
git log --graph --decorate --all --oneline # Ver los commits que hemos hecho en una sola linea y con colores.

git status # Ver el estado de los archivos

-----------
Volver a un commit anterior:
git checkout hellogit2.py # Volver a un commit anterior (situarnos en un punto concreto). 
¡¡¡¡ Se pierden los cambios que hayamos hecho desde ese commit !!!!

git reset # Volver a un commit anterior. Se pierden los cambios que hayamos hecho desde ese commit.


--------
Crear un alias para un comando (util para comandos largos):
git config --global alias.tree "log --graph --decorate --all --oneline" # creamos un alias llamado 'tree' para el comando 

--------



'''
print('Hello Git')
print('¿Que tal el curso?')
# El codigo que creamos va a tener diferentes flujos , y cada rama (flujo) va a tener un nombre diferente