import subprocess
import re

class vectorPDTB:

    __listaExplicitos = []
    __listaImplicitos = []
    __numeroSentenciaConector = 0    
    __relacionConector = ""
    __tipoConector = ""
    __conectorPOS = ""
    __nombreConector = ""
    __argumento1 = ""
    __argumento1POS = ""
    __argumento2 = ""
    __argumento2POS = ""


    def __init__(self):
	
	#Se llama el archivo encargado de ejecutar esta clase
	self.ejecutar()


    #Este metodo sirve para ir guardando en dos listas diferentes las lineas del archivo, distinguiendo entre explicitos e implicitos
    def ejecutar(self):

	lineaSentencia = ""
	
	#Se abre el archivo y se pregunta si el primer elemento es explicito o implicito para guardarlo en una lista aparte
	archivoALeer = open("/priimerproyecto/PLN/analizador/Resultados/archivoConectores.txt", "r+")

	lineaSentencia = archivoALeer.readline()

	while lineaSentencia!="":
	    listaPalabras = re.split("[|]+", lineaSentencia)	 	

	    for palabras in listaPalabras:
		#comienza la comparacion de los conectores
		if (palabras == "Explicit"):
		    self.__listaExplicitos.append(lineaSentencia)
		    break
		else:
		    if (palabras == "Implicit"):
			self.__listaImplicitos.append(lineaSentencia)
			break

	    lineaSentencia = archivoALeer.readline()
	
	#cerramos los archivos
	archivoALeer.close()


    #Aqui se pasan ambas listas y se procede a reacomodar los resultados encontrados. Retorna un string
    def armarSentencias(self):

	cadenaFinal = ""

	#Verificamos si la lista es vacia y si no, procedemos a recorrerla. Se hace para ambos casos 
	if (len(self.__listaExplicitos)!=0):
	    for cadenaExplicita in self.__listaExplicitos:
		self.dividirSentenciaExplicita(cadenaExplicita)
		cadenaFinal = cadenaFinal + self.__numeroSentenciaConector + " |||||||| " + self.__relacionConector + " |||||||| " + self.__tipoConector + " |||||||| " + self.__nombreConector + " |||||||| " + self.__conectorPOS + " |||||||| " + self.__argumento1 + " |||||||| " + self.__argumento1POS + " |||||||| " + self.__argumento2 + " |||||||| " + self.__argumento2POS + " \n "


	if (len(self.__listaImplicitos)!=0):
	    for cadenaImplicita in self.__listaImplicitos:
		self.dividirSentenciaImplicita(cadenaImplicita)
		cadenaFinal = cadenaFinal + self.__relacionConector + " |||||||| " + self.__tipoConector + " |||||||| " + self.__conectorPOS + " |||||||| " + self.__argumento1 + " |||||||| " + self.__argumento1POS + " |||||||| " + self.__argumento2 + " |||||||| " + self.__argumento2POS + " \n "

	return cadenaFinal


    #Este metodo ayuda a partir la cadena que contiene la informacion del conector explicito. 
    def dividirSentenciaExplicita(self, cadenaParcialVieja):	
	cadenaParcial = ""
	cadenaParcial = re.split("[|]+", cadenaParcialVieja)
        self.__numeroSentenciaConector = cadenaParcial[3]    
        self.__relacionConector = cadenaParcial[0]    
        self.__tipoConector = cadenaParcial[5]  
	self.__conectorPOS = self.extraerPOS(cadenaParcial[2])  
        self.__nombreConector = cadenaParcial[2]
	if (len(cadenaParcial)>=13):
            self.__argumento1 = cadenaParcial[8]
            self.__argumento1POS = self.extraerPOS(cadenaParcial[8])    
            self.__argumento2 = cadenaParcial[11]
	    self.__argumento2POS = self.extraerPOS(cadenaParcial[11])
	else:
            self.__argumento1 = cadenaParcial[9]
            self.__argumento1POS = self.extraerPOS(cadenaParcial[9])    
            self.__argumento2 = "Null"
	    self.__argumento2POS = "Null"


    #Este metodo ayuda a partir la cadena que contiene la informacion del conector explicito. 
    def dividirSentenciaImplicita(self, cadenaParcialVieja):	
	cadenaParcial = ""
	cadenaParcial = re.split("[|]+", cadenaParcialVieja)
	print cadenaParcial
        self.__relacionConector = cadenaParcial[0]    
        self.__tipoConector = cadenaParcial[1]  
	self.__conectorPOS = self.extraerPOS(cadenaParcial[1])  
        self.__argumento1 = cadenaParcial[4]
        self.__argumento1POS = self.extraerPOS(cadenaParcial[4])    
        self.__argumento2 = cadenaParcial[7]
	self.__argumento2POS = self.extraerPOS(cadenaParcial[7])


    #Este metodo ayuda a transformar la informacion obtenida en su respectivo POS
    def extraerPOS (self, cadenaSinPOS):
	cadenaTemporal = ""	

	#Se debe guardar en un archivo debido a que el programa POS de Stanford solo recibe archivos para ser tratados
	archivoTemporal = open("/priimerproyecto/PLN/analizador/Resultados/archivoTemporalPOS.txt", "w")
	archivoTemporal.write(cadenaSinPOS)
	archivoTemporal.close()

	#Se llama a los procesos encargados de realizar el POS
	resultadoPosSTD = open("/priimerproyecto/PLN/analizador/Resultados/resultadoPosSTD.txt", "w")
	subprocess.call(["/priimerproyecto/PLN/analizador/Standford/POS/stanford-postagger2.sh", "/priimerproyecto/PLN/analizador/Standford/POS/models/english-left3words-distsim.tagger", "/priimerproyecto/PLN/analizador/Resultados/archivoTemporalPOS.txt"], stdout = resultadoPosSTD)
	resultadoPosSTD.close()
	
	#Extraemos el resultado del archivo final
	archivoTemporalDos = open("/priimerproyecto/PLN/analizador/Resultados/resultadoPosSTD.txt", "r+")
	cadenaTemporal = archivoTemporalDos.readline()
	cadenaTemporal = cadenaTemporal.replace('\n', '')
	archivoTemporal.close()

	#retornamos el resultado final
	return cadenaTemporal

