# Clase de DNA
class Analisis_ADN:
    """
    Clase base para analizar una cadena de ADN.
    """
    def __init__(self, cadena):
        # Inicializa la clase con una cadena de ADN.
        self.cadena = cadena
    
    def contar(self):
        """
        Cuenta el número de caracteres en la cadena de ADN.
        """
        return len(self.cadena)
    
    def contar_codones(self):
        """
        Cuenta el número de codones en la cadena de ADN y lanza un error si la 
        cadena no se puede dividir en codones de 3 nucleótidos.
        """
        if self.contar()%3:
            raise ValueError(f"La cadena introducida tiene {self.contar()} caracteres, imposible dividirlo en codones")
        return int(self.contar() / 3)

    def __str__(self):
        """
        Descripción de la cadena de ADN.
        """
        return f"La cadena tiene {self.contar()} caracteres y {self.contar_codones()} codones."

class FreqGC(Analisis_ADN):
    """
    Clase para analizar la frecuencia de nucleótidos GC en una cadena de ADN.
    """
    def __init__(self, cadena):
        # Inicializa la clase con una cadena de ADN.
        super().__init__(cadena)
    
    def contar_gc(self):
        """
        Calcula el porcentaje de nucleótidos GC en la cadena de ADN.
        """
        return round(((self.cadena.count('G') + self.cadena.count('C')) / self.contar()) * 100, 1)
    
    def contar_codones(self):
        """
        Cuenta el número de codones en la cadena de ADN que contienen al menos una G o C.
        """
        if self.contar()%3:
            raise ValueError(f"La cadena introducida tiene {self.contar()} caracteres, imposible dividirlo en codones")
        codones_gc = [self.cadena[n:n+3] for n in range(0,self.contar(), 3) if "G" in self.cadena[n:n+3] or "C" in self.cadena[n:n+3]]
        return len(codones_gc)
    
    def __str__(self):
        """
        Descripción de la cadena de ADN.
        """
        return f"La cadena tiene {self.contar()} caracteres, el cual representa un {self.contar_gc()}% GC presentes en {self.contar_codones()} codones."

class FreqAT(Analisis_ADN):
    """
    Clase para analizar la frecuencia de nucleótidos AT en una cadena de ADN.
    """
    def __init__(self, cadena):
        # Inicializa la clase con una cadena de ADN.
        super().__init__(cadena)
    
    def contar_at(self):
        """
        Calcula el porcentaje de nucleótidos AT en la cadena de ADN.
        """
        return round(((self.cadena.count('A') + self.cadena.count('T')) / self.contar()) * 100, 1)
    
    def contar_codones(self):
        """
        Cuenta el número de codones en la cadena de ADN que contienen al menos una A o T.
        """
        if self.contar()%3:
            raise ValueError(f"La cadena introducida tiene {self.contar()} caracteres, imposible dividirlo en codones")
        codones_at = [self.cadena[n:n+3] for n in range(0,self.contar(), 3) if "A" in self.cadena[n:n+3] or "T" in self.cadena[n:n+3]]
        return len(codones_at)
    
    def __str__(self):
        """
        Descripción de la cadena de ADN.
        """
        return f"La cadena tiene {self.contar()} caracteres, el cual representa un {self.contar_at()}% AT presentes en {self.contar_codones()} codones."

if __name__ == "__main__":
    # Prueba de funcionalidad.
    test_sequence = "AAATTTGGGCCCAAATTTGGGCCCCCC"
    base = Analisis_ADN(test_sequence)
    cont_gc = FreqGC(test_sequence)
    cont_at = FreqAT(test_sequence)
    print(base)
    print(cont_gc)
    print(cont_at)