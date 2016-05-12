#Se importan los modulos necesarios para el desarrollo de la ejecucion
import subprocess

#Se llama al encargado de transformar el resultado del texto POS en un  texto con POS parentizado
subprocess.call(["python", "/priimerproyecto/PLN/analizador/parser/formatoDBParser.py"])

#Luego, se llama la funcion encargada de parsear la informacion anterior y asi obtener el arbol Bikel
#subprocess.call(["java", "-server", "-Xms1024m", "-Xmx1024m", "-cp", "../Bikel/dbparser/dbparser.jar", "-Dparser.settingsFile=../Bikel/dbparser/settings/bikel.properties", "danbikel.parser.Parser", "-is", "../Bikel/wsj-02-21.obj.gz", "-sa", "../Resultados/POSparentizado.txt"])

subprocess.call(["/priimerproyecto/PLN/analizador/Bikel/dbparser/bikel.sh", "/priimerproyecto/PLN/analizador/Bikel/dbparser/settings/bikel.properties", "/priimerproyecto/PLN/analizador/Bikel/wsj-02-21.obj.gz", "/priimerproyecto/PLN/analizador/Resultados/POSparentizado.txt"])
