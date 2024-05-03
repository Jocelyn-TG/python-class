"""
codon_content.py: Módulo para calcular el contenido de codones en secuencias de ADN.

Este módulo proporciona funciones para para primera mente determinar la cantidad de codones 
de una secuencia de ADN dada y ademas calcular la tasa de aparcion de esos codones en dicha secuencia.
La secuencia dada no puede contener caracteres distintos a: "A", "T", "G", "C".

Funciones:
- codon_content(sequence): Devuelve el total de apariciones del codon en una secuencia dada.
"""

def codon_content(sequence):
    """
    Calcula el contenido total de codones en una secuencia de ADN.

    Args:
        sequence (str): La secuencia de ADN a analizar.

    Returns:
        codons (dic): El % total de apariciones de dicho codon en la secuencia.

    Raises:
        ValueError: Si la secuencia está vacía, contiene caracteres no válidos o no es divisible entre 3.
    """

    # Validación básica de la secuencia
    if not sequence:
        raise ValueError("La secuencia proporcionada está vacía.")
    
    sequence = sequence.upper()
    if any(c not in 'ACGT' for c in sequence):
        raise ValueError("La secuencia contiene caracteres no válidos.")
    
    if len(sequence) % 3:
        raise ValueError("La secuencia no se puede separar por codones exactos (no es divisible entre 3).")

    # Conteo de codones
    total_codons = len(sequence) / 3
    codons= {}

    for n in range(0,len(sequence), 3):
        if sequence[n:n+3] not in codons:
            codons[sequence[n:n+3]] = 1
        else:
            codons[sequence[n:n+3]] += 1
    
    codon_freq = {codon : f"{round((instances / total_codons) * 100, 2)} %" for codon, instances in codons.items()}

    return codon_freq

if __name__ == "__main__":
    # Prueba de funcionalidad.
    test_sequence = "AAATTTGGGCCCAAATTTGGGCCCCCC"
    print(f"Frecuencia de aparicion de cada codon en la secuencia de prueba: {codon_content(test_sequence)}")