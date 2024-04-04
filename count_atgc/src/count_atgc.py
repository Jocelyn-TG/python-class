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

    % count_atgc.py [-h] input_file
    

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
# =                            imports
# ===========================================================================

import argparse

# ===========================================================================
# =                            main
# ===========================================================================


parser = argparse.ArgumentParser(description="Lee archivo de entrada")

# Agrega un argumento posicional para el archivo de entrada. 
parser.add_argument("input_file", type=str, 
			help="El archivo de texto que quieres procesar.")

args = parser.parse_args()

# Abre el archivo y guarda su contenido en la variable secuencia.
try:
    with open(args.input_file, "r") as arch:
        secuencia = arch.read().upper().strip()       
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{args.input_file}'.")
    exit(1)

# Hace el conteo 
conteo = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for nucleotido in secuencia:
    conteo[nucleotido] += 1 

# Imprime los resultados
for nucleotido, total in conteo.items():
    print(f"{nucleotido}: {total}")