'''
NAME: Codons
       

VERSION: 1
        

AUTHOR: JOCELYN TRUJILLO GUTIERREZ
        

DESCRIPTION: 
    
    Separa los codones de una secuencia de ADN dado un archivo fasta
    utilizando los distintos marcos de lectura y almacenando el resultado
    en un archivo.
        
CATEGORY:

    Análisis de secuencias de ADN/Bioinformática
        
USAGE

    % count_codons.py [-h] input_file
    
ARGUMENTS

    input_file(str): Archivo fasta que contiene las secuencias para separar
                     los codones.

METHOD

   A continuación, describiré brevemente cada parte del método:
        1.- Obtención del nombre del archivo desde linea de comando.
        2.- Separar Id de la secuencia.
        3.- Separar los codones de la secuencia de acuerdo al marco de lectura.
        4.- Almacenar el resultado en un archivo.
        5.- Regresar archivo al usuario.
     
'''


# ===========================================================================
# =                            imports
# ===========================================================================

import argparse
from Bio import SeqIO

# ===========================================================================
# =                            Command Line Options
# ===========================================================================

parser = argparse.ArgumentParser(description="Para ingresar archivo de entrada")

# Agrega un argumento posicional para el archivo de entrada. 
parser.add_argument("input_file", type=str, 
			help="El archivo de texto que quieres procesar.")

args = parser.parse_args()

# ===========================================================================
# =                            functions
# ===========================================================================

def find_codons(frame, sequence, output_filename):
    """
    Separa una secuencia de ADN en sus codones y almacena el resultado en un
    archivo.

    Args: 
        frame(int): Marco de lectura.
        sequence(str): Secuencia de ADN.

    Returns:
        output_filename(file): Regresa un archivo con el nombre introducido que
                               contiene los codones separados por espacios.
    """

    codons = []
    
    # Para frames positivos
    if frame < 4:
        start = frame - 1
        seq = sequence[start:]
        
    # Para frames negativos
    else:
        start = frame - 4
        seq = sequence.reverse_complement()[start:]
    
    # Extraccion de codones
    for n in range(0, len(seq), 3):
        codons.append(str(seq[n:n+3]))
    
    # Escribir el archivo de salida
    with open(output_filename, 'w') as f:
        f.write(f">Frame {frame}\n")
        f.write(' '.join(codons) + '\n')

# ===========================================================================
# =                            main
# ===========================================================================

# Frames 1, 2, 3 (positivo) and 4, 5, 6 (negativo)
frames = [1, 2, 3, 4, 5, 6]

# Lee el archivo y separa el identificador de la secuencia.
for seq_record in SeqIO.parse(args.input_file, "fasta"):
    sequence = seq_record.seq
    id = seq_record.id
    for frame in frames:
        output_filename = f"{id}_Frame{frame}.fasta"
        find_codons(frame, sequence, output_filename)
    
    
    
