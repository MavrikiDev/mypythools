# mypythools
Este repositorio contiene herramientas que desarrollo conforme necesito satisfacer una necesidad determinada.

newURL.py fue diseñado para automatizar el proceso de descarga de los libros en formato PDF publicaods por la editorial Stinger.
Si usted copia el archivo PDF que contiene los links y los libros a un txt, obtendrá las urls separadas junto con todo el contenido del texto
Este script lo que hace es obtener esas URLs limpias, extraer el ISBN de cada libro y, con el ISBN, construir las URLs de descarga
directa en un nuevo archivo txt para que esté listo para ser usado por WGET. Considere que los links del PDF no son directos y por eso es necesario construir la URL.
