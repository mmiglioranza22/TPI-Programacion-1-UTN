import csv, os

def verificar_archivo_existente():
	file_path = "dataset_base.csv"
	if os.path.isfile(file_path):
		return True
	else:
		return False


def cargar_paises():
	lista = []
	try:
		if verificar_archivo_existente():
			with open('dataset_base.csv', 'r', newline='') as archivo:
				lector = csv.reader(archivo)
				for fila in lector:
					# Se omite la primer fila que es la que contiene el nombre de las columnas
					if fila[0] == "nombre":
						continue
					else:
						lista.append({"PAIS": fila[0], "POBLACION": int(fila[1]), "SUPERFICIE": int(fila[2]), "CONTINENTE": fila[3]})
			return lista
	except Exception as e:
		print("Error en carga de archivo. Verifique que el formato del archivo CSV con países sea correcto")



def guardar_cambios(archivo_paises):
	with open("dataset_bassse.csv", "w") as archivo:
		archivo.write("nombre,poblacion,superficie,continente\n")
		for pais in archivo_paises:
			archivo.write(f"{pais["PAIS"]},{pais["POBLACION"]},{pais["SUPERFICIE"]},{pais["CONTINENTE"]}\n")


lista = cargar_paises()

print(lista)

# guardar_cambios(lista)

def agregar_pais(pais):
	pass

def actualizar_pais(pais):
	pass


#coincidencia parcial o exacta (regex)
def buscar_pais(pais):
	pass

def filtrar_paises():
	# mostrar opciones: 
	# filtrar por continente
	# filtrar por rango de población
	# filtrar por rango de superficie
	pass


def ordenar_paises():
	# mostrar opciones: orden ascendente
	# nombre
	# poblacion
	# superficie
	pass

def mostrar_estadisticas():
	# País con mayor y menor población
	# Promedio de población
	# Promedio de superficie
	# Cantidad de países por continente 
	pass

def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Buscar un país por nombre")
    print("2. Filtrar países por continente")
    print("3. Filtrar países por rango de población")
    print("4. Filtrar países por rango de superficie")
    print("5. Ordenar países por nombre")
    print("6. Ordenar países por población")
    print("7. Ordenar países por superficie")
    print("8. Mostrar estadísticas")
    print("0. Salir")