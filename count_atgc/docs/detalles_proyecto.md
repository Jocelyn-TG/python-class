#  Contador de Nucleótidos (A,T,G,C)

Fecha: 14/04/2024

**Participantes**:

- Jocelyn Trujillo jocelynt@lcg.unam.mx

## Descripción del Problema

Este es un proyecto que cuenta las ocurrencias de los nucleótidos "A", "T", "G" y "C", de una secuencia de ADN que leerá a través de un archivo, además de solo imprimir el resultado de los nucleótidos introducidos por el usuario. 

El problema enunciado implica leer un archivo de una sola línea, almacenando en un contador el total de cada una de las letras de la secuencia, también implica solo regresar como resultado el total de apariciones de los nucleótidos introducidos por el usuario (caso de que no se haya introducido ninguno imprimirá la cuenta total de A, T, G, C).

## Especificación de Requisitos

Requisitos funcionales

- Leer y analizar la secuencia de ADN dado un archivo, ya sea que la secuencia contenida este en mayúsculas o minúsculas (o ambas), además de capturar los nucleótidos de los cuales el usuario quiere imprimir el resultado.
- Calcular y desplegar el total de veces que aparece cada nucleótido en dicha secuencia (de los nucleótidos introducidos por el usuario) en el formato: 
		Nucleótido: total de apariciones.
- Detectar si el archivo esta vacío.
- Producir un mensaje de error si el archivo no existe.
- Producir un mensaje de error si la secuencia tenga un carácter diferente a "A", "T", "G" o "C":
- Producir un mensaje de error si el usuario introduce algún otro dato que no sea un carácter valido.


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
            (Opcional) Obtencion de los nucleotidos de los cuales se imprimira su total de apariciones.
	        (Opcional) Comprobar que el argumento de nucleotidos solo contenga caracteres validos.
        Abrir el archivo.
        Leer la secuencia de nucleotidos y comprobar:
	        No este vacio.
	        Que todos sus caracteres sean caracteres validos
        Contar cuantas veces se encuentra cada nucleotido en dicha secuencia.
        Mostrar los resultados (de los nucleotidos introducidos por el usuario o en caso de que no haya introducido nada se mostraran todos los nucleotidos).

Flujos alternativos(): 
	Input en argumento nucleotide no valido:
	    Imprimir el error.
    No encontrar el archivo:
		Imprimir el error.
	El archivo esta vario:
		Imprimir el error.
    Secuencia con caracteres no validos:
        Imprimir el error.
     
```

El formato de los datos de entrada será un archivo de una línea, el cual contenga la secuencia de nucleótidos, además de manera opcional el usuario puede introducir cuales son los  nucleótidos de los cuales quieras saber su tasa de aparición, separados por un espacio entre cada uno (ya sea estén escritos en mayúsculas, minúsculas o una combinación de ambos), si no se introduce ningún nucleótido se imprimirán los resultados de: A, T, G, C. El archivo puede contener la secuencia ya sea en mayúsculas o en minúsculas. La salida serán unas líneas de texto que muestran el total de veces que aparece cada nucleótido en dicha secuencia, en el formato:
	Nucleótido: total de apariciones.

#### Caso de uso: Contador de ATGC

```
        +---------------+
        |   Usuario     |
        +-------+-------+
                |
                | 1. Proporciona archivo de entrada (opcional = nucleotidos a contar).
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
- **Descripción**: El actor proporciona un archivo de entrada con la secuencia y los nucleótidos a contar.  El sistema valida el archivo y calcula el total de veces que aparece cada nucleótido en dicha secuencia, posteriormente muestra el resultado.

- **Flujo principal**:

	1. El actor inicia el sistema proporcionando el archivo de entrada con la secuencia y los nucleótidos a contar.
	2. El sistema valida la existencia del archivo y algunas otras condiciones.
	3. El sistema calcula el total de veces que aparece cada nucleótidos en dicha secuencia.
	4. El sistema muestra el resultado.
	
- **Flujos alternativos**:

	Si el argumento `nucleotides` no cuenta cuenta con los caracteres validos:
        1. El sistema muestra un mensaje diciendo que el dato introducido no valido.
        2. Se termina el programa.
        
	Si el archivo proporcionado no existe:
		1. El sistema muestra un mensaje de error diciendo que el archivo no se encuentra.
        2. Se termina el programa.
        
	Si el archivo proporcionado esta vacío:
		1. El sistema muestra un mensaje de error diciendo que el archivo esta vacío.
        2. Se termina el programa.
        
    Si la secuencia contiene otros caracteres no validos:
        1. El sistema muestra un mensaje diciendo que el dato de la secuencia no es un valido.
        2. Se termina el programa.
        

