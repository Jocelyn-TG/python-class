class Animal():
    # Atributos de la clase
    Multicelular = True
    Heterotrofo = True

    def __init__(self, nombre, edad):
        # Atributos de la instancia
        self.nombre = nombre     # Nombre (str)
        self.edad = edad     # En años(en años)

    def haz_ruido(self):
        return "AAAAAAAAAAAAH"

class Perro(Animal):  # Sub_clase perro
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)  # Constructor

    def haz_ruido(self):
        return "guau guau"  # Sobrescribiendo el método haz_ruido

class Gato(Animal): # Sub_clase perro
  # Atributos de la clase
  Usa_Arenero = True

  # Atributos de la clase
  def __init__(self, nombre, edad):
      super().__init__(nombre, edad)

  def haz_ruido(self):
      return "miau"  # Sobrescribiendo el método haz_ruido
  
if __name__ == "__main__":
    # Prueba de funcionalidad.
    Julian = Perro("Julian", 3)
    print(f"Los datos del perro = {Julian.__dict__}")
    print(f"Julian hace = {Julian.haz_ruido()}")
    Jose = Gato("Jose", 3)
    print(f"Los datos del perro = {Jose.__dict__}")
    print(f"Jose hace = {Jose.haz_ruido()}")
    caballo = Animal("Juan", 3)
    print(f"Los datos del animal (caballo) = {caballo.__dict__}")
    print(f"El caballo {caballo.nombre} hace = {caballo.haz_ruido()}")

#======================================================================================#
#==                                        Nota:                                      =#
#======================================================================================#

# Antes de juzgar la humildad de mi codigo, checar:
#    --> https://github.com/Jocelyn-TG/python-class/blob/main/Curso_biopython/Class_Analisis_DNA.py
# Que yo pense que la tarea era hacer una clase de lo que quisieramos jsjsjsjsj

# fin de la nota.