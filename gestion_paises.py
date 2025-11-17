"""
Sistema de Gestión de Datos de Países
Trabajo Práctico Integrador - Programación 1
"""

import os

# ==================== DATOS POR DEFECTO ====================

PAISES_DEFAULT = [
    'nombre,poblacion,superficie,continente',
    'Argentina,45376763,2780400,América',
    'Japón,125800000,377975,Asia',
    'Brasil,213993437,8515767,América',
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
    
    # Validar continente (no vacío)
    continente = ""
    while not continente:
        continente = input("Continente: ").strip()
        if not continente:
            print("⚠ El continente no puede estar vacío.")
    
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
        
        if opcion == '1':
            agregar_pais(paises)
        elif opcion == '2':
            actualizar_pais(paises)
        elif opcion == '0':
            print("\n¡Hasta pronto!")
            break
        else:
            print("⚠ Opción inválida. Intente nuevamente.")


# ==================== EJECUCIÓN DEL PROGRAMA ====================

menu()