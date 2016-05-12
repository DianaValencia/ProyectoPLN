#Esta clase se encarga de extraer los pronombres y limpiar la sentencia de stopwords 
from nltk.corpus import stopwords
import re


class nivelSentencial:

    __patronPronombrePersonal = ""
    __patronPronombreWh = ""
    __patronLimpiarSenteciaPOS = ""
    __archivoPOS = ""
    __listaPronombres = ""
    __listaSentencia = []
    __palabrasStop = []


    def __init__(self):
	#conjunto de palabras de parada
	self.__palabrasStop = stopwords.words('english')

	#Patrones a emplear en este nivel. Se deben reconocer los pronombres a partir de su etiqueta POS
        self.__patronPronombrePersonal = re.compile('PRP*')   
        self.__patronPronombreWh = re.compile('WH*')
        self.__patronLimpiarSentenciaPOS = re.compile('._.')

	#Se abre el archivo que contiene la informacion de las etiquetas POS.
        self.__archivoPOS = open("/priimerproyecto/PLN/analizador/Resultados/resultadoPosSTD.txt", "r+")  

	#Llamado al metodo que ejecutara todo este procedimiento
	self.ejecutar()
	self.__archivoPOS.close()


    #En este metodo se hace el llamado a las operaciones necesarias para generar el resultado ya indicado
    def ejecutar(self):

	numeroSentencia = 0
	sentenciaAGuardar = ""
	pronombresAGuardar = ""
	palabrasSinStop = ""

        sentencia = self.__archivoPOS.readline()
	
	#Se recorre el archivo en busqueda de las propiedades que estamos buscando
        while sentencia != "":
	    pronombresAGuardar = ""
	    palabrasSinStop = ""
	    listaPalabras = sentencia.split(" ")	    
	    for palabraPOS in listaPalabras:
		parejaPOS = palabraPOS.split("_")
		#comienza la extraccion de los pronombres		
		if (self.__patronPronombrePersonal.match(parejaPOS[1])!=None) or (self.__patronPronombreWh.match(parejaPOS[1])!=None):
		    pronombresAGuardar = pronombresAGuardar + " " + palabraPOS.lower()
		#preguntamos si la palabra no es una stopword para guardarla luego en el arreglo junto con su POS
		elif parejaPOS[0].lower() not in self.__palabrasStop:
		    palabrasSinStop = palabrasSinStop + " " + palabraPOS
	
	    #Guardamos los datos que se han capturado hasta el momento
	    self.__listaPronombres = self.limpiarPOS(pronombresAGuardar)
	    numeroSentencia = numeroSentencia + 1	
	    sentenciaAGuardar = str(numeroSentencia) + "|||||||| " + palabrasSinStop + " |||||||| " + self.__listaPronombres 
	    self.__listaSentencia.append(sentenciaAGuardar)

	    #LLame a una nueva linea
	    sentencia = self.__archivoPOS.readline()


    #Limpia la palabra de la etiqueta POS
    def limpiarPOS(self, sentenciaPOS):
	resultadoPalabras = ""
	palabrasPOS = sentenciaPOS.split(" ")
	for parejaPOS in palabrasPOS:
	    palabras = parejaPOS.split("_")
	    resultadoPalabras = resultadoPalabras + " " + palabras[0]		
	return resultadoPalabras	


    #Retorna el resultado de la clase como tal
    def getSentenciaParte1(self):
	return self.__listaSentencia
