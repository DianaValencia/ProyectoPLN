import subprocess

#Se crea el archivo donde se guardara el proceso final de la ejecucion en consola de la consulta
resultadoParserSTD = open("../Resultados/resultadoParserSTD.txt", "w+")

#Se hace un llamado para que ejecute el parser de Standford y guarda sus resultados en el archivo resultadoParserSTD
subprocess.call(["../Jars/parser/lexparser.sh", "../wsj_0008"], stdout = resultadoParserSTD)

#Se hace un llamado al archivo que permite extraer los subarboles en otro archivo
subprocess.call(["python", "./extraerSubarbolSTD.py"])

#cerramos el archivo para guardar los cambios y liberar los buffer de IO
resultadoParserSTD.close()
