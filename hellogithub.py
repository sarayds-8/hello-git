''''
1. AUTENTIZACION EN GITHUB

Crear una clave SSH en tu ordenador (ver documentación de github)

2. SUBIR UN REPOSITORIO A GITHUB

git push # Subir los cambios de tu ordenador al repositorio remoto.

3. DESCARGAR UN REPOSITORIO DE GITHUB
git fetch # Descargar los cambios del repositorio remoto a tu ordenador, sin fusionarlos con tu rama actual.
git pull # Descargar los cambios del repositorio remoto a tu ordenador y fusionarlos con tu rama actual.
git clone # Descargar un repositorio remoto a tu ordenador. Se crea una carpeta con el nombre del repositorio y se descargan todos los archivos.

4. SUBIR UN ARCHIVO A GITHUB
git push # Subir un archivo a github. Se sube el archivo al repositorio remoto.

Hacer un fork de un repositorio: copia del repositorio en tu cuenta de github
Obtienes todos los archivos del repositorio de otra persona en tu cuenta de github y en tu ordenador.
Para ello le tienes que dar a fork en la parte superior derecha de la pantalla del repositorio que quieres copiar, 
y luego clonar el repositorio en tu ordenador.

Si no puedes colaborar, lo puedes subir a tu GitHub y luego hacer un pull request al repositorio original.

Importante:
cuando has modificado algo del repoitorio original y lo has subido a tu github, darle siempre a SYNK FORK, para estar seguros de que 
tenemos la version mas actualizada del repositorio original.

Ciclo colabortivo
Cuando quieres que un cambio aparezca en el repositorio original, tienes que hacer un pull request (Importante, primero sincronizar
para estar seguros de que tenemos la versión mas actualizada del repositorio original).
    1. Pull request: se lo pides al propietario del repositorio original para que lo revise y lo acepte.
    2. El propietario del repositorio original revisa el pull request y lo acepta o lo rechaza, puede hacer comentarios y pedir cambios.
    3. Al aceptar, tiene que fusionar el pull request con el repositorio original (Merge pull request).
    GitHub te avisa si hay conflictos entre tu pull request y el repositorio original.
    4. Si hay conflictos, tienes que resolverlos y volver a hacer el pull request.

Un pull request no es un push. 

''''
print('Hello GitHub')