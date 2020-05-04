# mypythools
Este repositorio contiene herramientas que desarrollo conforme necesito satisfacer una necesidad determinada.

----------------------------------------------NEWURL---------------------------------------------------

newURL.py fue diseñado para automatizar el proceso de descarga de los libros en formato PDF publicaods por la editorial Stinger.
Si usted copia el archivo PDF que contiene los links y los libros a un txt, obtendrá las urls separadas junto con todo el contenido del texto
Este script lo que hace es obtener esas URLs limpias, extraer el ISBN de cada libro y, con el ISBN, construir las URLs de descarga
directa en un nuevo archivo txt para que esté listo para ser usado por WGET. Considere que los links del PDF no son directos y por eso es necesario construir la URL.


----------------------------------------FIXFIRMWARE------------------------------------------------------------

Esta herramienta, en su primera versión un poco precaria y puramente lineal, surgió ante una urgencia que tuve con Debian y los drivers privativos... Encendí mi equipo y me encontraba con el entorno gráfico inutilizable. Al hacer unas revisiones por consola, uno de los problemas que tuve, una vez más, fue con los drivers privativos de video. En concreto, firmwares faltantes (en este repo, en firmwares-faltantes.txt). A partir de ahí, y con la consola como única herramienta, me propuse descargar aquellos binarios que faltaban, pero necesitaba automatizar el proceso rápidamente para no estar construyendo de forma manual la URL con la descarga directa. Esto es lo que sencillamente hace este script.

downloadFirmware.py establece en una variable el prefijo de URL, o la porción de URL estática que compartirán todos los binarios en común. De esa URL de descarga directa, lo único que varía es el nombre del binario. Luego, lee el archivo con el path de los firmwares faltantes, para recorrerlos y capturar únicamente su nombre (esto claramente puede ser mejorado generalizándolo más, por ejemplo, que reciba directamente el nombre de los binarios). Una vez ya tiene los nombres en una lista, construye la URL final de descarga directa y las escribe en un archivo de texto que se llamará, ni más ni menos, "wgetME.txt". Esto como una pequeña gracia... En lugar de readme, wgetme... Entonces, este archivo final, claramente será pasado a WGET para que haga el trabajo final. 
