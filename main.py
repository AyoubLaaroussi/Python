import sys

from modelos.alumno import Alumno
from modelos.persona import Persona


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
comprobacion = True
try:
    numero = int(input("Introduce el numero de alumnos que va a anadir: "))
except Exception:
    while comprobacion:
        numero = int(input("Introduce el numero de alumnos que va a anadir: "))
        if numero >=0:
            comprobacion=False
        comprobacion=True

bbdd = agregar(numero,bbdd)
mostrar(bbdd)
#mostrar_adultos(bbdd)