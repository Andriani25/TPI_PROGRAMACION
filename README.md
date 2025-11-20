# 🌍 Sistema de Gestión de Datos de Países

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Activo-success.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Trabajo Práctico Integrador - Programación 1**

### 🔹 `mostrar_menu()`

> **Descripción:** Muestra el menú principal del sistema.

#### 📥 Parámetros

- Ninguno

#### 📤 Retorna

- `None`

#### 🎯 Opciones del Menú

| Opción | Descripción |
|--------|-------------|
| **1** | 📝 Agregar país |
| **2** | 🔄 Actualizar país |
| **3** | 🔍 Buscar país |
| **4** | 🌍 Filtrar por continente |
| **5** | 👥 Filtrar por población |
| **6** | 📏 Filtrar por superficie |
| **7** | 🔢 Ordenar países |
| **8** | 📊 Mostrar estadísticas |
| **9** | 📋 Listar todos los países |
| **0** | 🚪 Salir |

#### 💡 Ejemplo de Salida

```
==================================================
SISTEMA DE GESTIÓN DE PAÍSES
==================================================
1.  Agregar país
2.  Actualizar país
3.  Buscar país
4.  Filtrar por continente
5.  Filtrar por población
6.  Filtrar por superficie
7.  Ordenar países
8.  Mostrar estadísticas
9.  Listar todos los países
0.  Salir
==================================================
```

---

### 🔹 `menu()`

> **Descripción:** Función principal del programa. Controla el flujo del sistema.

#### 📥 Parámetros

- Ninguno

#### 📤 Retorna

- `None`

#### ⚡ Efectos Secundarios

- 📂 Carga datos del archivo CSV
- ⌨️ Interactúa con el usuario mediante input
- 🔄 Llama a diferentes funciones según la opción elegida
- 💾 Mantiene los datos en memoria durante la ejecución

## 🎮 Ejemplos de Uso

### 📝 Caso 1: Agregar un País

```python
# El usuario ejecuta el programa
python gestion_paises.py

# Selecciona la opción 1
Seleccione una opción: 1

# Ingresa los datos
--- AGREGAR NUEVO PAÍS ---
Nombre del país: Uruguay
Población: 3473730
Superficie (km²): 176215
Continente: América
✓ Datos guardados correctamente.
✓ País 'Uruguay' agregado exitosamente.
```

---

### 🔍 Caso 2: Buscar Países

```python
# Búsqueda parcial
Seleccione una opción: 3

--- BUSCAR PAÍS ---
Ingrese el nombre (o parte del nombre): ale

✓ Se encontraron 1 resultado(s):

NOMBRE               POBLACIÓN       SUPERFICIE (km²)     CONTINENTE     
----------------------------------------------------------------------
Alemania             83,149,300      357,022              Europa         
```

---

### 🌍 Caso 3: Filtrar por Continente

```python
Seleccione una opción: 4

--- FILTRAR POR CONTINENTE ---
Continente: asia

✓ Países en asia:

NOMBRE               POBLACIÓN       SUPERFICIE (km²)     CONTINENTE     
----------------------------------------------------------------------
Japón                125,800,000     377,975              Asia           
```

---

### 🔢 Caso 4: Ordenar Países

```python
Seleccione una opción: 7

--- ORDENAR PAÍSES ---
1. Por nombre
2. Por población
3. Por superficie

Seleccione criterio: 3
¿Ascendente (a) o Descendente (d)? d

✓ Países ordenados por superficie (descendente):

NOMBRE               POBLACIÓN       SUPERFICIE (km²)     CONTINENTE     
----------------------------------------------------------------------
Brasil               213,993,437     8,515,767            América        
Argentina            45,376,763      2,780,400            América        
Japón                125,800,000     377,975              Asia           
Alemania             83,149,300      357,022              Europa         
```

---

### 📊 Caso 5: Ver Estadísticas

```python
Seleccione una opción: 8

==================================================
ESTADÍSTICAS GENERALES
==================================================

📊 POBLACIÓN:
  • Mayor: Brasil (213,993,437 habitantes)
  • Menor: Argentina (45,376,763 habitantes)
  • Promedio: 117,079,875 habitantes

🗺️  SUPERFICIE:
  • Promedio: 3,007,791 km²

🌍 PAÍSES POR CONTINENTE:
  • América: 2 país(es)
  • Asia: 1 país(es)
  • Europa: 1 país(es)

==================================================
```

---

### 🔄 Caso 6: Actualizar un País

```python
Seleccione una opción: 2

--- ACTUALIZAR PAÍS ---
Nombre del país a actualizar: japón

País encontrado: Japón
Población actual: 125,800,000
Superficie actual: 377,975 km²

Nueva población (Enter para mantener): 126000000
✓ Población actualizada.
Nueva superficie en km² (Enter para mantener): 
✓ Datos guardados correctamente.

✓ País 'Japón' actualizado correctamente.
```

---

### 👥 Caso 7: Filtrar por Rango de Población

```python
Seleccione una opción: 5

--- FILTRAR POR POBLACIÓN ---
Población mínima: 80000000
Población máxima: 150000000

✓ Países con población entre 80,000,000 y 150,000,000:

NOMBRE               POBLACIÓN       SUPERFICIE (km²)     CONTINENTE     
----------------------------------------------------------------------
Alemania             83,149,300      357,022              Europa         
Japón                125,800,000     377,975              Asia           
```

---

## 📄 Estructura del Archivo CSV

### Formato del Archivo

El archivo `paises.csv` utiliza el siguiente formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

### 📋 Especificaciones

| Característica | Descripción |
|----------------|-------------|
| **Codificación** | UTF-8 |
| **Separador** | Coma (`,`) |
| **Encabezado** | Primera línea |
| **Campos** | 4 columnas obligatorias |

### 🔤 Campos del CSV

| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| `nombre` | `string` | Nombre del país | Argentina |
| `poblacion` | `integer` | Población en habitantes | 45376763 |
| `superficie` | `integer` | Superficie en km² | 2780400 |
| `continente` | `string` | Continente | América |

### ✅ Validación de Datos

Al cargar el archivo, el sistema valida:

- ✔️ Que existan los 4 campos en cada línea
- ✔️ Que población y superficie sean números enteros
- ✔️ Que no haya campos vacíos
- ⚠️ Líneas con formato inválido son ignoradas con advertencia

### 📂 Ubicación del Archivo

```
proyecto/
│
├── gestion_paises.py
└── paises.csv          ← Creado automáticamente si no existe
```

---

## 🛠️ Manejo de Errores

### ❌ Errores Comunes y Soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| `⚠ Archivo 'paises.csv' no encontrado` | El archivo no existe | Se crea automáticamente con datos por defecto |
| `⚠ El archivo está vacío` | CSV sin contenido | Agregar encabezado y datos |
| `⚠ Fila con formato inválido` | Línea con datos incorrectos | Revisar que tenga 4 campos separados por comas |
| `⚠ Debe ingresar números válidos` | Entrada no numérica | Ingresar solo números enteros |
| `⚠ No se encontró el país` | País no existe en la lista | Verificar el nombre ingresado |
| `⚠ El nombre no puede estar vacío` | Campo obligatorio vacío | Ingresar un valor |

---

## 💡 Mejores Prácticas

### ✅ Recomendaciones de Uso

1. **📝 Backup Regular**
   - Hacer copias de seguridad de `paises.csv` periódicamente
   - Usar control de versiones para el archivo

2. **🔍 Validación de Datos**
   - Siempre verificar los datos antes de agregarlos
   - Revisar estadísticas después de actualizaciones masivas

3. **📊 Consultas Eficientes**
   - Usar filtros para grandes conjuntos de datos
   - Ordenar antes de analizar

4. **💾 Persistencia**
   - Los datos se guardan automáticamente después de agregar o actualizar
   - No cerrar el programa abruptamente durante operaciones

5. **🌍 Nombres de Continentes**
   - Mantener consistencia en los nombres (América, Europa, Asia, África, Oceanía)
   - Usar la misma capitalización

---

## 🔐 Limitaciones Conocidas

| Limitación | Descripción |
|------------|-------------|
| 📏 **Tamaño de archivo** | No optimizado para archivos muy grandes (>10,000 registros) |
| 🔄 **Algoritmo de ordenamiento** | Bubble Sort es O(n²), lento para grandes datasets |
| 🔒 **Concurrencia** | No soporta acceso simultáneo de múltiples usuarios |
| 📝 **Formato CSV** | No maneja comas dentro de los valores (requeriría comillas) |
| 🔍 **Búsqueda** | Búsqueda lineal O(n), sin índices |

---

### 📖 Documentación Relacionada

- [Python Official Documentation](https://docs.python.org/3/)
- [CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
- [Python Style Guide (PEP 8)](https://pep8.org/)

### 🎓 Conceptos Aplicados

| Concepto | Implementación |
|----------|----------------|
| **Estructuras de Datos** | Listas y Diccionarios |
| **Algoritmos de Ordenamiento** | Bubble Sort |
| **Manejo de Archivos** | Lectura/Escritura de CSV |
| **Validación de Datos** | Verificación de tipos y rangos |
| **Funciones** | Modularización del código |
| **Bucles** | `for`, `while` |
| **Condicionales** | `if`, `elif`, `else` |

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-4D4D4D?style=for-the-badge&logo=windows-terminal&logoColor=white)

## ✨ Características Principales

| Funcionalidad | Descripción |
|--------------|-------------|
| 📝 **CRUD Completo** | Agregar, actualizar, buscar y listar países |
| 🔍 **Búsqueda Avanzada** | Búsqueda parcial por nombre (case-insensitive) |
| 🔢 **Filtros Múltiples** | Por continente, población y superficie |
| 📊 **Ordenamiento** | Por nombre, población o superficie (asc/desc) |
| 📈 **Estadísticas** | Máximos, mínimos, promedios y distribución |
| 💾 **Persistencia** | Datos almacenados en CSV con codificación UTF-8 |
| ✅ **Validaciones** | Validación robusta de entrada de datos |
| 🎨 **Interfaz Amigable** | Menús claros con emojis y formato tabular |

---

## 🔧 Requisitos

### Módulos Requeridos

```python
import os  # Operaciones con sistema de archivos
```

### Versión de Python

- Python 3.x o superior

### Sistema Operativo

- ✅ Windows
- ✅ Linux
- ✅ macOS

---

---

### 👨‍💻 Autores

**Leandro Andriani**

**Luis Almeida**

---

## 🙏 Agradecimientos

- 🎓 Universidad Tecnológica Nacional - Por el apoyo académico
- 👨‍🏫 Profesores Cinthia Rigoni y Martín García - Por las clases, consultas y conocimiento brindado
- 📚 Comunidad Python - Por la documentación y recursos

### ⭐ Si te gustó este proyecto, no olvides darle una estrella

---

**Hecho con ❤️ por Leandro Andriani y Luis Almeida**

*Trabajo Práctico Integrador - Programación 1 - 2024*

---
