#Definimos la url constante o el prefijo de url
prefixUrl = "git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/vega20"


leer = "firmwares_faltantes.txt"

listaString = []
with open(leer) as file:
	for linea in file:
		listaString.append(linea.split())



binario = [] #Almacena el nombre de los archivos binarios
for sublista in listaString:
	for path in sublista:
		binario.append(path[27:])
		print ("Se agregó " + path[27:])

file = open('wgetMe.txt','w')

for bin in binario:
	file.write(prefixUrl + bin + "\n")

file.close()
print ("Se crearon las url exitosamente")



