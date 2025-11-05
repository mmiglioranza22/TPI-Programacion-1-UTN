
def validar_numero(cadena):
	return cadena.isdigit() and int(cadena).is_integer() and int(cadena) >= 0

def continente_valido(continente):
	return continente == "América" or continente == "Asia" or continente == "Europa" or continente == "África" or continente == "Oceanía" or continente == "Antártida"

def criterio_orden_valido(criterio):
	return criterio == "NOMBRE" or criterio == "POBLACION" or criterio == "SUPERFICIE"

def opcion_valida(opcion):
	return opcion == "0" or opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6" or opcion == "7" or opcion == "8" or opcion == "9" or opcion == "10"
