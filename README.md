# TPI de Programación - README

## Descripción

Aplicación en Python que permita gestionar información sobre países, aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas. El sistema es capaz de leer datos desde un archivo CSV, realizar consultas y generar indicadores clave a partir del dataset.

## Requisitos

- Python 3.8+

## Instalación

1. Clonar el repositorio:
   git clone [<repo-url>](https://github.com/Andriani25/TPI_PROGRAMACION.git)
2. Entrar al directorio del proyecto:
   cd TPI_PROGRAMACION

## Uso

Ejecutar el programa principal desde la línea de comandos:

- Python:
  python gestion_paises.py

## Ejemplos de entradas y salidas

--- AGREGAR NUEVO PAÍS ---
Entradas:

- Nombre del país: España
- Población: 235235
- Superficie (km²): 546475

Continentes disponibles:

1. África
2. América del Norte
3. América del Sur
4. Antártida
5. Asia
6. Europa
7. Oceanía

- Seleccione el número del continente: 6

Salida:

    ✓ Datos guardados correctamente.
    ✓ País 'España' agregado exitosamente.

--- ACTUALIZAR PAÍS ---

Entrada 1:

    - Nombre del país a actualizar: España

Salida 1:

    País encontrado: España
    Población actual: 235,235
    Superficie actual: 546,475 km²

Entrada 2:

    - Nueva población (Enter para mantener): 123456

Salida 2:

    ✓ Población actualizada.

Entrada 3:

    - Nueva superficie en km² (Enter para mantener): 321654

Salida 3:

    ✓ Superficie actualizada.
    ✓ Datos guardados correctamente.
    ✓ País 'España' actualizado correctamente.

--- BUSCAR PAÍS ---

Entrada:

    - Ingrese el nombre (o parte del nombre): Japon

Salida:

    ✓ Se encontraron 1 resultado(s):

    NOMBRE               POBLACIÓN       SUPERFICIE (km²)     CONTINENTE
    ----------------------------------------------------------------------
    Japon                43,578,888      2,234,345            Asia

--- FILTRAR PAÍSES ---

1. Por continente
2. Por población
3. Por superficie

Entrada:

    - Seleccione criterio: 1

--- FILTRAR POR CONTINENTE ---

Continentes disponibles:

1. África
2. América del Norte
3. América del Sur
4. Antártida
5. Asia
6. Europa
7. Oceanía

Entrada:

    - Seleccione el número del continente: 3

Salida:

    ✓ Países en América del Sur:

    NOMBRE               POBLACIÓN       SUPERFICIE (km²)     CONTINENTE
    ----------------------------------------------------------------------
    Argentina            45,376,763      2,780,400            América del Sur
    Brasil               213,993,437     8,515,767            América del Sur

--- FILTRAR POR POBLACIÓN ---

Entradas:

    - Población mínima: 300
    - Población máxima: 999999

Salida:

    ✓ Países con población entre 300 y 999,999:

    NOMBRE               POBLACIÓN       SUPERFICIE (km²)     CONTINENTE
    ----------------------------------------------------------------------
    Canada               9,098           91,874               América del Norte
    España               123,456         321,654              Europa

--- FILTRAR POR SUPERFICIE ---

Entradas:

    - Superficie mínima (km²): 200
    - Superficie máxima (km²): 9999999

Salida:

    ✓ Países con superficie entre 200 y 9,999,999 km²:

    NOMBRE               POBLACIÓN       SUPERFICIE (km²)     CONTINENTE
    ----------------------------------------------------------------------
    Argentina            45,376,763      2,780,400            América del Sur
    Japón                125,800,000     377,975              Asia
    Brasil               213,993,437     8,515,767            América del Sur
    Alemania             83,149,300      357,022              Europa
    Canada               9,098           91,874               América del Norte
    España               123,456         321,654              Europa

--- ORDENAR PAÍSES ---

1. Por nombre
2. Por población
3. Por superficie

--- POR NOMBRE ---

Entrada:

    - Seleccione criterio: 1

✓ Países ordenados por nombre:

## NOMBRE POBLACIÓN SUPERFICIE (km²) CONTINENTE

Alemania 83,149,300 357,022 Europa
Argentina 45,376,763 2,780,400 América del Sur
Brasil 213,993,437 8,515,767 América del Sur
Canada 9,098 91,874 América del Norte
España 123,456 321,654 Europa
Japón 125,800,000 377,975 Asia

--- POR POBLACION ---

Entradas:

    - Seleccione criterio: 2
    - ¿Ascendente (a) o Descendente (d)? d

Salida:

    ✓ Países ordenados por población (descendente):

    NOMBRE               POBLACIÓN       SUPERFICIE (km²)     CONTINENTE
    ----------------------------------------------------------------------
    Brasil               213,993,437     8,515,767            América del Sur
    Japón                125,800,000     377,975              Asia
    Alemania             83,149,300      357,022              Europa
    Argentina            45,376,763      2,780,400            América del Sur
    España               123,456         321,654              Europa
    Canada               9,098           91,874               América del Norte

--- POR SUPERFICIE ---

Entradas:

    - Seleccione criterio: 3
    - ¿Ascendente (a) o Descendente (d)? a

Salida:

    ✓ Países ordenados por superficie (ascendente):

    NOMBRE               POBLACIÓN       SUPERFICIE (km²)     CONTINENTE
    ----------------------------------------------------------------------
    Canada               9,098           91,874               América del Norte
    España               123,456         321,654              Europa
    Alemania             83,149,300      357,022              Europa
    Japón                125,800,000     377,975              Asia
    Argentina            45,376,763      2,780,400            América del Sur
    Brasil               213,993,437     8,515,767            América del Sur

--- MOSTRAR ESTADISTICAS ---

==================================================
SISTEMA DE GESTIÓN DE PAÍSES
==================================================

1.  Agregar país
2.  Actualizar país
3.  Buscar país
4.  Filtrar paises
5.  Ordenar países
6.  Mostrar estadísticas
7.  Listar todos los países
8.  # Salir

Entrada:

    - Seleccione una opción: 6

Salida:

    ==================================================
    ESTADÍSTICAS GENERALES
    ==================================================

    📊 POBLACIÓN:
    • Mayor: Brasil (213,993,437 habitantes)
    • Menor: Canada (9,098 habitantes)
    • Promedio: 78,075,342 habitantes

    🗺️  SUPERFICIE:
    • Promedio: 2,074,115 km²

    🌍 PAÍSES POR CONTINENTE:
    • América del Norte: 1 país(es)
    • América del Sur: 2 país(es)
    • Asia: 1 país(es)
    • Europa: 2 país(es)

    ==================================================

--- LISTAR PAISES ---

==================================================
SISTEMA DE GESTIÓN DE PAÍSES
==================================================

1.  Agregar país
2.  Actualizar país
3.  Buscar país
4.  Filtrar paises
5.  Ordenar países
6.  Mostrar estadísticas
7.  Listar todos los países
8.  # Salir

Entrada:

    - Seleccione una opción: 7

Salida:

    --- TODOS LOS PAÍSES ---

    NOMBRE               POBLACIÓN       SUPERFICIE (km²)     CONTINENTE
    ----------------------------------------------------------------------
    Argentina            45,376,763      2,780,400            América del Sur
    Japón                125,800,000     377,975              Asia
    Brasil               213,993,437     8,515,767            América del Sur
    Alemania             83,149,300      357,022              Europa
    Canada               9,098           91,874               América del Norte
    España               123,456         321,654              Europa

## Estructura del proyecto

- gestion_paises.py : código fuente
- paises.csv : archivo de salida
- README.md : este archivo

## Participación de los integrantes

- Luis Almeida

  - Diseño del algoritmo
  - Implementación de la lógica:
    - Filtrar paises
    - Ordenar paises
    - Mostrar estadísticas
    - Mostrar menú
  - Pruebas y corrección de errores
  - README

- Leandro Andriani

  - Diseño del algoritmo
  - Implementación de la lógica:
    - Agregar pais
    - Actualizar pais
    - Buscar pais
    - Manipulación y creación del archivo
    - Listar todos los países
    - Mostrar menú
  - Pruebas y corrección de errores

-- Fin --
