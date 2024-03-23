'''
NAME: count_atgc
       

VERSION: 3.12
        

AUTHOR: JOCELYN TRUJILLO GUTIERREZ
        

DESCRIPTION: 
    
    Este es un proyecto que cuenta las ocurrencias de los símbolos "A", "T", 
    "G" y "C", de una secuencia de ADN que leerá a través de un archivo.
        
CATEGORY:

    Análisis de secuencias de ADN/Bioinformática
        
USAGE

    % python programName
    

ARGUMENTS

    archivo(str): Archivo que contiene la cadena para realizar el conteo.


METHOD

    El método utilizado en el código anterior es un enfoque simple para contar 
    los nucleótidos (A, C, G, T) en una secuencia de ADN contenida en un archivo 
    de texto. A continuación, describiré brevemente cada parte del método:
        1.- Obtención del nombre del archivo.
        2.- Apertura del archivo.
        3.- Lectura de la secuencia de ADN.
        4.- Conteo de nucleótidos.
        5.- Impresión de resultados.
     
'''

# ===========================================================================
# =                            main
# ===========================================================================


# Obtención del archivo
archivo = input("Por favor, introduce el nombre del archivo que contiene la secuencia de ADN: ")

# Abre el archivo
try:
    with open(archivo, "r") as arch:
        secuencia = arch.read().upper()        
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo}'.")

# Hace el conteo 
conteo = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for nucleotido in secuencia:
    conteo[nucleotido] += 1 

# Imprime los resultados
for nucleotido, total in conteo.items():
    print(f"{nucleotido}: {total}")

