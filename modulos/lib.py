import csv

def cargar_paises():
	lista = []
	try:
		with open('dataset_base.csv', 'r', newline='') as archivo:
			lector = csv.reader(archivo)
			for fila in lector:
				# Se omite la primer fila que es la que contiene el nombre de las columnas
				if fila[0] == "nombre":
					continue
				else:
					lista.append({"PAIS": fila[0], "POBLACION": int(fila[1]), "SUPERFICIE": int(fila[2]), "CONTINENTE": fila[3]})
		
		return lista[1:]
	except Exception as e:
		print("Error en carga de archivo. Verifique que el formato del archivo CSV con países sea correcto")



def guardar_cambios(archivo_paises):
	with open("dataset_bassse.csv", "w") as archivo:
		archivo.write("nombre,poblacion,superficie,continente\n")
		for pais in archivo_paises:
			archivo.write(f"{pais["PAIS"]},{pais["POBLACION"]},{pais["SUPERFICIE"]},{pais["CONTINENTE"]}\n")


# lista = cargar_paises()

# print(lista)

# guardar_cambios(lista)