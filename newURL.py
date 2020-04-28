def leerTxt(ruta):
	listaString = []
	with open(ruta) as file:
		for linea in file:
			listaString.append(linea.split())
	return listaString

def getURL(listaString):
	#Captura las urls de un txt y las escribe en otro
	urls = []
	for sublista in listaString:
		for cadena in sublista:
			if(cadena[0:4] == "http"):
				urls.append(cadena)
				print ("Se agregó la URL " + cadena)
	return urls

def getISBN(listaString):
	#Captura el ISBN de la URL
	isbn = []
	for sublista in listaString:
		for cadena in sublista:
			if(cadena[0:4] == "http"):
				isbn.append(cadena[-17:])
				#obtengo ISBN de la url
				print ("Se agregó la URL " + cadena[-17:])
	return isbn



#Escribiendo un nuevo archivo con las url...
def escribirArchivo(isbn):
	f=open("urls.txt","w")
	for num in isbn:
		f.write("https://link.springer.com/content/pdf/10.1007%2F"+num+".pdf"+"\n")

	f.close()
	print ("Archivo creado con éxito")


print ("""
	==============================================
	==================DETECT URL==================
	==============================================

	DISCLAIMER: Esta herramienta fue diseñada con el propósito de contribuir
	en el proceso de automatización de la descarga de libros PDF publicados
	por la editorial STINGER. En ningún caso fue pensada como una herramienta
	maliciosa.

	Considere que una vez que obtenga las URL limpias en un archivo de texto
	deberá hacer uso de wget -i archivoConUrl.txt para descargarlas.
	""")

try:
	ruta = input("Escriba la ruta del archivo:")
	listaString = leerTxt(ruta)
	isbn = getISBN(listaString)
	escribirArchivo(isbn)
except Exception as e:
	raise e#print ("Ha ocurrido un error inesperado\n")
finally:
	print ("Goodbye")

	