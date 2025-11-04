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
						lista.append({"NOMBRE": fila[0], "POBLACION": int(fila[1]), "SUPERFICIE": int(fila[2]), "CONTINENTE": fila[3]})
			return lista
		else:
			print("\nNo hay archivo csv en el directorio de la aplicación")
			print("\nAgregue un archivo con nombre 'dataset_base.csv' con el formato nombre,poblacion,superficie,continente")
			print("Inicializando lista de países vacía...")
			return lista
	except Exception as e:
		print("Error en carga de archivo. Verifique que el formato del archivo CSV con países sea correcto")

def guardar_cambios(archivo_paises):
	with open("dataset_base.csv", "w") as archivo:
		archivo.write("nombre,poblacion,superficie,continente\n")
		for pais in archivo_paises:
			archivo.write(f"{pais["NOMBRE"]},{pais["POBLACION"]},{pais["SUPERFICIE"]},{pais["CONTINENTE"]}\n")

def validar_numero(cadena):
	return cadena.isdigit() and int(cadena).is_integer() and int(cadena) >= 0

def continente_valido(continente):
	return continente == "América" or continente == "Asia" or continente == "Europa" or continente == "África" or continente == "Oceanía"

def agregar_pais(lista_paises):
	pais_repetido = False
	nombre = input("Por favor ingrese el nombre del país: ").strip()
	while nombre == "":
		nombre = input("Opción inválida. Por favor indíque un país: ").strip()

	poblacion = input("Por favor ingrese la población del país: ").strip()
	while poblacion == "" or (not validar_numero(poblacion)):
		poblacion = input("Opción inválida. Por favor indíque número entero positivo: ").strip()

	superficie = input("Por favor ingrese la superficie del país: ").strip()
	while superficie == "" or (not validar_numero(superficie)):
		superficie = input("Opción inválida. Por favor indíque un número entero positivo: ").strip()

	continente = input("Por favor ingrese el continente del país: ").strip()
	while continente == "" or (not continente_valido(continente)):
		continente = input("Opción inválida. Por favor indíque un continente (América, Asia, África, Oceanía, Europa): ").strip()

	# verificar que el país no exista ya en el archivo
	for nombre_pais in lista_paises:
		if nombre_pais["NOMBRE"].lower() == nombre.lower():
			print("\nYa existe un registro para ese país")
			pais_repetido = True
			break
	
	if not pais_repetido:
		nuevo_pais = {"NOMBRE": nombre, "POBLACION": int(poblacion), "SUPERFICIE": int(superficie), "CONTINENTE": continente}
		lista_paises.append(nuevo_pais)
		print(f"\n'{nombre}' fue ingresado como nuevo país.")

def actualizar_pais(lista_paises):
	nombre = input("Por favor ingrese el nombre del país: ").strip()
	while nombre == "":
		nombre = input("Opción inválida. Por favor indíque un país: ").strip()	
	
	nueva_poblacion = input("Ingrese la nueva población: ")
	while nueva_poblacion == "" or (not validar_numero(nueva_poblacion)):
		nueva_poblacion = input("Opción inválida. Por favor indíque número entero positivo: ").strip()

	nueva_superficie = input("Ingrese la nueva superficie: ")
	while nueva_superficie == "" or (not validar_numero(nueva_superficie)):
		nueva_superficie = input("Opción inválida. Por favor indíque un número entero positivo: ").strip()

	encontrado = False
	for pais in lista_paises:
		if pais["NOMBRE"].lower() == nombre.lower():
			encontrado = True
			pais["POBLACION"] = int(nueva_poblacion)
			pais["SUPERFICIE"] = int(nueva_superficie)
			print(f"\n'{nombre}' fue actualizado.")

	if not encontrado:
		print("El país no se encuentra en el archivo")

#coincidencia parcial o exacta (regex)
def buscar_pais(lista_paises):
	nombre = input("Ingrese el país que desee buscar: ")
	while nombre == "" or len(nombre) < 4:
		nombre = input("Opción inválida. Ingreso al menos 4 caracteres: ").strip()	

	for pais in lista_paises:
		if nombre.lower() in pais["NOMBRE"].lower():
			print(f"Datos sobre {pais["NOMBRE"]}")
			print(f"Población: {pais["POBLACION"]}")
			print(f"Superficie: {pais["SUPERFICIE"]}")
			print(f"Continente: {pais["CONTINENTE"]}")

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

def opcion_valida(opcion):
	return opcion == "0" or opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6" or opcion == "7" or opcion == "8" or opcion == "9" or opcion == "10"

def mostrar_menu():
	print("\n--- MENÚ DE OPCIONES ---")
	print("1. Agregar un país")
	print("2. Actualizar datos de un país (población y superficie)")
	print("3. Buscar un país por nombre")
	print("4. Filtrar países por continente")
	print("5. Filtrar países por rango de población")
	print("6. Filtrar países por rango de superficie")
	print("7. Ordenar países por nombre")
	print("8. Ordenar países por población")
	print("9. Ordenar países por superficie")
	print("10. Mostrar estadísticas")
	print("0. Salir")
	
print("===========================================")
print("Bienvenido a la aplicación de países.")
print("===========================================")


lista_paises = cargar_paises()

while True: 
	mostrar_menu()
		
	opcion = input("Por favor, elija una de las opciones sugeridas: ").strip()
	print("")

	while not opcion_valida(opcion):
		print("La opción ingresada no es válida.")
		opcion = input("Por favor, elija una de las opciones sugeridas: ").strip()
		print("\n===========================================\n")
		
	match opcion:
		case "1":
			agregar_pais(lista_paises)
			guardar_cambios(lista_paises)
			print("\n===========================================")
			pass
			
		case "2":
			actualizar_pais(lista_paises)	
			guardar_cambios(lista_paises)
			print("\n===========================================")
			pass

		case "3":
			buscar_pais(lista_paises)
			print("\n===========================================")
			pass
		
		case "4":


			print("\n===========================================")
			pass
		
		case "5":
				
			print("\n===========================================")
			pass

		case "6":

			print("\n===========================================")
			pass

		case "7":

			print("\n===========================================")	
			pass

		case "8":

			print("\n===========================================")	
			pass

		case "9":

			print("\n===========================================")	
			pass

		case "10":

			print("\n===========================================")	
			pass

		case "0":
			break