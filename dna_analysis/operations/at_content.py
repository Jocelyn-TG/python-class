"""
at_content.py: Módulo para calcular el contenido de adenina y timina en secuencias de ADN.

Este módulo proporciona funciones para determinar el porcentaje de las bases de adenina (A)
y timina (T) en una secuencia de ADN dada. Esto es útil para estudios genéticos donde
las proporciones de AT pueden ser indicativas de ciertas características genómicas.

Funciones:
- calculate_at_content(sequence, normalize=True): Devuelve el porcentaje de AT en la secuencia.
"""

def calculate_at_content(sequence, normalize=True):
    """
    Calcula el contenido porcentual de adenina (A) y timina (T) en una secuencia de ADN.

    Args:
        sequence (str): La secuencia de ADN a analizar.
        normalize (bool): Si True, normaliza el contenido de AT en caso de que haya 'N's en la secuencia.

    Returns:
        float: El porcentaje de contenido de AT en la secuencia.

    Raises:
        ValueError: Si la secuencia está vacía o contiene caracteres no válidos.
    """

    # Validación básica de la secuencia
    if not sequence:
        raise ValueError("La secuencia proporcionada está vacía.")
    
    sequence = sequence.upper()
    if any(c not in 'ACGTN' for c in sequence):
        raise ValueError("La secuencia contiene caracteres no válidos.")

    a_count = sequence.count('A')
    t_count = sequence.count('T')
    at_count = a_count + t_count

    if normalize:
        total_count = sequence.count('A') + sequence.count('C') + sequence.count('G') + sequence.count('T')
        if total_count == 0:
            return 0
        return (at_count / total_count) * 100
    else:
        total_length = len(sequence)
        return (at_count / total_length) * 100

if __name__ == "__main__":
    # Prueba de funcionalidad.
    test_sequence = "ACTGNAT"
    print(f"Contenido de AT en la secuencia de prueba: {calculate_at_content(test_sequence, normalize=True)}%")