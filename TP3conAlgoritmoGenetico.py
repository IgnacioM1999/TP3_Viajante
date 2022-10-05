#TP3 El viajante con Algoritmo Genetico

import numpy
import random

# diccionarioObjetos = {'Cordoba' : [0, 677, 824, 698], 'Corrientes' : [646, 0, 677, 830], 'Formosa': [792, 677, 0, 968], 'La Plata': [698, 830, 968, 0]}
dic = {1: ['Cordoba', [0, 677, 824, 698]], 2:['Corrientes',[646, 0, 677, 830]], 3: ['Formosa', [792, 677, 0, 968]], 4: ['La Plata', [698, 830, 968, 0]]}


def crearPoblacionInicial(listaNumerosCromosoma): # crea la poblacion incial de 50 cromomosomas con los 23 genes
    poblacionIni = []
    for i in range(cromosomasPoblacion): # se crea 50 cromosomas
        cromosoma = numpy.random.permutation(listaNumerosCromosoma) #genera una permutacion aleatoria con la lista que se pasa como parametro
        poblacionIni.append(list(cromosoma)) #lo converto en una lista porque en la linea anterior, cromosoma es un objeto numpy.array no una lista
    return poblacionIni

def funcionObjetivo(cromosoma):
    acum = 0
    indice = 0
    print(cromosoma)
    for i in cromosoma:
        if(indice < len(cromosoma)-1):
            ciudad = []
            distancias = []
            ciudad = dic.get(i)
            distancias.extend(ciudad[1])
            print(ciudad)
            #print("su distancias son:", distancias)
            indice += 1
            numeroProximaCiudad = cromosoma[indice]
            #print("La siguiente ciudad es:", numeroProximaCiudad)
            dist = distancias[numeroProximaCiudad-1]
            #print("distacia hacia la siguiente ciudad:",dist)
            acum += dist
    print("el total recorrido es:", acum)
    return acum

def funcionFitness(x, subLista) -> float: #El fitness del cromosoma se calcula como el cociente entre el valor de la función sobre la suma de todos los valores funcionales
    return x / sum(subLista)

def aplicarFunObj(subLista): #
    listaF = []
    for m in subLista:
        f = funcionObjetivo(m) #OBS: subLista[m] es un cromosoma en su valor decimal en la posicion m en formato entero
                                                # en reduntante pedir que se convierta un entero a entero
        listaF.append(f) #listaF va a ser una lista que contiene el valor de un cromosoma aplicando la Funcion Objetivo en formato FLOTANTE
    return listaF #retornamos la lista con todos los valores de la funcion objetivo del correspondiente cromosoma (segun su posicion) en formato FLOTANTE

def aplicarFitness(subLista): #Aca sublista es listaFunObj que es la lista que contiene los valores en formato entero de la funcion objetivo de cada cromosoma 
    listaFit = []
    for m in subLista:
        f = funcionFitness(m, subLista) #m contiene el valor entero en la posicion de subLista
        listaFit.append(f) #listaFit es una lista con los valores de la fitness de cada cromosoma en forma flotante(ya que lo que retorna a funcion fitness es el valor en flotante)
    return listaFit  # retorna una lista de los valores de la funcion Fitness aplicadas a los cromosomas en formato flotante

def seleccionTorneo(listaPoblacion, listaFitness):
    
    largo=[]
    listaGanadores=[]
    listaParticipantes=[]
    listaIndicesParticipantes=[]
    listaFitnessParticipantes=[]
    k = 50 # porque la poblacion tiene que tener 50 cromosomas
    
    for q in range(k): # k es la cantidad de veces que se repite la seleccion por torneo
        largo.clear()
        listaParticipantes.clear()
        listaIndicesParticipantes.clear()
        listaFitnessParticipantes.clear()
    
        for t in range(len(listaPoblacion)): #aca genero la lista de los indices de listaPoblacionInicialCadena para trabajar mas tarde con el Fitness
            largo.append(t)
            print(largo) #largo tiene todos los indices de listaPoblacionInicialCadena
            print()
        for e in range(5):# 5 es la cantidad de individuos para seleccion torneo (el grupo de participantes)
            indiceParti= random.choice(largo) #elijo a los participantes que van a estar en el torneo
            print("indice del participante seleccionado que hace referencia a la posicion en listaPoblacionIncialCadena es: ",indiceParti)
            print()
            listaIndicesParticipantes.append(indiceParti)
            print("lista de indices de los participantes seleccionados en listaPoblacionInicialCadena: ",listaIndicesParticipantes)
            print()
            parti = listaPoblacion[indiceParti] #parti tiene el cromosoma en STRING que fue seleccionado para ser participante
            listaParticipantes.append(parti) #agrego los participantes que van a ir al torneo a esta lista
            print("participantes en la listaParticipantes: ", listaParticipantes)
            print()
            #ya esta conformado la lista con los 5 participantes, ahora tengo que seleccionar el que tiene el mayor fitness
        for o in listaIndicesParticipantes:
            print("lista indices participantes: ",listaIndicesParticipantes)
            print("valor de o: ", o)
            print()
            listaFitnessParticipantes.append(listaFitness[o])
            print("lista fitness de cada participante: ", listaFitnessParticipantes)
            print()
        minfit = min(listaFitnessParticipantes)
        print("fitness maximo de la lista fitness participante: ", minfit)
        indiceGanador = listaFitnessParticipantes.index(minfit)
        print("el indice del ganador es: ", indiceGanador)
        print()
            
        listaGanadores.append(listaParticipantes[indiceGanador])
        print("lista ganadores en la iteracion",q+1," es ",listaGanadores)    
    return listaGanadores #listaGanadores es una lista con los cromosomas padres en formato STRING 

def crossoverCiclico(padre1, padre2): #Se usa un crossover ciclico 
    cont = 0
    hijo1 = []
    hijo2 = []
    hijo1.append(padre1[0])
    hijo2.append(padre2[0])
    genBuscado = padre2[0]
    cont+=1
    while(cont <= len(padre1)-1):
        if(padre1[cont] == genBuscado):
            hijo1.append(padre1[cont])
            hijo2.append(padre2[cont])
            genBuscado = padre2[cont]
        else:
            hijo1.append(padre2[cont])
            hijo2.append(padre1[cont])
        cont+=1  
    return hijo1, hijo2

def mutacion(cromosoma):
    a = random.randrange(1, 4)
    print("a: ", a)
    b = a
    print("b: ", b)
    while a == b:
        b = random.randrange(1, 4)
    print("nuevo b: ", b)
    aux = cromosoma.copy()
    print("aux: ", aux)
    cromosoma[b]=cromosoma[a]
    cromosoma[a]= aux[b]
    return cromosoma

def funcionPrincipal(listaPoblacionInicial):
    
    listaFunObj = []
    listaFitness = []
    listaPadres = []
    
    listaFunObj.extend(aplicarFunObj(listaPoblacionInicial))
    listaFitness.extend(aplicarFitness(listaFunObj))
    return

def ejecutarProgramaPorIteracion(nroIteracion):

    listaNumerosCromosoma = list(dic.keys()) #lista de los numeros de las ciudades obtenido del diccionario
    poblacionInicial = []
    listaMinimosFit = []
    listaMaximosFit = []
    listaPromFit = []
    listaMinimosObj = []
    listaMaximosObj = []
    listaPromObj = []
    
    #Se crea la poblacion inicial de 50 cromosomas. Cada cromosoma es una permutacion de 1 a 23, que simboliza las ciudades 
    c = crearPoblacionInicial(listaNumerosCromosoma)
    poblacionInicial.extend(c) #esta lista esta en formato ENTERO
    print("poblacion inicial de cromosomas:")
    for n in poblacionInicial:
        print(n)# muestra cada cromosoma en la poblacion inicial
    print()
    #Se empieza a ejecutar la funcion ejecutarProgramaPorIteracion segun el parametro nroIteracion
    for i in range(nroIteracion):
        nuevaGeneracion = funcionPrincipal(poblacionInicial)
        
    return

#PROGRAMA PRINCIPAL
cromosomasPoblacion = 5 # numero de cromosomas de las poblaciones
ciclos = 200 # Cantidad de ciclos
frecuenciaCrossover = 0
frecuenciaMutacion = 0
ejecutarProgramaPorIteracion(2)


