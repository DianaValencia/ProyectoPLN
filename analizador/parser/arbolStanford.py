import subprocess

def ejecutar():
	#Se crea el archivo donde se guardara el proceso final de la ejecucion en consola de la consulta
	resultadoParserSTD = open("/priimerproyecto/PLN/analizador/Resultados/resultadoParserSTD.txt", "w")

	#Se hace un llamado para que ejecute el parser de Standford y guarda sus resultados en el archivo resultadoParserSTD
	subprocess.call(["/priimerproyecto/PLN/analizador/Standford/parser/lexparser.sh", "/priimerproyecto/PLN/textoIngresado.txt"], stdout = resultadoParserSTD)

	#Se hace un llamado al archivo que permite extraer los subarboles en otro archivo
	subprocess.call(["python", "/priimerproyecto/PLN/analizador/parser/extraerSubarbolSTD.py"])

	#cerramos el archivo para guardar los cambios y liberar los buffer de IO
	resultadoParserSTD.close()


