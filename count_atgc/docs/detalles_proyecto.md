# Nombre del Proyecto

Fecha: 21/03/2024

**Participantes**:

- Jocelyn Trujillo jocelynt@lcg.unam.mx

## Descripción del Problema

Este es un proyecto que cuenta las ocurrencias de los nucleotidos "A", "T", "G" y "C", de una secuencia de ADN que leerá a través de un archivo.

El problema enunciado implica leer un archivo de una sola  línea, almacenando en un contador el total de cada una de las letras de la secuencia.

## Especificación de Requisitos

Requisitos funcionales

- Leer y analizar la secuencia de ADN dado un archivo, ya sea que este en mayúsculas o minúsculas.
- Calcular el total de veces que aparece cada nucleótido en dicha secuencia.
- Desplegar el total calculado en el formato: 
		A: total de apariciones... 
		T: total de apariciones... 
		G: total de apariciones... 
		C: total de apariciones... 
- Producir un mensaje de error si el archivo no existe.

Requisitos no funcionales

-  El script deberá estar escrito en Python.
-  El tiempo de respuesta debe ser rápido, incluso con archivos de gran tamaño.
-  La entrada del archivo debe ser flexible (i.e. se acepta a través de la línea de comandos).


## Análisis y Diseño

Para resolver este problema, se utilizarán varias funciones incorporadas en Python, así como el manejo de excepciones para la validación de datos y archivo. A continuación, se muestra un pseudocódigo simple para ilustrar la lógica básica del script:

```
Función principal():
    Intentar:
        Obtener el nombre del archivo a travez del usuario.
        Abrir el archivo.
        Leer la secuencia de nucleotidos.
        Contar cuantas veces se encuentra cada nucleotido en dicha secuencia.
        Mostrar los resultados al usuario.
    No encontrar el archivo:
		Imprimir el error
```

El formato de los datos de entrada será simplemente un archivo de una línea, el cual contenga la secuencia de nucleótidos. Dicho archivo puede contener la secuencia ya sea en mayúsculas o en minúsculas. La salida será una línea de texto que muestra  el total de veces que aparece cada nucleótido en dicha secuencia, en el formato:
	A: total de apariciones... 
	T: total de apariciones... 
	G: total de apariciones... 
	C: total de apariciones... 

#### Caso de uso: Contador de ATGC

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 v
         +-------+-------+
         |               |
         |  Contador de  |
	     |  nucleotidos  |
	     |  en  Archivo  |
         |   (Sistema)   |
         |               |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**: El actor proporciona un archivo de entrada con la secuencia a contar.  El sistema valida el archivo y calcula el total de veces que aparece cada nucleótidos en dicha secuencia, posteriormente muestra el resultado.

- **Flujo principal**:

	1. El actor inicia el sistema proporcionando el archivo de entrada con la secuencia a contar.
	2. El sistema valida la existencia del archivo.
	3. El sistema calcula el total de veces que aparece cada nucleótidos en dicha secuencia.
	4. El sistema muestra el resultado.
	
- **Flujos alternativos**:
	Si el archivo proporcionado no existe
		1. El sistema muestra un mensaje de error diciendo que el archivo no se encuentra.
                

