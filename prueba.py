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


class Alumno(Persona):

    def __init__(self, nombre, apellidos, edad, asignatura):
        super().__init__(nombre, apellidos, edad)
        self.asignatura = asignatura

    def __str__(self):
        return super().__str__() + " Asignatura: "+self.asignatura


def agregar(numero,bbdd=[]):

    for i in range(numero):

        nombre = str(input("Introduce un nombre: "))
        apellidos = str(input("Introduce los apellidos: "))
        edad = int(input("Introduce la edad: "))
        asignatura = str(input("Introduce asignatura: "))

        bbdd.append(Alumno(nombre,apellidos,edad, asignatura))

    return bbdd

def mostrar(bbdd):
    for i in bbdd:
        print(i)

def mostrar_adultos(bbdd):
    for i in bbdd:
        if i.mayor_de_edad:
            print(i)

bbdd = [
        Alumno('Angela','Manero',23, 'PHP'),
        Alumno('Marina','Portilla',21, 'Java'),
        Alumno('Pepe','Fernandez',17, 'Python'),
        Persona('Juan','Gomez',15)
]

numero = int(input("Introduce el numero de alumnos que va a anadir: "))

bbdd = agregar(numero,bbdd)
mostrar(bbdd)
#mostrar_adultos(bbdd)