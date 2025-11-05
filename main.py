from funciones_logica_negocio import cargar_paises, mostrar_menu, mostrar_estadisticas, actualizar_pais, agregar_pais, buscar_pais, filtrar_continente, filtrar_por_rango, guardar_cambios, ordenar_paises
from funciones_validadoras import opcion_valida

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
			
		case "2":
			actualizar_pais(lista_paises)	
			guardar_cambios(lista_paises)
			print("\n===========================================")

		case "3":
			buscar_pais(lista_paises)
			print("\n===========================================")
		
		case "4":
			filtrar_continente(lista_paises)
			print("\n===========================================")
		
		case "5":
			filtrar_por_rango(lista_paises, "POBLACION")	
			print("\n===========================================")

		case "6":
			filtrar_por_rango(lista_paises, "SUPERFICIE")	
			print("\n===========================================")

		case "7":
			ordenar_paises(lista_paises, "NOMBRE")
			print("\n===========================================")

		case "8":
			ordenar_paises(lista_paises, "POBLACION")
			print("\n===========================================")

		case "9":
			ordenar_paises(lista_paises, "SUPERFICIE")
			print("\n===========================================")

		case "10":
			mostrar_estadisticas(lista_paises)
			print("\n===========================================")

		case "0":
			break