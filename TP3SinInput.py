diccionarioObjetos = {'Cordoba' : [0, 677, 824, 698], 'Corrientes' : [646, 0, 677, 830], 'Formosa': [792, 677, 0, 968], 'La Plata': [698, 830, 968, 0]}


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


distanciasOtrasCiudades=[]
distanciasSinCero =[]
distanciaMinima=0
ciudades = list(diccionarioObjetos.keys());
ciudadesMostrar = list(diccionarioObjetos.keys())
indiceCiudadInicial = 0
distanciasOtrasCiudadesV2=[]
kmMasCorto = 0
kmTotal =0
listaKmRecorridos = []
listaRecorridosCiudades = [] # En esta lista se guardan las listas de todos los recorridos de las distintas ciudades iniciales
print(ciudadesMostrar)
recorridos=[] #esta lista a va a tener las ciudades que se van recorriendo en orden
indiceCiudadesRecorridas = []#estos indices los uso para ir eliminando las ciudades que ya fueron recorridas asi en el for no busca las distancias de las ciudades que ya pasamos

for ciudad in ciudades: #este for es para recorrer cada ciudad en la lista ciudadesy iniciar el recorrido en esa ciudad
    distanciasOtrasCiudadesFijas =  list(diccionarioObjetos.get(ciudad)) #esta lista se usa para, una vez obtenido el valor de la distanciaMinima, obtener el indice de ese valor y asi saber que ciudad es
    distanciasOtrasCiudadesV2 = list(diccionarioObjetos.get(ciudad)) #en esta lista se van a eliminar las ciudades que ya se han recorrido
    recorridos.append(ciudad)
    indiceCiudadesRecorridas.append(ciudades.index(ciudad))
    ciudadesMostrar.remove(ciudad)
    ciudadActual = ciudad

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
    
    
    recorridos.append(ciudad)
    recorridosV2 = []
    recorridosV2.extend(recorridos)
    indiceCiudadInicial=ciudades.index(ciudad)
    kmTotal += distanciaCortaCiudadInicial(ciudad, indiceCiudadInicial, ciudadActual)
    #print("el recorrido mas corto a todas las ciudades es:", recorridos,"con una cantidad de km recorridos de:", kmTotal)
    print("recorridos:", recorridos)
    print("listaRecorridosCiudades antes del append: ",listaRecorridosCiudades)
    listaRecorridosCiudades.append(recorridosV2)
    print("listaRecorridosCiudades: ", listaRecorridosCiudades)
    listaKmRecorridos.append(kmTotal)
    print("listaKmRecorridos: ", listaKmRecorridos)
    print()
    ciudadesMostrar = list(diccionarioObjetos.keys()) #se vuelve a llenar las ciudades a mostrar en pantalla
    indiceCiudadesRecorridas.clear() # limpio la lista para que guarde los indices de las ciudades del siguiente recorrido
    recorridos.clear() # limpio la lista de recorridos para el siguiente recorrido 
kmMinimo= min(listaKmRecorridos)
indiceRecorridoMinimo = listaKmRecorridos.index(kmMinimo)
recorridoMasCorto = listaRecorridosCiudades[indiceRecorridoMinimo]
print("el recorrido mas corto es:",recorridoMasCorto, "con un total km de:",kmMinimo)    

