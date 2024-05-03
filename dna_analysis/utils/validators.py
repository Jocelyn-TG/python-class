"""
validators.py: Módulo para realizar validaciones de secuencias de ADN y formatos de archivos en un paquete de análisis de ADN.

Este módulo proporciona funciones útiles para validar:
- La correctitud de las secuencias de ADN, asegurando que sólo contengan caracteres permitidos.
- El formato de archivos comúnmente usados en bioinformática, como el formato FASTA.
- La longitud de las secuencias de ADN para cumplir con los requisitos mínimos para análisis.

Funciones:
- validate_dna_sequence(sequence): Valida que la secuencia de ADN solo contenga caracteres válidos.
- validate_fasta_format(file_path): Verifica que un archivo tenga el formato FASTA correcto.
- check_sequence_length(sequence, min_length): Comprueba que la longitud de una secuencia de ADN cumpla con un mínimo especificado.

Los errores de validación levantan excepciones para permitir una gestión de errores adecuada en las funciones de llamada.
"""

def validate_dna_sequence(sequence):
    """
    Valida que la secuencia de ADN contenga solo caracteres válidos (A, C, G, T).

    Args:
        sequence (str): La secuencia de ADN a validar.

    Returns:
        bool: True si la secuencia es válida, False de lo contrario.

    Raises:
        ValueError: Si la secuencia contiene caracteres inválidos.
    """
    valid_chars = {'A', 'C', 'G', 'T'}
    if not set(sequence.upper()).issubset(valid_chars):
        raise ValueError("La secuencia de ADN contiene caracteres no válidos.")
    return True

def validate_fasta_format(file_path):
    """
    Verifica que el archivo tenga el formato correcto de FASTA.

    Args:
        file_path (str): Ruta al archivo FASTA.

    Returns:
        bool: True si el formato es correcto, False de lo contrario.

    Raises:
        IOError: Si el archivo no se puede leer.
        ValueError: Si el archivo no sigue el formato FASTA.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('>'):
                    if not line[1:].strip():
                        raise ValueError("Cabecera de FASTA vacía encontrada.")
                elif not set(line.strip().upper()).issubset({'A', 'C', 'G', 'T', 'N'}):
                    raise ValueError("Líneas de secuencia contienen caracteres no válidos.")
        return True
    except Exception as e:
        raise e

def check_sequence_length(sequence, min_length=100):
    """
    Comprueba que la longitud de una secuencia de ADN cumpla un mínimo requerido.

    Args:
        sequence (str): Secuencia de ADN.
        min_length (int): Longitud mínima requerida.

    Returns:
        bool: True si la secuencia cumple con la longitud mínima, False de lo contrario.

    Raises:
        ValueError: Si la longitud de la secuencia es menor que min_length.
    """
    if len(sequence) < min_length:
        raise ValueError(f"La secuencia debe tener al menos {min_length} bases.")
    return True


if __name__ == "__main__":
    seq = "ATGCATCAG"
    assert(validate_dna_sequence(seq)) == True

