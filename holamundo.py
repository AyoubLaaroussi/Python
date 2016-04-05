

print "***************"

lista = [
			{'Nombre':'Ayoub','idiomas':5},
        	{'Nombre':'Santos','idiomas':2}
        ]

print "************Listado Normal****************"



buscar = "%(Nombre)s sabe %(idiomas)i idiomas."

for persona in lista:
    print buscar % persona


print "************Listado Con metodo****************"



def consulta(nombre,idiomas):

	cambio = "%(nombre)s sabe %(idiomas)i idiomas."

	listas = [
				{"nombre":nombre,"idiomas":int(idiomas)}
			]
	for personas in listas:
		print cambio % personas

		 
consulta("Santos",5)


print "***************MODIFICACION****************"

print "Modificamos el nombre y numero de idiomas."

def cambiar(nombre,idiomas):

    buscar = "%(Nombre)s sabe %(idiomas)i idiomas."
    name = str(raw_input("nombre a buscar."))
    for persona in lista:
    	if persona['Nombre'] == name:
        	persona['Nombre']=nombre
        	persona['idiomas']=idiomas
    	print buscar % persona

cambiar("Jaime",4)