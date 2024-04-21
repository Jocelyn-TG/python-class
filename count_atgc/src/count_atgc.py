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
        2.- Comprobar si los argumentos son adecuados.
        3.- Apertura y lectura del archivo.
        4.- Conteo de nucleótidos.
        5.- Impresión de resultados.
     
'''

# ===========================================================================
# =                            imports
# ===========================================================================

import argparse

# ===========================================================================
# =                            Command Line Options
# ===========================================================================

parser = argparse.ArgumentParser(description="Lee archivo de entrada y (opcionalmente)los nucleotidos de los cuales imprimira el resultado")

# Agrega un argumento posicional para el archivo de entrada. 
parser.add_argument("input_file", type=str, 
			help="El archivo de texto que quieres procesar.")

# Agrega un argumento opcional los nucleotidos de los cuales quieras observar su total de apariciones.
parser.add_argument("-n", "--nucleotides", nargs="+", default=["A","C","G","T"],
			help="Total de apariciones de nucleotidos introducidos (default = A,C,G,T).")
args = parser.parse_args()

# ===========================================================================
# =                            functions
# ===========================================================================

def non_valid_char(data):
    """
    Lee una secuencia de caracteres y busca si hay caracteres que no son validos.
    En caso ser una secuencia completamente valida no regresa ningun valor.

    Args: 
        data(str): Secuencia de caracteres en mayusculas.

    Returns:
        char(str): 1er caracter invalido de la secuencia introducida.
    """
    for char in data:
        if char.upper() not in ("A","T","G","C"):
            return(char)


def find_seq(file):
    """
    Abre el archivo y regresa la secuencia de ADN a la cual se le van a contar 
    sus nucleotidos, en caso de que la secuencia no sea de ADN,que no se 
    encuentre el archivo o que este se encuentre vacio, se mostrara un error.

    Args:
        file(str): Cadena de texto que contiene el nombre del archivo.

    Returns:
        seq(str): Secuencia en mayusculas contenida en el archivo.

    FileNotFoundError:
        En caso de error se regresa el siguiente mensaje:
            "Error: No se encontró el archivo '{file}'."
    
    """
    try:
        with open(file, "r") as arch:
            seq = arch.read().strip().upper()
        if not seq:
            print("El archivo esta vacio.")  
            exit(1)
        invalid_char_seq = non_valid_char(seq)
        if invalid_char_seq:
            print(f"Error: Se encontro el caracter: {invalid_char_seq}, el cual no es valido.")
            exit(1)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{file}'.")
        exit(1)
    return seq

# ===========================================================================
# =                            main
# ===========================================================================

# Combrueba que se hayan introducido caracteres validos en el argumento nucleotides
if non_valid_char(args.nucleotides):
    print(f"Error: Se encontro un argumento el cual no valido.")
    exit(1)

# Abre el archivo y guarda su contenido en la variable secuencia.
seq = find_seq(args.input_file)

# Conteo de nucleotidos
count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for nucleotide in seq:
    count[nucleotide] += 1 

# Impresion de los resultados
for nucleotide in args.nucleotides:
    print(f"{nucleotide.upper()}: {count[nucleotide.upper()]}")