"""
calculate_at_content.py: Script para calcular el contenido de adenina y timina (AT) en una secuencia de ADN.

Este script lee una secuencia de ADN desde un archivo dado y calcula el porcentaje de adenina (A)
y timina (T) en esa secuencia. La secuencia de ADN debe estar en un archivo de texto y solo
contener los caracteres 'A', 'C', 'G', 'T', o 'N' (este último representa cualquier nucleótido). 
Opcionalmente, el cálculo puede normalizar el contenido excluyendo los caracteres 'N'.

Uso:
    python calculate_at_content.py <path_to_dna_file> [--normalize]

Argumentos:
    <path_to_dna_file> : Ruta al archivo de texto que contiene la secuencia de ADN.
    --normalize        : Opción para normalizar el contenido de AT excluyendo 'N's del c
"""

import argparse

from dna_analysis.operations.at_content import calculate_at_content
from dna_analysis.utils.file_io import read_dna_sequence

def main():
    
    parser = argparse.ArgumentParser(description="Calcula el contenido de AT en una secuencia de ADN.")
    parser.add_argument("file", type=str, help="Archivo de ADN del cual leer la secuencia.")
    parser.add_argument("-n", "--normalize", action="store_true", help="Normaliza el contenido de AT excluyendo 'N's del cálculo.")

    args = parser.parse_args()
    file_path = args.file
    normalize = args.normalize

    try:
        # Leer la secuencia del archivo especificado utilizando la función proporcionada por file_io.py
        sequence = read_dna_sequence(file_path)
        
        # Calcular el contenido de AT de la secuencia utilizando la función proporcionada por at_content.py
        at_content = calculate_at_content(sequence, normalize=normalize)
        
        # Mostrar el resultado al usuario
        print(f"El contenido de AT en la secuencia es: {at_content:.2f}%")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()