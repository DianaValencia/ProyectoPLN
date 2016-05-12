from ejecucionPDTB import ejecutarPDTB
from extraerVectorPDTB import vectorPDTB

cadenaFinal = ""

#Se crean las instancias necesarias para el funcionamiento de este modelo
#Primero, se crea la instancia encargada de ejecutar y extraer los conectores y sus caracteristicas acorde al corpus pdtb
objetoPDTB = ejecutarPDTB()

#Luego, se hace una clasificacion del objeto. Para ellos se crea una instancia que guarda todos estos atributos
objetoVectorPDTB = vectorPDTB()

#Se recuperan los vectores desde el objeto que se crea con anterioridad y luego se guardan en un archivo.

cadenaFinal = objetoVectorPDTB.armarSentencias()

archivoModelo1 = open("/priimerproyecto/PLN/analizador/parser/resultadoModelo1.txt", "w+")
archivoModelo1.write(cadenaFinal)
archivoModelo1.close()
