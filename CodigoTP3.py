# TP Viajante

import itertools
import numpy

diccionarioObjetos = {'Cordoba' : [0, 677, 824, 698], 'Corrientes' : [646, 0, 677, 830], 'Formosa': [792, 677, 0, 968], 'La Plata': [698, 830, 968, 0]}

 
#inp_list = ['Cordoba', 'Corrientes']
#permutations = list(itertools.permutations(inp_list))
#for i in range(len(permutations)):
#    print(permutations[i])


#PERSONA DEBE INGRESAR DONDE QUIERE INICIAR Y TAMBIEN SE DEBE CALCULAR PARA CADA CIUDAD CUAL ES EL VIAJE MAS CORTO
#RECORDAR VOLVER A LA CIUDAD DE INICIO
print("Se inicia el viaje desde Cordoba")
ciudades = list(diccionarioObjetos.keys());
ciudadInicio = input("Ingrese la ciudad que quiera iniciar el viaje: ")
distanciasOtrasCiudades=[]
distanciasSinCero =[]
distanciaMinima=0
for i in range(len(ciudades)):
    print(ciudades[i])
    if (ciudadInicio == ciudades[i]):
        print("se encontro ciudad")
        distanciasOtrasCiudades=list(diccionarioObjetos.get(ciudades[i]))
        break
    else:
        print("no es")
distanciaMinima = min(distanciasOtrasCiudades)
if (distanciaMinima == 0):
    distanciasSinCero = distanciasOtrasCiudades
    distanciasSinCero.remove(0)
    distanciaMinima = min(distanciasSinCero)
indice = distanciasOtrasCiudades.index(distanciaMinima)

print("La distancia mas corta hacia la otra ciudad es: ", distanciaMinima)
        

#si es por heuristica, cuando estoy en una ciudad, hay que ver las distancias con esa ciudad y ver la mas chica.
# no se hace falta armar todas las soluciones porque sino se esta haciendo la exaustiva 
