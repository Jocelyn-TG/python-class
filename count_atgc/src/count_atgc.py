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

    % count_atgc.py [-h] [-n NUCLEOTIDES [NUCLEOTIDES ...]] input_file
    
ARGUMENTS

    input_file(str): Archivo que contiene la cadena para realizar el conteo.
    nucleotides(str): Opcional. Nucleotidos de los cuales quieras adquirir el conteo.

METHOD

    El método utilizado en el código anterior es un enfoque simple para contar 
    los nucleótidos (A, C, G, T) en una secuencia de ADN contenida en un archivo 
    de texto. A continuación, describiré brevemente cada parte del método:
        1.- Obtención del nombre del archivo desde linea de comando.
            1.1.- (Opcional) Obtencion de los nucleotidos de los cuales se 
                  imprimira su total de apariciones.
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

# Agrega un argumento opcional los nucleotidos de los cuales quieras observar su total de apariciones.
parser.add_argument("-n", "--nucleotides", nargs="+", default=["A","C","G","T"],
			help="Total de apariciones de nucleotidos introducidos (default = A,C,G,T).")
args = parser.parse_args()

# Abre el archivo y guarda su contenido en la variable secuencia.
try:
    with open(args.input_file, "r") as arch:
        secuencia = arch.read().upper().strip()
    if not secuencia:
        print("El archivo esta vacio.")
        exit(1)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{args.input_file}'.")
    exit(1)

# Hace el conteo 
conteo = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for nucleotido in secuencia:
    if nucleotido not in conteo:
        print(f"Tu secuencia contiene el caracter: {nucleotido}, el cual no es valido.")
        exit(1)
    else:
        conteo[nucleotido] += 1 

# Imprime los resultados
for nucleotido in args.nucleotides:
    if nucleotido.upper() not in conteo:
        print(f"{nucleotido} no es un caracter valido.")
    else:
        print(f"{nucleotido.upper()}: {conteo[nucleotido.upper()]}")