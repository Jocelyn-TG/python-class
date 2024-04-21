# Casos de prueba 

Este documento describe los casos de prueba para el script de Python desarrollado para contar las ocurrencias de los nucleótidos "A", "T", "G" y "C" en un archivo, imprimiendo como resultado solo los nucleótidos introducidos por el usuario (en caso de que no se haya introducido ninguno imprimirá la cuenta total de "A", "T", "G" y "C"). El objetivo de estas pruebas es validar y garantizar que el script funciona correctamente y cumple con las especificaciones.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script está diseñado para validar el archivo y calcular el total de veces que aparece cada nucleótido en dicha secuencia, posteriormente muestra el resultado (incluyendo solo los nucleótidos mencionados por el usuario o  "A", "T", "G" y "C") . El script también está diseñado para manejar errores como si el archivo no existe o si los datos introducidos como nucleótidos son los adecuados.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.
    
    
### Caso de prueba 1: Comprobación de la cuenta adecuada de ATGC.

- Descripción: Verificar que el script puede contar de manera adecuada las ocurrencias de ATGC en una secuencia dada sin importar si se encuentra en mayúsculas o en minúsculas.
		Archivo con la siguiente secuencia:
			"CAGTCATCGATCAGCTACGATCATCAGCTACGTCATCT".
- Resultado esperado: 
		A: 10 
		C: 12
		G: 6
		T: 10

### Caso de prueba 2: Comprobación del funcionamiento con secuencia de mayúsculas/minúsculas y del requerimiento de nucleótidos específicos.

- Descripción: Verificar que el script puede imprimir solo el resultado de los nucleótidos introducidos por el usuario, sin importar si la secuencia o los datos introducidos por el usuario están completamente escritos en minúsculas o las contienen.
- Datos de entrada: 
		Archivo con la siguiente secuencia:
			"AAAAaaaaTTTTttttGGGGggggCCCCcccc".
		En linea de comandos introducir [-n A t] después del nombre del archivo.
- Resultado esperado: 
		A: 8
		T: 8


### Caso de prueba 3: Comprobación de error para cuando el archivo introducido no existe
- Descripción: Verificar que el script maneja correctamente los archivos no existentes.
- Datos de entrada: Ruta a un archivo que no existe.
- Resultado esperado: 
		1.- Muestra el mensaje: Error: No se encontró el archivo '{nombre_del_archivo}'.
		2.- Termina el programa.

### Caso de prueba 4: Comprobación de error para cuando el archivo introducido esta vacío
- Descripción: Verificar que el script maneja correctamente los archivos vacíos.
- Datos de entrada: Archivo sin contenido.
- Resultado esperado: 
		1.-  Muestra el mensaje: "El archivo esta vacío."
		2.- Termina el programa.

### Caso de prueba 5: Comprobación de error para cuando el archivo introducido contiene una secuencia con caracteres no validos
- Descripción: Verificar que el script maneja correctamente los archivos cuya secuencia contiene caracteres no validos.
- Datos de entrada: 
		Archivo con la siguiente secuencia:
			"AUUGGCCAAAUUGGCCAAAUUGGCCAA".
- Resultado esperado: 
		1.- Muestra el mensaje: "Error: Se encontró el carácter: {caracter_introducido}, el cual no es valido."
		2.- Termina el programa.
### Caso de prueba 6: Comprobación de error para caracteres no validos introducidos por el usuario para obtener su ocurrencia
- Descripción: Verificar que el script maneja correctamente  el input de caracteres no validos al ejecutar el programa.
- Datos de entrada: 
		Archivo con la siguiente secuencia:
			"CAGTCATCGATCAGCTACGATCATCAGCTACGTCATCT".
		En linea de comandos introducir [-n u A] después del nombre del archivo.
- Resultado esperado: 
		1.- Muestra el mensaje: ""Error: Se encontró un argumento el cual no valido."
		2.- Termina el programa.