'''
Terminal
----------- COMANDOS INICIALES -----------

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

----------- GUARDAR CAMBIOS EN GIT -----------

1º Añadir un archivo a la zona de preparación (staging):
git add hellogit.py # Añadir un archivo a la zona de preparación. Aun no tengo commits, pero ya tenemos un archivo.

2º Crear un commit (hacer una fotografia):
git commit # Guardar el archivo en git. Se crea un 'commit' que es un punto de guardado.
# Se abre un editor de texto para escribir un mensaje. Es obligatorio escribir un mensaje para identificar el commit.

git commit -m "Mensaje" # Hacer un commit con un mensaje directamente
# Cada commit tiene un identificador único. Es un código de 40 caracteres que identifica el commit.

---------- ESTADO DE LOS ARCHIVOS -----------
git log # Ver los commits que hemos hecho
git log --graph # Ver los commits que hemos hecho de forma gráfica. Para salir pulsar 'q'.
git log --graph --pretty=oneline # Ver los commits que hemos hecho en una sola linea
git log --graph --decorate --all --oneline # Ver los commits que hemos hecho en una sola linea y con colores.

git status # Ver el estado de los archivos

git diff # Ver los cambios que hemos hecho en el archivo. Nos dice que cambios hemos hecho desde el último commit sin hacer un commit.

----------- VOLVER A COMMIT ANTERIOR -----------
git checkout hellogit2.py # Volver a un commit anterior (situarnos en un punto concreto). 
¡¡¡¡ Se pierden los cambios que hayamos hecho desde ese commit !!!!

git reset # Volver a un commit anterior. Se pierden los cambios que hayamos hecho desde ese commit.
git reset --hard ID_COMMIT # Hace un reset a un commit anterior. Se pierden los cambios que hayamos hecho desde ese commit. 

Siempre que hayas commiteado un cambio eso esta guardado, aunque hayas hecho un reset hard.

git reflog # Ver el historial completo de commits que hemos hecho, no solo hasta el último commit.
git reflog --graph # Ver el historial completo de commits que hemos hecho de forma gráfica. Para salir pulsar 'q'.
---------
Ejempolo de reset:
git reset --hard ID_COMMIT1 anterior # Se pieren los cambios que hayamos hecho desde ese commit. 
git chechout ID_COMMIT2 que habiamos eliminado # el main va a estar en un lado y la head apunta a otro lado.
git reset --hard ID_COMMIT2 # volvemos a un commit que habiamos eliminado usando el mismo reset

-------- ALIAS --------
Crear un alias para un comando (util para comandos largos)
git config --global alias.tree "log --graph --decorate --all --oneline" # creamos un alias llamado 'tree' para el comando 

-------- GIT TAG --------
git tag nombre_tag

Los tag se suelen usar para señalar puntos importantes en el tiempo, como por ejemplo una version de un programa.
Buena practica: todos en minuscula y sin espacios. Se pueden usar guiones bajos o guiones medios.


'''
print('Hello Git')
print('¿Que tal el curso?')
# El codigo que creamos va a tener diferentes flujos , y cada rama (flujo) va a tener un nombre diferente