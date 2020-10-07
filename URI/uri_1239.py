while True:
	try:
		izinho  = False
		bezinho = False
		resultado = ""

		texto = input()
		for i in range(len(texto)):
			if (texto[i] != '_' and texto[i] != '*'):
				resultado = resultado + texto[i]
			elif (texto[i] == '_' and izinho == False):
				resultado = resultado + "<i>"
				izinho = True
				continue
			elif (texto[i] == '_' and izinho == True):
				resultado = resultado + "</i>"
				izinho = False
				continue
			elif (texto[i] == '*' and bezinho == False):
				resultado = resultado + "<b>"
				bezinho = True
				continue
			elif (texto[i] == '*' and bezinho == True):
				resultado = resultado + "</b>"
				bezinho = False
				continue
		
		print(resultado)

	except EOFError:
		break