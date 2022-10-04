#TP3 El viajante con Algoritmo Genetico

import numpy

diccionarioObjetos = {'Cordoba' : [0, 677, 824, 698], 'Corrientes' : [646, 0, 677, 830], 'Formosa': [792, 677, 0, 968], 'La Plata': [698, 830, 968, 0]}
dic = {1: ['Cordoba', [0, 677, 824, 698]], 2:['Corrientes',[646, 0, 677, 830]], 3: ['Formosa', [792, 677, 0, 968]], 4: ['La Plata', [698, 830, 968, 0]]}


def crearPoblacionInicial(listaNumerosCromosoma): # crea la poblacion incial de 50 cromomosomas con los 23 genes
    poblacionIni = []
    for i in range(cromosomasPoblacion): # se crea 50 cromosomas
        cromosoma = numpy.random.permutation(listaNumerosCromosoma) #genera una permutacion aleatoria con la lista que se pasa como parametro
        poblacionIni.append(list(cromosoma)) #lo converto en una lista porque en la linea anterior, cromosoma es un objeto numpy.array no una lista
    return poblacionIni

def funcionObjetivo(cromosoma):

    return 

def funcionFitness(x, subLista) -> float: #El fitness del cromosoma se calcula como el cociente entre el valor de la función sobre la suma de todos los valores funcionales
    return x / sum(subLista)

def aplicarFunObj(subLista): #
    listaF = []
    for m in range(len(subLista)):
        f = funcionObjetivo(int(subLista[m])) #OBS: subLista[m] es un cromosoma en su valor decimal en la posicion m en formato entero
                                                # en reduntante pedir que se convierta un entero a entero
        listaF.append(f) #listaF va a ser una lista que contiene el valor de un cromosoma aplicando la Funcion Objetivo en formato FLOTANTE
    return listaF #retornamos la lista con todos los valores de la funcion objetivo del correspondiente cromosoma (segun su posicion) en formato FLOTANTE


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

def mutacion():
    return

def funcionPrincipal(listaPoblacionInicial):
    
    listaFunObj = []
    listaFitness = []
    listaPadres = []
    
    listaFunObj.extend(aplicarFunObj(listaPoblacionInicial))
    
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
    
    #Se empieza a ejecutar la funcion ejecutarProgramaPorIteracion segun el parametro nroIteracion
    for i in range(nroIteracion):
        nuevaGeneracion = funcionPrincipal()
        
    return

#PROGRAMA PRINCIPAL
cromosomasPoblacion = 50 # numero de cromosomas de las poblaciones
ciclos = 200 # Cantidad de ciclos
frecuenciaCrossover = 0
frecuenciaMutacion = 0
ejecutarProgramaPorIteracion(200)


