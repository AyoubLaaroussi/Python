class Persona():

    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def __str__(self):
        return self.nombre+" "+self.apellidos+", "+str(self.edad)

    @property
    def mayor_de_edad(self):
        return self.edad >= 18