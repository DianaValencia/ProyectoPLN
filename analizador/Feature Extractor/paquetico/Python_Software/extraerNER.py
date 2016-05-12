#Esta clase se encarga de generar dos cosas: La lista de NER de las sentencias y las sentencias como tal (el RAW).
from nltk.tokenize import sent_tokenize
import subprocess



class extraccionNER:

    __resultadoNER = ""
    __rutaArchivo = ""
    __listaNER = []
    __listaSentencias = []


    def __init__(self, rutaArchivoOriginal):
	self.__rutaArchivo = rutaArchivoOriginal
	
        #Se llama al metodo encargado de la ejecucion del programa
	self.ejecucion()


    def ejecucion(self):

	#Se llama al metodo encargado de extraer las NER del archivo
        self.realizarArchivoNER(self.__rutaArchivo)
	
	#Se llama al metodo que recorre el archivo NER 
	self.extraerNER()

	#Se llama al metodo que extrae las sentencias
	self.extraerSentencia()


    #Este metodo crea un archivo aparte que permite guardar el resultado de la ejecucion del NER
    def realizarArchivoNER(self, cadenaArchivo):
	#Se crea el archivo donde se guardara el proceso final de la ejecucion en consola de la consulta
	resultadoNER = open("/priimerproyecto/PLN/analizador/Resultados/resultadoNER.txt", "w+")

	subprocess.call(["/priimerproyecto/PLN/analizador/Standford/NER/ner2.sh", cadenaArchivo], stdout = resultadoNER)

	#cerramos el archivo para guardar los cambios y liberar los buffer de IO
	resultadoNER.close()


    #Metodo encargado de depurar el archivo resultadoNER para extraer solo las sentencias.
    def extraerNER(self):
	archivoALeer = open("/priimerproyecto/PLN/analizador/Resultados/resultadoNER.txt", "r+")
	sentencia = ""
	entidadesEncontradas = ""

        sentencia = archivoALeer.readline()
	
	#Se recorre el archivo en busqueda de las entidades que estamos buscando
        while sentencia != "":
	    entidadesEncontradas = ""
	    listaPalabras = sentencia.split(" ")   
	    for palabraNER in listaPalabras:
		parejaNER = palabraNER.split("/")
		#comienza la extraccion de las entidades preguntando si son diferentes a O		
		if (parejaNER[0] != "\n"):
		    if (parejaNER[1] != "O"):
		        entidadesEncontradas = entidadesEncontradas + ", " + parejaNER[0]
	
	    #Guardamos los datos que se han capturado hasta el momento
	    self.__listaNER.append(entidadesEncontradas)

	    #LLame a una nueva linea
	    sentencia = archivoALeer.readline()
	
	archivoALeer.close()	   


    #Metodo encargado de separar las sentecias del archivo
    def extraerSentencia(self):
	archivoALeer = open(self.__rutaArchivo, "r+")
	sentencia = ""
	sentenciasEncontradas = ""

        sentencia = archivoALeer.readline()
	
	#Se recorre el archivo en busqueda de las sentencias que estamos buscando
        while sentencia != "":
	    if sentencia!="\n":
	        sentenciasEncontradas = sent_tokenize(sentencia)
	
	        #Guardamos los datos que se han capturado hasta el momento
	        self.__listaSentencias.extend(sentenciasEncontradas)

	    #LLame a una nueva linea
	    sentencia = archivoALeer.readline()

	archivoALeer.close()


    #Devuelve una lista de las entidades encontradas
    def getNER(self):
	return self.__listaNER


    #Devuelve una lista de las sentencias contenidas en el documento	
    def getSentencias(self):
	return self.__listaSentencias
