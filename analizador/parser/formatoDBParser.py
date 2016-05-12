#!/usr/bin/env python

#Importamos las librerias necesarias para la construccion de la parentizacion del resultado del Postag
import sys, re, os, shlex,getopt
from  NLPlib import *
nlp = NLPlib()
import nltk
from subprocess import *

def ejecutar():

 #Primero, debemos crear el postagging de las sentencias


 #Posteriormente se emplea un patron para poder separar de manera adecuada las palabras del texto generado en la operacion anterior
 patronSoloCadenas = re.compile('(\S+)')

 #Se crea un archivo auxiliar con el resultado del postagging parentizado para la correcta lectura con el dbparser
 f = open('/priimerproyecto/PLN/analizador/Resultados/resultadoPosSTD.txt', 'r+')
 f1= open('/priimerproyecto/PLN/analizador/Resultados/POSparentizado.txt', 'w+')

 #Aqui se almacenan las parejas parentizadas
 conjuntoPalabraPOS=[]


 #Comienza el proceso de parentizacion de los POS del archivo ingresado 
 for linea in f:     
     linea1 = linea.strip() 
     listaPalabras = patronSoloCadenas.findall(linea)
     for pareja in listaPalabras:
         if pareja != " ":
             dupla = pareja.split("_")
             conjuntoPalabraPOS.append("(" + dupla[0] + " " + "(" + dupla[1] + ")" + ")")
           
 
 #Cuando ya se tiene guardadas las parejas parentizadas, se construye el parenesis final para pasarlo al dbparaser 

# limite = 0
# f1.write("(")
# for parejita in conjuntoPalabraPOS:          
#     if(parejita != "(. (.))"): 
#         f1.write(str(parejita))
#     else:
#         if(limite!=len(conjuntoPalabraPOS)):
#             f1.write(str(parejita) + ")")
#             f1.write("(")
#     limite += 1
# f1.write(")")

 cuente = 0
 f1.write("(")
 for parejita in conjuntoPalabraPOS:
     if parejita != "(. (.))":
         f1.write(str(parejita))
     else:
         if cuente != (len(conjuntoPalabraPOS) - 1):
	     f1.write(str(parejita) + ")")
	     f1.write("(")
         else:
	     f1.write(str(parejita))
     cuente = cuente + 1
 f1.write(")")



 #Se cierran los archivos de lectura y escritura que se usaron
 f.close()
 f1.close() 

