# Contador de Nucleótidos (A,T,G,C)

Este es un script de Python diseñado para contar las ocurrencias de los nucleótidos "A", "T", "G" y "C", de una secuencia de ADN que leerá a través de un archivo.

## Uso

El script acepta un argumento posicional y varios opcionales, siendo el posicional, el nombre del archivo y los opcionales serian los nucleótidos de los cuales quieras conocer su total de apariciones:

```
python count_atgc.py [archivo] -n [nucleotido]
```

donde `archivo` es el nombre del archivo que contiene la secuencia de ADN. El archivo debe toda la secuencia en una sola línea.
y donde `nucleotido` es la lista de nucleótidos (ya sea en minúscula, mayúscula o ambos) de los cuales se va a mostrar su total de incidencias, estos deben estar separados uno o mas espacios entre ellos.

## Salida

El script imprimirá las ocurrencias de los nucleótidos en la consola. 

## Control de errores

Si el archivo proporcionado no existe, el script generará un mensaje de error. Del mismo modo, si ingresas como argumento alguna cosa que no sea un desoxirribonucleótido, el script imprimirá una leyenda con un error.

## Datos

El script está diseñado para operar en archivos de texto plano, con una única secuencia. No hay restricciones en la longitud (mientras sea de una sola línea).

## Metadatos y documentación

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script, consulte [https://github.com/Jocelyn-TG/python-class/tree/main/count_atgc/docs].

## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia [Apache License]. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [Trujillo, J. (2024) Codigo count_atgc. Version 1.0. GitHub: https://github.com/Jocelyn-TG/python-class/tree/main/count_atgc].

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: [jocelynt@lcg.unam.mx].
