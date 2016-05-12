#Modulo para trabajar con expresiones regulares
import re

#Como los resultados del parser contienen tanto los arboles como la relacion entre dependencias, se procede a separar estos resultados
#Creamos primero el patron para identificar el inicio y la parada de la extraccion del subarbol generado
patronInicioArbol = re.compile('\(ROOT')
patronSalto = re.compile('\n')

#Se abren los archivos de lectura y escritura a usar
archivoLectura = open("../Resultados/resultadoParserSTD.txt", "r+")
archivoEscrituraArbol = open("../Resultados/arbolesExtraidosSTD.txt", "w+")
archivoEscrituraDependencias = open("../Resultados/dependenciasExtraidasSTD.txt", "w+")

#leer lineas
linea = archivoLectura.readline()

#Se emplea un centinela para determinar si lo que pasa es en realidad el arbol o no
centinelaArbol = False
centinelaDependencia = False

#Ciclo para ir leyendo el archivo hasta el final
while linea!="":   
    #Si encuentra el patro inicio, cambie la variable a verdadero, sino a falso
    if patronSalto.match(linea)!=None:
        archivoEscrituraArbol.write(linea)
        archivoEscrituraDependencias.write(linea)
        centinelaArbol = False
        centinelaDependencia = True
    elif patronInicioArbol.match(linea)!=None:
        centinelaArbol = True    
        centinelaDependencia = False    

    #Si el centinela es verdadero, pasa la linea del arbol a guardar en el archivo de escritura.De lo contrario, no pasa nada que no sea del arbol
    if centinelaArbol!=False:
        archivoEscrituraArbol.write(linea)
    if centinelaDependencia!=False:
        archivoEscrituraDependencias.write(linea)

    linea = archivoLectura.readline()

#Se cierran los archivos de lectura y escritura que se usaron
archivoLectura.close()
archivoEscrituraArbol.close()
archivoEscrituraDependencias.close()
