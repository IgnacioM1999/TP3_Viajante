# TP Viajante

import itertools
import numpy

diccionarioObjetos = {'Cordoba' : [0, 677, 824, 698], 
                   'Corrientes' : [646, 0, 677, 830], 
                       'Formosa': [792, 677, 0, 968], 
                      'La Plata': [698, 830, 968, 0]}

 
#inp_list = ['Cordoba', 'Corrientes']
#permutations = list(itertools.permutations(inp_list))
#for i in range(len(permutations)):
#    print(permutations[i])


#PERSONA DEBE INGRESAR DONDE QUIERE INICIAR Y TAMBIEN SE DEBE CALCULAR PARA CADA CIUDAD CUAL ES EL VIAJE MAS CORTO
#RECORDAR VOLVER A LA CIUDAD DE INICIO

distanciasOtrasCiudades=[]
distanciasSinCero =[]
distanciaMinima=0

def buscarCiudad(ciudadesMostrar, ciudadActual):
    ciudadEncontrada = False
    for i in range(len(ciudadesMostrar)):
        if (ciudadActual == ciudadesMostrar[i]):
            ciudadEncontrada = True
    return ciudadEncontrada

def busquedaHeuristica(ciudades, ciudadActual,distanciaOtrasCiudadesFijas, distanciasOtrasCiudadesV2):
    distanciasSinCero=[]
    c=""
    indice= 0
    kmTotal = 0
    distanciaMinima = min(distanciasOtrasCiudadesV2)
    if (distanciaMinima == 0):
        distanciasSinCero.extend(distanciasOtrasCiudadesV2) 
        distanciasSinCero.remove(0)
        print("Se encontro un 0 => distancias de las otras ciudades sin el cero:",distanciasSinCero)
        distanciaMinima = min(distanciasSinCero)
    kmTotal = distanciaMinima
    print("distancia minima: ",distanciaMinima)
    #print("distaciasOtrasCiudades:", distanciasOtrasCiudades)
    indice = distanciasOtrasCiudadesFijas.index(distanciaMinima) #este indice es el indice de la ciudad en la lista distanciaOtrasCiudades que tiene la distancia mas corta con ciudadActual
    print("el indice en distanciaOtrasCiudadesFijas de la distancia minima:",indice)
    c = ciudades[indice]
    print("La distancia mas corta hacia la otra ciudad es: ", distanciaMinima, "correspondiente a:", c)
    return c, indice, kmTotal

def distanciaCortaCiudadInicial(ciudadInicial, indiceCiudadInicial, ciudadActual):
    distancias = []
    print("la ultima ciudad que se recorrio es:", ciudadActual)
    distancias = diccionarioObjetos.get(ciudadActual)
    distanciaACiudadInicial = distancias[indiceCiudadInicial]
    print("La distancia hacia la ciudad inicial ", ciudadInicial," es:", distanciaACiudadInicial)
    return distanciaACiudadInicial 
    

#FUNCION PRINCIPAL
ciudades = list(diccionarioObjetos.keys());
ciudadesMostrar = list(diccionarioObjetos.keys())
ciudadAnterior = ""
indiceCiudadInicial = 0
distanciasOtrasCiudadesV2=[]
kmMasCorto = 0
kmTotal =0
print(ciudades)
recorridos=[] #esta lista a va a tener las ciudades que se van recorriendo en orden
indiceCiudadesRecorridas = []#estos indices los uso para ir eliminando las ciudades que ya fueron recorridas asi en el for no busca las distancias de las ciudades que ya pasamos
ciudadInicial = input("Ingrese la ciudad que quiera iniciar el viaje: ")
ciudadActual = ciudadInicial


#Se valida que la ciudad que ingresa el usuario se encuentre en la lista de ciudades
bandera = buscarCiudad(ciudadesMostrar, ciudadActual)
while (bandera == False):
    print("Ciudad no encontrada")
    ciudadInicial = input("Ingrese la ciudad que quiera iniciar el viaje: ")
    ciudadActual = ciudadInicial 
    bandera = buscarCiudad(ciudades, ciudadActual)

distanciasOtrasCiudadesFijas =  list(diccionarioObjetos.get(ciudadActual)) #esta lista se usa para, una vez obtenido el valor de la distanciaMinima, obtener el indice de ese valor y asi saber que ciudad es
distanciasOtrasCiudadesV2 = list(diccionarioObjetos.get(ciudadActual)) #en esta lista se van a eliminar las ciudades que ya se han recorrido
recorridos.append(ciudadActual)
indiceCiudadesRecorridas.append(ciudades.index(ciudadActual))
ciudadesMostrar.remove(ciudadActual)

#Se empieza a hacer el registro del recorrido que se hace 
for v in range(len(ciudades)-1):
    print("iteracion:",v)
    print()
    print("ciudad actual:", ciudadActual)
    print("ciudades a viajar:",ciudadesMostrar) 
    print("distancias otras ciudades:",distanciasOtrasCiudadesFijas)
    # ciudadAnterior = ciudadActual
    #indiceCiudadAnterior = ciudades.index(ciudadAnterior)
    ciu, indi, kmMasCorto = busquedaHeuristica(ciudades, ciudadActual, distanciasOtrasCiudadesFijas, distanciasOtrasCiudadesV2)
    kmTotal += kmMasCorto
    print("la ciudad devuelta es:",ciu)
    print("El indice devuelto es:",indi)
    recorridos.append(ciu)
    indiceCiudadesRecorridas.append(indi)
    ciudadActual=ciu
    ciudadesMostrar.remove(ciudadActual)
    distanciasOtrasCiudadesFijas.clear()
    distanciasOtrasCiudadesFijas.extend(list(diccionarioObjetos.get(ciudadActual)))
    distanciasOtrasCiudadesV2.clear()
    distanciasOtrasCiudadesV2.extend(list(diccionarioObjetos.get(ciudadActual)))
    print("distanciasOtrasCiudadesV2 antes de hacer el pop(remover elemento):",distanciasOtrasCiudadesV2)
    print("indice ciudades recorridas:",indiceCiudadesRecorridas)
    for r in indiceCiudadesRecorridas:
        distancia = distanciasOtrasCiudadesFijas[r]
        distanciasOtrasCiudadesV2.remove(distancia)
        print("distancias otras ciudadesV2:",distanciasOtrasCiudadesV2)
    print("distanciasOtrasCiudadesV2 despues del pop:", distanciasOtrasCiudadesV2)
    print()
recorridos.append(ciudadInicial)
indiceCiudadInicial=ciudades.index(ciudadInicial)
kmTotal += distanciaCortaCiudadInicial(ciudadInicial, indiceCiudadInicial, ciudadActual)
print("el recorrido mas corto a todas las ciudades es:", recorridos,"con una cantidad de km recorridos de:", kmTotal)


        
#si es por heuristica, cuando estoy en una ciudad, hay que ver las distancias con esa ciudad y ver la mas chica.
# no se hace falta armar todas las soluciones porque sino se esta haciendo la exaustiva 

#SUMAR LOS KILOMETROS DE LA ULTIMA CIUDAD A LA CIUDAD INICIAL Y PONER COMO ULTIMA CIUDAD LA CIUDAD INICIAL

