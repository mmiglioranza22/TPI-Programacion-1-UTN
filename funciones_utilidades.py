# Se desarrolla una función de ordenamiento con el algoritmo "bubble sort" por restricción del trabajo práctico.
# Normalmente se utilizaría la función sorted e itemgetter para ordenar una lista de diccionarios
# La idea principal de este algoritmo es comparar un elemento con el siguiente según un determinado criterio (mayor/menor)
# Ej: Si el elemento es menor que el siguiente (primer caracter en la tabla ASCII), se lo pone primero y se mueve el elemento mayor una posición en la lista
# Se itera la cantidad de veces necesarias para ordenar toda la lista, y cuando se hace una pasada por la lista sin hacer ningún cambio, la lista estará ordenada
# Se hacen las modificaciones concretas para tomar exclusivamente lista de diccionarios, el elemento de comparación (key) y el sentido del ordenamiento (ascendente/descendente)
def bubble_sort_diccionarios(lista_de_diccionarios, key, sentido="ASCENDENTE"):
	# Se hace una copia de la lista original para no modificar esta última
	lista_copia = list(lista_de_diccionarios)
	# Se utiliza un marcador para saber si se ha realizado un cambio, cuando se haga un recorrido por la lista sin hacer cambios, la lista estará ordenada
	# Se inicializa en True para que entre al menos 1 vez al bucle while
	se_hicieron_cambios = True
	while se_hicieron_cambios:
		# Se cambia a False porque aún no se sabe aún si se hizo un cambio de posición entre elementos
		se_hicieron_cambios = False
		# Esto control de flujo permite ordenar en distintos sentidos (ascendente, descendente)
		if sentido == "ASCENDENTE":
			for indice in range(0, len(lista_copia) - 1):
				# Si se ingresa en el if, asumimos que se hace un cambio
				if lista_copia[indice][key] > lista_copia[indice + 1][key]:
					# Se guarda la referencia del elemento y se hace el cambio (el más chico se pone primero)
					puntero_temporal = lista_copia[indice]
					lista_copia[indice] = lista_copia[indice + 1]
					lista_copia[indice + 1] = puntero_temporal
					se_hicieron_cambios = True
		elif sentido == "DESCENDENTE":
			for indice in range(0, len(lista_copia) - 1):
				# Si se ingresa en el if, asumimos que se hace un cambio (el más grande se pone primero)
				if lista_copia[indice][key] < lista_copia[indice + 1][key]:
					# Se guarda la referencia del elemento y se hace el cambio
					puntero_temporal = lista_copia[indice + 1]
					lista_copia[indice + 1] = lista_copia[indice]
					lista_copia[indice] = puntero_temporal
					se_hicieron_cambios = True
		else:
			print("El criterio elegido no es posible, debe ser ASCENDENTE o DESCENDENTE")

	return lista_copia

# Se desarrolla una función promedio y no se usa mean del módulo statistics por restricción del trabajo práctico.
# Normalmente se preferiría la función mean por estar mejor probada y testeada
def promedio(lista, criterio):
	suma = 0
	for elemento in lista:
		suma = suma + elemento[criterio]
	
	promedio = suma / len(lista)
	return round(promedio, 2)