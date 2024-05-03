"""
count_codons.py: Script para calcula frecuencia de codones dada una secuencia(solo en el 1er marco de lectura).

Este script lee una secuencia de ADN desde un archivo dado, la separa en codones e imprime la frecuencia en porcentaje
(redondeada a 2 decimales) de cada uno de ellos.

Uso:
    python calculate_at_content.py <path_to_dna_file> 

Argumentos:
    <path_to_dna_file> : Ruta al archivo de texto que contiene la secuencia de ADN.
"""

import argparse

from dna_analysis.operations.codon_content import codon_content
from dna_analysis.utils.file_io import read_dna_sequence

def main():
    
    parser = argparse.ArgumentParser(description="Calcula el contenido de AT en una secuencia de ADN.")
    parser.add_argument("file", type=str, help="Archivo de ADN del cual leer la secuencia.")

    args = parser.parse_args()
    file_path = args.file

    # Leer la secuencia del archivo especificado utilizando la función proporcionada por file_io.py
    sequence = read_dna_sequence(file_path)

    # Calcula la frecuencia de aparicion de cada codon un la secuencia proporcionada e imprime el resultado.
    print(f"Frecuencia de aparicion de cada codon en la secuencia de prueba: {codon_content(sequence)}")

if __name__ == "__main__":
    main()