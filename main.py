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
while True:
    numero = input("Introduce el numero de alumnos que va a anadir: ")
    try:
        numero = int(numero)
        if numero >= 0:
            bbdd = agregar(numero,bbdd)
            mostrar(bbdd)
            sys.exit()
    except Exception:
        print("Cuidado! tiene que introducir un numero entero.")
        


#mostrar_adultos(bbdd)