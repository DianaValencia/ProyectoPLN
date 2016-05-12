import re
import subprocess


class extraccionNP:

    __resultadoParserSTD = ""
    __rutaArchivoOriginal = ""
    __patronSalto = ""
    __patronTerminal = ""
    __patronNP = ""
    __listaNP = []


    def __init__(self, rutaArchivoOriginal):
	#se guarda la ruta del archivo de origen de consulta
	self.__rutaArchivo = rutaArchivoOriginal

	#Creacion de los patrones necesarios para la busqueda dentro del archivo de arboles
	self.__patronSalto = re.compile('\n')
	self.__patronTerminal = re.compile('(\S+)\)*\)\n')
	self.__patronNP = re.compile('\(NP*')

        #Se llama al metodo encargado de la ejecucion del programa
	self.ejecucion()


    def ejecucion(self):

	#Se llama al metodo encargado de extraer los arboles generados por el parser al pasarle el archivo original
        self.realizarArchivoNP(self.__rutaArchivo)
	
	#Se llama al metodo que recorre el archivo NER 
	self.extraerNP()


    #Este metodo crea un archivo aparte que permite guardar el resultado de la ejecucion del NER
    def realizarArchivoNP(self, cadenaArchivo):
	#Se crea el archivo donde se guardara el proceso final de la ejecucion en consola de la consulta
	resultadoParserSTD = open("/priimerproyecto/PLN/analizador/Resultados/resultadoParserSTD.txt", "w+")

	#Se hace un llamado para que ejecute el parser de Standford y guarda sus resultados en el archivo resultadoParserSTD
	subprocess.call(["/priimerproyecto/PLN/analizador/Standford/parser/lexparser.sh", cadenaArchivo], stdout = resultadoParserSTD)

	#Se hace un llamado al archivo que permite extraer los subarboles en otro archivo
	subprocess.call(["python", "./extraerSubarbolSTD.py"])

	#cerramos el archivo para guardar los cambios y liberar los buffer de IO
	resultadoParserSTD.close()


    #Metodo encargado de depurar el archivo resultadoNP para extraer solo los nodos NP.
    def extraerNP(self):
	#Se abre el archivo donde estan los arboles ya procesados
	archivoALeer = open("/priimerproyecto/PLN/analizador/Resultados/arbolesExtraidosSTD.txt", "r+")
	sentencia = ""
	NPEncontradas = ""
	centinelaSalto = 0
	centinelaNP = False       
	cantidadNP = 0		
	listaNPEncontradas = []

        sentencia = archivoALeer.readline()
	
	#Se recorre el archivo en busqueda de las entidades que estamos buscando
        while sentencia != "":
	    listaPalabras = sentencia.split(" ")   
	    for palabraNP in listaPalabras:		
		if self.__patronSalto.match(sentencia)!=None:
		    centinelaSalto = centinelaSalto + 1
		    centinelaNP = False

		if (palabraNP == "(NP\n") or (palabraNP == "(NP"):
		    cantidadNP = cantidadNP + 1
		    centinelaNP = True
		    centinelaSalto = False 		

		if centinelaNP!=False:
		    if (palabraNP!=""):
			palabraNP.replace("\n", " ")
		        NPEncontradas = NPEncontradas + " " + palabraNP			
		        if (self.__patronTerminal.match(palabraNP)!=None):
			    cantidadNP = cantidadNP - 1
			if (cantidadNP==0):
			    centinelaNP = False

		if centinelaSalto == 2:		    
		    listaNPEncontradas.append(NPEncontradas)
		    centinelaSalto = False
		    NPEncontradas = ""

	    #LLame a una nueva linea
	    sentencia = archivoALeer.readline()
	self.__listaNP = listaNPEncontradas	
	archivoALeer.close()

    #Devuelve una lista de las entidades encontradas
    def getNP(self):
	return self.__listaNP

