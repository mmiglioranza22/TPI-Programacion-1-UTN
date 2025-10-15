data_50 = {
    "nombre": [
        "Argentina", "Brasil", "Chile", "México", "Estados Unidos",
        "Canadá", "España", "Alemania", "Francia", "Italia",
        "Reino Unido", "Portugal", "Rusia", "China", "Japón",
        "India", "Australia", "Nueva Zelanda", "Sudáfrica", "Egipto",
        "Nigeria", "Marruecos", "Turquía", "Arabia Saudita", "Irán",
        "Irak", "Israel", "Suecia", "Noruega", "Finlandia",
        "Dinamarca", "Países Bajos", "Bélgica", "Suiza", "Polonia",
        "Ucrania", "Grecia", "Hungría", "Austria", "Irlanda",
        "Corea del Sur", "Corea del Norte", "Tailandia", "Vietnam", "Filipinas",
        "Indonesia", "Pakistán", "Bangladés", "Colombia", "Perú"
    ],
    "poblacion": [
        45376763, 213993437, 19116201, 126000000, 331000000,
        38000000, 47351567, 83149300, 67413000, 59554000,
        68207116, 10305564, 144000000, 1411778724, 125800000,
        1393409038, 26000000, 5135300, 59308690, 104000000,
        223000000, 36910558, 85000000, 35600000, 85000000,
        40200000, 9643000, 10500000, 5430000, 5540000,
        5830000, 17400000, 11500000, 8800000, 38000000,
        41000000, 10400000, 9600000, 8900000, 5000000,
        51780000, 26000000, 70000000, 99000000, 113000000,
        276000000, 235000000, 166000000, 51400000, 34000000
    ],
    "superficie": [
        2780400, 8515767, 756102, 1964375, 9833520,
        9984670, 505990, 357022, 551695, 301340,
        243610, 92212, 17098242, 9596961, 377975,
        3287263, 7692024, 268021, 1219090, 1002450,
        923768, 446550, 783562, 2149690, 1648195,
        438317, 22072, 450295, 385207, 338455,
        43094, 41543, 30528, 41285, 312696,
        603628, 131957, 93030, 83879, 70273,
        100210, 120540, 513120, 331212, 300000,
        1910931, 881913, 148460, 1141748, 1285216
    ],
    "continente": [
        "América", "América", "América", "América", "América",
        "América", "Europa", "Europa", "Europa", "Europa",
        "Europa", "Europa", "Europa", "Asia", "Asia",
        "Asia", "Oceanía", "Oceanía", "África", "África",
        "África", "África", "Asia", "Asia", "Asia",
        "Asia", "Asia", "Europa", "Europa", "Europa",
        "Europa", "Europa", "Europa", "Europa", "Europa",
        "Europa", "Europa", "Europa", "Europa", "Europa",
        "Asia", "Asia", "Asia", "Asia", "Asia",
        "Asia", "Asia", "Asia", "América", "América"
    ]
}

# Crear DataFrame
df_50 = pd.DataFrame(data_50)

# Guardar como CSV
csv_path_50 = "/mnt/data/paises_50.csv"
df_50.to_csv(csv_path_50, index=False)

csv_path_50
#menú principal
# ---------------------------
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