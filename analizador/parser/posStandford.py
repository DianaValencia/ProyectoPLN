import subprocess

def ejecutar():
	#Se crea el archivo donde se guardara el proceso final de la ejecucion en consola de la consulta
	resultadoPosSTD = open("/priimerproyecto/PLN/analizador/Resultados/resultadoPosSTD.txt", "w")

	subprocess.call(["/priimerproyecto/PLN/analizador/Standford/POS/stanford-postagger2.sh", "/priimerproyecto/PLN/analizador/Standford/POS/models/english-left3words-distsim.tagger", "/priimerproyecto/PLN/textoIngresado.txt"], stdout = resultadoPosSTD)

	#cerramos el archivo para guardar los cambios y liberar los buffer de IO
	resultadoPosSTD.close()
	#subprocess.call(["clear"])


