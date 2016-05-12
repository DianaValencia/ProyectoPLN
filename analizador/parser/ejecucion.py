from nivelSentencial import nivelSentencial
from extraerNER import extraccionNER
from extraerNP import extraccionNP

def ejecutar():
	#Se crean los objetos necesarios para la ejecucion y extraccion de las caracteristicas de las sentencias.
	#Este es el objeto que maneja las caracteristicas de las palabras y los pronombres
	caracteristicasSen = nivelSentencial()

	#Este es el objeto que maneja las caracteristicas de las NER y las RAW de las sentencias 
	caracteristicasNER = extraccionNER("/priimerproyecto/PLN/textoIngresado.txt")

	#Este es el objeto que maneja las caracteristicas de los NP
	caracteristicasNP = extraccionNP("/priimerproyecto/PLN/textoIngresado.txt")


	#Guardamos las caracteristicas necesarias dentro de unas variables adicionales
	listaSentencia = caracteristicasSen.getSentenciaParte1()
	listaNER = caracteristicasNER.getNER()
	listaRAWSen = caracteristicasNER.getSentencias()
	listaNP = caracteristicasNP.getNP()


	#el tamanio de las listas.
	tamanioLista = len(listaSentencia)
        
	sentenciaFinal = ""


	#Abrimos un archivo donde se guardaran los resultados finales.
	archivoFinalSentencia = open("/priimerproyecto/PLN/analizador/Resultados/resultadoSentencias.txt", "w+")

	#Unimos los resultados previos y guardamos en el archivo
        print tamanioLista
        print len(listaNER)
        print len(listaRAWSen)
        print len(listaNP)
        
	cuenta = 0
	for item in range(tamanioLista):
   	    sentenciaFinal = listaSentencia[cuenta] + "|||||||| " + listaNER[cuenta] + "|||||||| " + listaNP[cuenta] + "|||||||| " + listaRAWSen[cuenta] + "\n"
    	    cuenta = cuenta + 1
	    archivoFinalSentencia.write(sentenciaFinal)
	archivoFinalSentencia.close()    
