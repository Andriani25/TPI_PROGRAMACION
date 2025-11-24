"""
Sistema de Gestión de Datos de Países
Trabajo Práctico Integrador - Programación 1
"""

import os

# ==================== DATOS POR DEFECTO ====================

PAISES_DEFAULT = [
    'nombre,poblacion,superficie,continente',
    'Argentina,45376763,2780400,América del Sur',
    'Japón,125800000,377975,Asia',
    'Brasil,213993437,8515767,América del Sur',
    'Alemania,83149300,357022,Europa'
]

# ==================== FUNCIONES DE CARGA Y GUARDADO ====================

def crear_csv_default(nombre_archivo):
    """
    Crea un archivo CSV con datos por defecto si no existe.
    
    Args:
        nombre_archivo (str): Ruta del archivo CSV
    """
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        for linea in PAISES_DEFAULT:
            archivo.write(linea + '\n')
    
    print(f"✓ Archivo '{nombre_archivo}' creado con datos por defecto.")


def parsear_linea_csv(linea):
    """
    Convierte una línea CSV en una lista de valores.
    
    Args:
        linea (str): Línea del archivo CSV
    
    Returns:
        list: Lista con los valores separados por coma
    """
    valores = []
    valor_actual = ''
    
    for caracter in linea:
        if caracter == ',':
            valores.append(valor_actual.strip())
            valor_actual = ''
        elif caracter != '\n' and caracter != '\r':
            valor_actual = valor_actual + caracter
    
    # Agregar el último valor
    if valor_actual:
        valores.append(valor_actual.strip())
    
    return valores


def cargar_paises_desde_csv(nombre_archivo):
    """
    Carga los datos de países desde un archivo CSV.
    Si el archivo no existe, lo crea con datos por defecto.
    
    Args:
        nombre_archivo (str): Ruta del archivo CSV
    
    Returns:
        list: Lista de diccionarios con información de países
    """
    paises = []
    
    # Verificar si el archivo existe
    if not os.path.exists(nombre_archivo):
        print(f"⚠ Archivo '{nombre_archivo}' no encontrado.")
        crear_csv_default(nombre_archivo)
    
    # Abrir y leer el archivo
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    
    # La primera línea contiene los encabezados
    if len(lineas) == 0:
        print("⚠ El archivo está vacío.")
        return paises
    
    encabezados = parsear_linea_csv(lineas[0])
    
    # Procesar cada línea de datos (desde la segunda línea)
    for i in range(1, len(lineas)):
        linea = lineas[i].strip()
        if linea:  # Ignorar líneas vacías
            valores = parsear_linea_csv(linea)
            
            # Verificar que tenga los 4 campos esperados
            if len(valores) == 4:
                poblacion_str = valores[1].strip()
                superficie_str = valores[2].strip()
                
                # Validar que los campos numéricos sean válidos
                if poblacion_str.isdigit() and superficie_str.isdigit():
                    pais = {
                        'nombre': valores[0].strip(),
                        'poblacion': int(poblacion_str),
                        'superficie': int(superficie_str),
                        'continente': valores[3].strip()
                    }
                    paises.append(pais)
                else:
                    print(f"⚠ Fila con formato inválido ignorada: {linea}")
            else:
                print(f"⚠ Fila con número incorrecto de campos: {linea}")
    
    print(f"✓ Se cargaron {len(paises)} países correctamente.")
    
    return paises


def reescribir_csv(paises, nombre_archivo):
    """
    Guarda la lista de países en un archivo CSV.
    
    Args:
        paises (list): Lista de diccionarios con datos de países
        nombre_archivo (str): Ruta del archivo CSV
    """
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        # Escribir encabezado
        archivo.write('nombre,poblacion,superficie,continente\n')
        
        # Escribir cada país
        for pais in paises:
            linea = pais['nombre'] + ',' + str(pais['poblacion']) + ',' + str(pais['superficie']) + ',' + pais['continente'] + '\n'
            archivo.write(linea)
    
    print("✓ Datos guardados correctamente.")


# ==================== FUNCIONES DE VALIDACIÓN ====================

def validar_entero_positivo(texto_entrada, mensaje_campo):
    """
    Valida que la entrada sea un número entero positivo.
    
    Args:
        texto_entrada (str): Texto ingresado por el usuario
        mensaje_campo (str): Nombre del campo para mensajes de error
    
    Returns:
        tuple: (bool, int) - (es_valido, valor_convertido)
    """
    if not texto_entrada:
        print(f"⚠ {mensaje_campo} no puede estar vacío.")
        return False, 0
    
    if not texto_entrada.isdigit():
        print(f"⚠ {mensaje_campo} debe ser un número entero válido.")
        return False, 0
    
    valor = int(texto_entrada)
    if valor < 0:
        print(f"⚠ {mensaje_campo} debe ser un número positivo.")
        return False, 0
    
    return True, valor


# ==================== FUNCIONES DE GESTIÓN DE PAÍSES ====================

def agregar_pais(paises):
    """
    Agrega un nuevo país a la lista.
    No permite campos vacíos.
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- AGREGAR NUEVO PAÍS ---")
    
    # Validar nombre (no vacío)
    nombre = ""
    while not nombre:
        nombre = input("Nombre del país: ").strip()
        if not nombre:
            print("⚠ El nombre no puede estar vacío.")
    
    # Validar población
    poblacion = 0
    valido = False
    while not valido:
        pob_str = input("Población: ").strip()
        valido, poblacion = validar_entero_positivo(pob_str, "La población")
    
    # Validar superficie
    superficie = 0
    valido = False
    while not valido:
        sup_str = input("Superficie (km²): ").strip()
        valido, superficie = validar_entero_positivo(sup_str, "La superficie")    
    
    continentes = [
        "África",
        "América del Norte",
        "América del Sur",
        "Antártida",
        "Asia",
        "Europa",
        "Oceanía"
    ]    
    continente = ""

    while True:
        print("Continentes disponibles:")
        for i, cont in enumerate(continentes, start=1):
            print(f"{i}. {cont}")
        cont_opcion = input("Seleccione el número del continente: ").strip()
        if cont_opcion.isdigit():
            cont_index = int(cont_opcion) - 1
            if 0 <= cont_index < len(continentes):
                continente = continentes[cont_index]
                break
        print("⚠ Opción inválida. Por favor, intente nuevamente.")
    
    # Crear y agregar el país
    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    paises.append(nuevo_pais)

    reescribir_csv(paises, 'paises.csv')

    print(f"✓ País '{nombre}' agregado exitosamente.")


def actualizar_pais(paises):
    """
    Actualiza los datos de población y superficie de un país existente.
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- ACTUALIZAR PAÍS ---")
    nombre_buscar = input("Nombre del país a actualizar: ").strip()
    
    # Buscar el país
    pais_encontrado = None
    for pais in paises:
        if pais['nombre'].lower() == nombre_buscar.lower():
            pais_encontrado = pais
            break
    
    if pais_encontrado is None:
        print(f"⚠ No se encontró el país '{nombre_buscar}'.")
        return
    
    print(f"\nPaís encontrado: {pais_encontrado['nombre']}")
    print(f"Población actual: {pais_encontrado['poblacion']:,}")
    print(f"Superficie actual: {pais_encontrado['superficie']:,} km²")
    
    # Actualizar población
    nueva_poblacion_str = input("\nNueva población (Enter para mantener): ").strip()
    if nueva_poblacion_str:
        valido, nueva_poblacion = validar_entero_positivo(nueva_poblacion_str, "La población")
        if valido:
            pais_encontrado['poblacion'] = nueva_poblacion
            print("✓ Población actualizada.")
    
    # Actualizar superficie
    nueva_superficie_str = input("Nueva superficie en km² (Enter para mantener): ").strip()
    if nueva_superficie_str:
        valido, nueva_superficie = validar_entero_positivo(nueva_superficie_str, "La superficie")
        if valido:
            pais_encontrado['superficie'] = nueva_superficie
            print("✓ Superficie actualizada.")

    reescribir_csv(paises, "paises.csv")
    
    print(f"\n✓ País '{pais_encontrado['nombre']}' actualizado correctamente.")


def buscar_pais(paises):
    """
    Busca países por nombre (coincidencia parcial o exacta).
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- BUSCAR PAÍS ---")
    termino = input("Ingrese el nombre (o parte del nombre): ").strip().lower()
    
    if not termino:
        print("⚠ Debe ingresar un término de búsqueda.")
        return
    
    # Buscar coincidencias
    resultados = []
    for pais in paises:
        if termino in pais['nombre'].lower():
            resultados.append(pais)
    
    if len(resultados) == 0:
        print(f"⚠ No se encontraron países con '{termino}'.")
        return
    
    print(f"\n✓ Se encontraron {len(resultados)} resultado(s):\n")
    mostrar_paises(resultados)

# ==================== FUNCIONES DE FILTRADO ====================

def filtrar_por_continente(paises):
    """
    Filtra países por continente.
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- FILTRAR POR CONTINENTE ---")
    continentes = [
        "África",
        "América del Norte",
        "América del Sur",
        "Antártida",
        "Asia",
        "Europa",
        "Oceanía"
    ]
    while True:
        print("Continentes disponibles:")
        for i, cont in enumerate(continentes, start=1):
            print(f"{i}. {cont}")

        opcion = input("Seleccione el número del continente: ").strip()
        if opcion.isdigit():
            cont_index = int(opcion) - 1
            if 0 <= cont_index < len(continentes):
                continente = continentes[cont_index]
                break
        print("⚠ Opción inválida. Por favor, intente nuevamente.")
    
    resultados = []
    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            resultados.append(pais)
    
    if len(resultados) == 0:
        print(f"⚠ No hay países en '{continente}'.")
        return
    
    print(f"\n✓ Países en {continente}:\n")
    mostrar_paises(resultados)


def filtrar_por_poblacion(paises):
    """
    Filtra países por rango de población.
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- FILTRAR POR POBLACIÓN ---")
    
    minimo_str = input("Población mínima: ").strip()
    maximo_str = input("Población máxima: ").strip()
    
    # Validar entrada
    if not minimo_str.isdigit() or not maximo_str.isdigit():
        print("⚠ Debe ingresar números válidos.")
        return
    
    minimo = int(minimo_str)
    maximo = int(maximo_str)
    
    if minimo > maximo:
        print("⚠ El mínimo no puede ser mayor al máximo.")
        return
    
    resultados = []
    for pais in paises:
        if minimo <= pais['poblacion'] <= maximo:
            resultados.append(pais)
    
    if len(resultados) == 0:
        print(f"⚠ No hay países con población entre {minimo:,} y {maximo:,}.")
        return
    
    print(f"\n✓ Países con población entre {minimo:,} y {maximo:,}:\n")
    mostrar_paises(resultados)


def filtrar_por_superficie(paises):
    """
    Filtra países por rango de superficie.
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- FILTRAR POR SUPERFICIE ---")
    
    minimo_str = input("Superficie mínima (km²): ").strip()
    maximo_str = input("Superficie máxima (km²): ").strip()
    
    # Validar entrada
    if not minimo_str.isdigit() or not maximo_str.isdigit():
        print("⚠ Debe ingresar números válidos.")
        return
    
    minimo = int(minimo_str)
    maximo = int(maximo_str)
    
    if minimo > maximo:
        print("⚠ El mínimo no puede ser mayor al máximo.")
        return
    
    resultados = []
    for pais in paises:
        if minimo <= pais['superficie'] <= maximo:
            resultados.append(pais)
    
    if len(resultados) == 0:
        print(f"⚠ No hay países con superficie entre {minimo:,} y {maximo:,} km².")
        return
    
    print(f"\n✓ Países con superficie entre {minimo:,} y {maximo:,} km²:\n")
    mostrar_paises(resultados)

def filtrar_paises(paises):
    """
    Filtra países según el criterio seleccionado.
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- FILTRAR PAÍSES ---")
    print("1. Por continente")
    print("2. Por población")
    print("3. Por superficie")
    
    opcion = input("\nSeleccione criterio: ").strip()
    
    if opcion == '1':
        filtrar_por_continente(paises)
    elif opcion == '2':
        filtrar_por_poblacion(paises)
    elif opcion == '3':
        filtrar_por_superficie(paises)
    else:
        print("⚠ Opción inválida.")

# ==================== FUNCIONES DE ORDENAMIENTO ====================

def ordenar_por_nombre(paises):
    """
    Ordena países por nombre usando bubble sort.
    
    Args:
        paises (list): Lista de países
    
    Returns:
        list: Lista ordenada
    """
    paises_copia = paises[:]
    n = len(paises_copia)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if paises_copia[j]['nombre'] > paises_copia[j + 1]['nombre']:
                paises_copia[j], paises_copia[j + 1] = paises_copia[j + 1], paises_copia[j]
    
    return paises_copia


def ordenar_por_poblacion(paises, descendente=False):
    """
    Ordena países por población.
    
    Args:
        paises (list): Lista de países
        descendente (bool): Si True, ordena de mayor a menor
    
    Returns:
        list: Lista ordenada
    """
    paises_copia = paises[:]
    n = len(paises_copia)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if descendente:
                condicion = paises_copia[j]['poblacion'] < paises_copia[j + 1]['poblacion']
            else:
                condicion = paises_copia[j]['poblacion'] > paises_copia[j + 1]['poblacion']
            
            if condicion:
                paises_copia[j], paises_copia[j + 1] = paises_copia[j + 1], paises_copia[j]
    
    return paises_copia


def ordenar_por_superficie(paises, descendente=False):
    """
    Ordena países por superficie.
    
    Args:
        paises (list): Lista de países
        descendente (bool): Si True, ordena de mayor a menor
    
    Returns:
        list: Lista ordenada
    """
    paises_copia = paises[:]
    n = len(paises_copia)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if descendente:
                condicion = paises_copia[j]['superficie'] < paises_copia[j + 1]['superficie']
            else:
                condicion = paises_copia[j]['superficie'] > paises_copia[j + 1]['superficie']
            
            if condicion:
                paises_copia[j], paises_copia[j + 1] = paises_copia[j + 1], paises_copia[j]
    
    return paises_copia


def ordenar_paises(paises):
    """
    Ordena países según el criterio seleccionado.
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- ORDENAR PAÍSES ---")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    
    opcion = input("\nSeleccione criterio: ").strip()
    
    if opcion == '1':
        paises_ordenados = ordenar_por_nombre(paises)
        print("\n✓ Países ordenados por nombre:\n")
        mostrar_paises(paises_ordenados)
        
    elif opcion == '2':
        orden = input("¿Ascendente (a) o Descendente (d)?: ").strip().lower()
        descendente = (orden == 'd')
        paises_ordenados = ordenar_por_poblacion(paises, descendente)
        tipo_orden = "descendente" if descendente else "ascendente"
        print(f"\n✓ Países ordenados por población ({tipo_orden}):\n")
        mostrar_paises(paises_ordenados)
        
    elif opcion == '3':
        orden = input("¿Ascendente (a) o Descendente (d)?: ").strip().lower()
        descendente = (orden == 'd')
        paises_ordenados = ordenar_por_superficie(paises, descendente)
        tipo_orden = "descendente" if descendente else "ascendente"
        print(f"\n✓ Países ordenados por superficie ({tipo_orden}):\n")
        mostrar_paises(paises_ordenados)
        
    else:
        print("⚠ Opción inválida.")


# ==================== FUNCIONES DE ESTADÍSTICAS ====================

def encontrar_maximo_poblacion(paises):
    """
    Encuentra el país con mayor población.
    
    Args:
        paises (list): Lista de países
    
    Returns:
        dict: País con mayor población
    """
    if len(paises) == 0:
        return None
    
    max_pais = paises[0]
    for pais in paises:
        if pais['poblacion'] > max_pais['poblacion']:
            max_pais = pais
    
    return max_pais


def encontrar_minimo_poblacion(paises):
    """
    Encuentra el país con menor población.
    
    Args:
        paises (list): Lista de países
    
    Returns:
        dict: País con menor población
    """
    if len(paises) == 0:
        return None
    
    min_pais = paises[0]
    for pais in paises:
        if pais['poblacion'] < min_pais['poblacion']:
            min_pais = pais
    
    return min_pais


def calcular_promedio_poblacion(paises):
    """
    Calcula el promedio de población de los países.
    
    Args:
        paises (list): Lista de países
    
    Returns:
        float: Promedio de población
    """
    if len(paises) == 0:
        return 0
    
    suma = 0
    for pais in paises:
        suma = suma + pais['poblacion']
    
    return suma / len(paises)


def calcular_promedio_superficie(paises):
    """
    Calcula el promedio de superficie de los países.
    
    Args:
        paises (list): Lista de países
    
    Returns:
        float: Promedio de superficie
    """
    if len(paises) == 0:
        return 0
    
    suma = 0
    for pais in paises:
        suma = suma + pais['superficie']
    
    return suma / len(paises)


def contar_por_continente(paises):
    """
    Cuenta la cantidad de países por continente.
    
    Args:
        paises (list): Lista de países
    
    Returns:
        dict: Diccionario con continentes y cantidades
    """
    continentes = {}
    
    for pais in paises:
        cont = pais['continente']
        if cont in continentes:
            continentes[cont] = continentes[cont] + 1
        else:
            continentes[cont] = 1
    
    return continentes


def mostrar_estadisticas(paises):
    """
    Calcula y muestra estadísticas sobre los países.
    
    Args:
        paises (list): Lista de países
    """
    if len(paises) == 0:
        print("⚠ No hay países en el sistema.")
        return
    
    print("\n" + "="*50)
    print("ESTADÍSTICAS GENERALES")
    print("="*50)
    
    # País con mayor y menor población
    pais_max_pob = encontrar_maximo_poblacion(paises)
    pais_min_pob = encontrar_minimo_poblacion(paises)
    
    print(f"\n📊 POBLACIÓN:")
    print(f"  • Mayor: {pais_max_pob['nombre']} ({pais_max_pob['poblacion']:,} habitantes)")
    print(f"  • Menor: {pais_min_pob['nombre']} ({pais_min_pob['poblacion']:,} habitantes)")
    
    # Promedio de población
    promedio_pob = calcular_promedio_poblacion(paises)
    print(f"  • Promedio: {promedio_pob:,.0f} habitantes")
    
    # Promedio de superficie
    promedio_sup = calcular_promedio_superficie(paises)
    print(f"\n🗺️  SUPERFICIE:")
    print(f"  • Promedio: {promedio_sup:,.0f} km²")
    
    # Cantidad de países por continente
    print(f"\n🌍 PAÍSES POR CONTINENTE:")
    continentes = contar_por_continente(paises)
    
    # Ordenar continentes alfabéticamente
    continentes_ordenados = sorted(continentes.items())
    
    for continente, cantidad in continentes_ordenados:
        print(f"  • {continente}: {cantidad} país(es)")
    
    print("\n" + "="*50)

# ==================== FUNCIONES DE VISUALIZACIÓN ====================

def mostrar_paises(paises):
    """
    Muestra la lista de países en formato tabular.
    
    Args:
        paises (list): Lista de países a mostrar
    """
    if len(paises) == 0:
        print("No hay países para mostrar.")
        return
    
    # Encabezado
    print(f"{'NOMBRE':<20} {'POBLACIÓN':<15} {'SUPERFICIE (km²)':<20} {'CONTINENTE':<15}")
    print("-" * 70)
    
    # Datos
    for pais in paises:
        print(f"{pais['nombre']:<20} {pais['poblacion']:<15,} {pais['superficie']:<20,} {pais['continente']:<15}")


def mostrar_menu():
    
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE PAÍSES")
    print("="*50)
    print("1.  Agregar país")
    print("2.  Actualizar país")
    print("3.  Buscar país")
    print("4.  Filtrar paises")
    print("5.  Ordenar países")
    print("6.  Mostrar estadísticas")
    print("7.  Listar todos los países")
    print("0.  Salir")
    print("="*50)


# ==================== FUNCIÓN PRINCIPAL ====================

def menu():
    """
    Función principal del programa.
    Gestiona el flujo del menú y las operaciones.
    """
    nombre_archivo = 'paises.csv'
    paises = cargar_paises_desde_csv(nombre_archivo)
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:
            case '1':
                agregar_pais(paises)
            case '2':
                actualizar_pais(paises)
            case '3':
                buscar_pais(paises)
            case '4':
                filtrar_paises(paises)        
            case '5':
                ordenar_paises(paises)
            case '6':
                mostrar_estadisticas(paises)
            case '7':
                print("\n--- TODOS LOS PAÍSES ---\n")
                mostrar_paises(paises)
            case '0':
                print("\n¡Hasta pronto!")
                break
            case _:
                print("⚠ Opción inválida. Intente nuevamente.")


# ==================== EJECUCIÓN DEL PROGRAMA ====================

menu()