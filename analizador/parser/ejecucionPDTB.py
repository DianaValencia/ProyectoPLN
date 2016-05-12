import subprocess
import re

class ejecutarPDTB:


    def __init__(self):
		
	subprocess.call(["java", "-jar", "parser.jar", "/priimerproyecto/PLN/analizador/parser/resultadoModelo1.txt"])
	
	self.extraerConectores()


    #Una vez se ha ejecutado el proyecto de pdtb, se procede a extraer las caracteristicas del archivo pipe final. Recorremos el archivo y, por cada sentencia, revisamos si el conector es explicito o implicito, ya que solo se guardan estos conectores. 
    def extraerConectores(self):

	archivoConectores = open("/priimerproyecto/PLN/analizador/Resultados/archivoConectores.txt", "w+")

	lineaSentencia = ""
	
	#Abrimos el archivo donde procedemos a extraer la informacion de pdtb
	archivoParcial = open("/priimerproyecto/PLN/analizador/parser/output/resultadoModelo1.txt.pipe", "r+")

	lineaSentencia = archivoParcial.readline()

        while lineaSentencia != "":
	    guardarSentencia = False	    
	    listaPalabras = re.split("[|]+", lineaSentencia)	 	    

	    for palabras in listaPalabras:
		#comienza la comparacion de los conectores
		if (palabras == "Explicit") or (palabras == "Implicit"):
		    guardarSentencia = True
		    break
	    
	    if guardarSentencia!=False:
	        archivoConectores.write(lineaSentencia)	

	    lineaSentencia = archivoParcial.readline()
	
	#cerramos los archivos
	archivoParcial.close()
	archivoConectores.close()
