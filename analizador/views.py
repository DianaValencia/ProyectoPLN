from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import parser.arbolStanford as aS
import parser.posStandford as pS
import parser.extraerSubarbolSTD as eS
import parser.formatoDBParser as fP
import parser.arbolBikel as aB
import parser.parseval as pV
import parser.parsevalBikel as pB
import parser.ejecucion as eJ
from Tkinter import Tk
from tkFileDialog import askopenfilename

# Create your views here.
@csrf_exempt
def analizadorP(request):
	print(request.method)
	if request.method == "POST":
		textoIngresado = request.POST.get('query')
		parserSeleccionado = request.POST.get('parserSelect')
		crearArchivo(str(textoIngresado))
		if parserSeleccionado=="Stanford":
			aS.ejecutar()
			pS.ejecutar()
			eS.ejecutar()
			tag='\n'.join(open('/priimerproyecto/PLN/analizador/Resultados/resultadoPosSTD.txt').readlines())
			dependencias='\n'.join(open('/priimerproyecto/PLN/analizador/Resultados/dependenciasExtraidasSTD.txt').readlines())
			arbol='\n'.join(open('/priimerproyecto/PLN/analizador/Resultados/arbolesExtraidosSTD.txt').readlines())
			template_project = loader.get_template("ventanaStanford.html")
			context_project = Context({'textoCampo': textoIngresado, 'campoTag': tag, 'campoParse': arbol, 'campoDependencias': dependencias, 'req':True})
		else:
			pS.ejecutar()
			fP.ejecutar()
			aB.ejecutar()
			arbol='\n'.join(open('/priimerproyecto/PLN/analizador/Resultados/POSparentizado.txt.parsed').readlines())
			template_project = loader.get_template("ventanaBikel.html")
			context_project = Context({'textoCampo': textoIngresado,'campoParse': arbol, 'req':True})
 
	else: 
		template_project = loader.get_template("ventanaStanford.html")
		context_project = Context({'textoCampo': 'She has finished her homework.', 'campoTag': 'Ponga aqui el postagging', 'campoParse': 'Ponga aqui el parse', 'campoDependencias': 'Ponga aqui las dependencias'})

	return HttpResponse(template_project.render(context_project))


@csrf_exempt
def parseval(request): 
	if request.method == "POST":
		rutaArchivoLectura=seleccionarArchivo()
		rutaGoldStandard=seleccionarArchivo() 
		archivo='\n'.join(open(rutaArchivoLectura).readlines())
		crearArchivo(str(archivo))
		aS.ejecutar()
		pS.ejecutar()
		eS.ejecutar()
                fP.ejecutar()
		aB.ejecutar()
		rutaArbolStanford = '/priimerproyecto/PLN/analizador/Resultados/arbolesExtraidosSTD.txt'
		rutaArbolBikel = '/priimerproyecto/PLN/analizador/Resultados/POSparentizado.txt.parsed'                	
		pV.parseval(rutaArbolStanford, rutaGoldStandard,"") 
		pB.parseval(rutaArbolBikel, rutaGoldStandard,"")
		analisis='\n'.join(open('/priimerproyecto/PLN/analizador/Resultados/estadisticas.txt').readlines())
		analisisBikel='\n'.join(open('/priimerproyecto/PLN/analizador/Resultados/estadisticasBikel.txt').readlines())
		template_project = loader.get_template("parseval.html")
		context_project = Context({'textoCampo': archivo, 'campoEvalStanford':analisis, 'campoEvalBikel':analisisBikel})
	else:
		template_project = loader.get_tempate("parseval.html")
		context_project = Context({'campoEvalStanford':'', 'campoEvalBikel':''})
	return HttpResponse(template_project.render(context_project))

@csrf_exempt
def features(request): 
        if request.method == "POST":
		textoIngresado = request.POST.get('query')
		crearArchivo(str(textoIngresado))
                aS.ejecutar()
                pS.ejecutar() 
                eS.ejecutar()
                eJ.ejecutar()
                printFeatures = '\n'.join(open('/priimerproyecto/PLN/analizador/Resultados/resultadoSentencias.txt').readlines())
                template_project = loader.get_template("features.html")
	        context_project = Context({'textoCampo': textoIngresado, 'campoFeatures': printFeatures})
	else: 
		template_project = loader.get_template("features.html")
		context_project = Context({'textoCampo': 'She has finished her homework.', 'campoFeatures':''})

	return HttpResponse(template_project.render(context_project))
	
def crearArchivo(texto):
	archivoLectura = open('textoIngresado.txt', 'w')
	archivoLectura.write(texto)
	archivoLectura.close()

#Devuelve la ruta del archivo seleccionado
def seleccionarArchivo():
        ventana = Tk()
        ventana.withdraw() # we don't want a full GUI, so keep the root window from appearing
	filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        ventana.destroy()
	return filename
