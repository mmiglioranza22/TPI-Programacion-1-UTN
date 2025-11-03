import csv



def cargar_paises():
	lista = []
	with open('dataset_base.csv', 'r', newline='') as archivo:
		lector = csv.reader(archivo)
		for fila in lector:
			# Se omite la primer fila que es la que contiene el nombre de las columnas
			if fila[0] == "nombre":
				continue
			else:
				lista.append({"PAIS": fila[0], "POBLACION": int(fila[1]), "SUPERFICIE": int(fila[2]), "CONTINENTE": fila[3]})
	
	return lista[1:]


lista_paises = cargar_paises()

