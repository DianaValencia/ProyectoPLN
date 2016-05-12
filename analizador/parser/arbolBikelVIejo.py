#!/usr/bin/env python

import sys, re, os, shlex,subprocess,getopt
from per1 import partition, textToTree, clean, getSegments, evaluate, printList, printDisagreements
from  NLPlib import *
nlp = NLPlib()
import nltk
import per1
from subprocess import *

def ejecutar():
    global pareja1
    f = open('/home/cristian/Descargas/PLN/analizador/Resultados/sentenciasSeparadas.txt', 'r+')
    f1= open('/home/cristian/Descargas/PLN/analizador/Resultados/arbolBikel.txt', 'w+')
    pareja1=[]
    for line in f: 
        print line 
        line=line.strip() 
        tokens = nlp.tokenize(line)
        tagged = nlp.tag(tokens)
        i=0
        while i < len(tokens):
            if tokens[i] != " " and tagged[i] != " ":
                pareja1.append("("+tokens[i]+ " "+"("+tagged[i]+")"+")")
                print "(",tokens[i],"(",tagged[i],")",")"
            i+=1   
         
    print 'esta es el arreglo guardado'
    f1.write("(")
    for parejita in pareja1:
        if parejita != "(. (.))": 
            f1.write(str(parejita))
        else:
            f1.write(str(parejita+")"))
            f1.write(str("("))
    f.close()
    f1.close() 

