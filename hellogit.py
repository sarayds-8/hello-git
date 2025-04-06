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
git checkout hellogit2.py # Volver a un commit anterior (situarnos en un punto concreto). CAMBIAS EL PUNTERO (HEAD).
¡¡¡¡ Se pierden los cambios que hayamos hecho desde ese commit !!!!

git reset # Volver a un commit anterior. Se pierden los cambios que hayamos hecho desde ese commit.
git reset --hard ID_COMMIT # Hace un reset a un commit anterior. Se pierden los cambios que hayamos hecho desde ese commit. 

Siempre que hayas commiteado un cambio eso esta guardado, aunque hayas hecho un reset hard.

git reflog # Ver el historial completo de commits que hemos hecho, no solo hasta el último commit.
git reflog --graph # Ver el historial completo de commits que hemos hecho de forma gráfica. Para salir pulsar 'q'.
---------
Ejempolo para deshacer un reset:
git reset --hard ID_COMMIT1 anterior # Se pieren los cambios que hayamos hecho desde ese commit. 
git chechout ID_COMMIT2 que habiamos eliminado # el main va a estar en un lado y la head apunta a otro lado.
git reset --hard ID_COMMIT2 # volvemos a un commit que habiamos eliminado usando el mismo reset


1º VAMOS A LA RAMA QUE QUEREMOS VOLVER A UN COMMIT ANTERIOR (SWITCH)
2º HACEMOS RECET A ESE COMMIT ANTERIOR

SI HACEMOS CHECKOUT Y RESET A LA VEZ, LO QUE HACEMOS ES VOLVER A UN COMMIT ANTERIOR Y CREAR UNA NUEVA RAMA EN ESE COMMIT ANTERIOR
PERO NO ESTAMOS ELIMINANDO COMMITS DE LA RAMA PRINCIPAL.

-------- ALIAS --------
Crear un alias para un comando (util para comandos largos)
git config --global alias.tree "log --graph --decorate --all --oneline" # creamos un alias llamado 'tree' para el comando 

-------- GIT TAG --------
git tag nombre_tag

Los tag se suelen usar para señalar puntos importantes en el tiempo, como por ejemplo una version de un programa.
Buena practica: todos en minuscula y sin espacios. Se pueden usar guiones bajos o guiones medios.

------- RAMAS ------
Las ramas son lo equivalenta a trabajos temporales. En algun momento que tengamos todo el codigo lo querremos unir a la rama principal.

git branch nombre_rama # Crear una rama nueva. Se crea una copia del commit en el que estamos.
git branch # Ver las ramas que tenemos. La rama en la que estamos es la que tiene un asterisco al lado.
git switch nombre_rama # Cambiar de rama. Cambiamos a la rama que queramos.

git merge nombre_rama # Unir una rama a la rama en la que estamos. Se unen los cambios de la rama que queremos a la rama en la que estamos.

git stash # se guardan los cambios sin hacer un commit. Un commit deberia ser algo que este terminado y correcto.
git stash list # Ver los cambios que tenemos guardados en el stash.
git stash pop # Recuperar los cambios que tenemos guardados en el stash. Se eliminan los cambios del stash.
git stash apply # Recuperar los cambios que tenemos guardados en el stash. Se mantienen los cambios en el stash.
git stash drop # Eliminar los cambios que tenemos guardados en el stash. Se eliminan los cambios del stash.

Cuando ya hemos hecho merge entre la nueva rama y la rama principal, podemos eliminar la rama nueva.
git branch -d nombre_rama # Eliminar la rama nueva. Se eliminan los cambios de la rama nueva.

--------- CONFLICTOS -----------
git diff nombre_rama # Ver los cambios que hay entre la rama en la que estamos y la rama que queremos comprobar.


-------- CHECKOUT -----------
El checkout se usa para cambiar de rama o para volver a un commit anterior. Tanto a nivel de rama como de un archivo.
'''
print('Hello Git')
print('¿Que tal el curso?')
# El codigo que creamos va a tener diferentes flujos , y cada rama (flujo) va a tener un nombre diferente

