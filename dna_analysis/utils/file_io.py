"""
file_io.py: Funciones para manejar operaciones de entrada/salida de archivos de ADN.

Este módulo provee funcionalidades para leer y escribir secuencias de ADN desde y hacia
archivos, asegurando que las secuencias sean válidas y estén bien formateadas.

Funciones:
    read_dna_sequence(filename) - Lee una secuencia de ADN de un archivo.
    write_dna_sequence(filename, sequence) - Escribe una secuencia de ADN en un archivo.
    
Ejemplos de uso están disponibles en el bloque principal del módulo.

Autores: [Tu Nombre]
Versión: 1.0
"""

# imports


# meta-info
__author__ = "Tu Nombre"
__version__ = "1.0"

# global vars


# functions internal

# main functions

def read_dna_sequence(filename):
    """
    Lee una secuencia de ADN de un archivo de texto.
    
    Args:
        filename (str): El nombre del archivo del cual leer la secuencia.
        
    Returns:
        str: La secuencia de ADN contenida en el archivo.
        
    Raises:
        FileNotFoundError: Si el archivo especificado no se encuentra.
        ValueError: Si el archivo está vacío o contiene caracteres no válidos.
    """
    with open(filename, 'r') as file:
        sequence = file.read().strip().upper()
    if not sequence:
        raise ValueError("El archivo está vacío.")
    if any(char not in 'ACGT' for char in sequence):
        raise ValueError("La secuencia contiene caracteres no válidos.")
    return sequence

def write_dna_sequence(filename, sequence):
    """
    Escribe una secuencia de ADN en un archivo de texto.
    
    Args:
        filename (str): El nombre del archivo donde se escribirá la secuencia.
        sequence (str): La secuencia de ADN a escribir.
        
    Raises:
        IOError: Si no se puede escribir en el archivo.
    """
    with open(filename, 'w') as file:
        file.write(sequence + '\n')


if __name__ == "__main__":
    # Bloques de prueba para demostrar la funcionalidad del módulo.
    
    # Suponiendo que el archivo "example_dna.txt" contiene la secuencia válida "ATCG"
    try:
        sequence = read_dna_sequence("example_dna.txt")
        print(f"Secuencia leída correctamente: {sequence}")
        
        # Ahora escribir esta secuencia a un nuevo archivo
        write_dna_sequence("output_dna.txt", sequence)
        print("Secuencia escrita correctamente en 'output_dna.txt'.")
    except Exception as e:
        print(f"Error: {str(e)}")