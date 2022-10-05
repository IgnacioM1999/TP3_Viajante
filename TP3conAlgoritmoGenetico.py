#TP3 El viajante con Algoritmo Genetico

import numpy
import random
import folium

# diccionarioObjetos = {'Cordoba' : [0, 677, 824, 698], 'Corrientes' : [646, 0, 677, 830], 'Formosa': [792, 677, 0, 968], 'La Plata': [698, 830, 968, 0]}
dic = {1: ['Ciudad de Buenos Aires' , [0, 646, 792, 933, 53, 986, 985, 989, 375, 834, 1127, 794, 2082, 979, 1080, 1334, 1282, 1005, 749, 393, 579, 939, 2373, 799] , [ -34.6082787, -58.3708681]],
       2: ['Cordoba' , [646, 0, 677, 824, 698, 340, 466, 907, 348, 919, 1321, 669, 2281, 362, 517, 809, 745, 412, 293, 330, 577, 401, 2618, 1047] , [-31.4135, -64.18105]],
       3: ['Corrientes' , [792, 677, 0, 157, 830, 814, 1131, 1534, 500, 291, 1845, 13, 2819, 691, 633, 742, 719, 1039, 969, 498, 1136, 535, 3131, 1527] , [ -27.461195,-58.836841]],
       4: ['Formosa' , [933, 824, 157, 0, 968, 927, 1269, 1690, 656, 263, 1999, 161, 2974, 793, 703, 750, 741, 1169, 1117, 654, 1293, 629, 3284, 1681], [-26.18489, -58.17313]] ,
       5: ['La Plata' , [53, 698, 830, 968, 0, 1038, 1029, 1005, 427, 857, 1116, 833, 2064, 1030, 1132, 1385, 1333, 1053, 795, 444, 602, 991, 2350, 789] , [-34.92145, -57.95453]],
       6: ['La Rioja' , [986, 340, 814, 927, 1038, 0, 427, 1063, 659, 1098, 1548, 802, 2473, 149, 330, 600, 533, 283, 435, 640, 834, 311, 2821, 1311] , [-29.414280, -66.855750]],
       7: ['Mendoza' , [985, 466, 1131, 1269, 1029, 427, 0, 676, 790, 1384, 1201, 1121, 2081, 569, 756, 1023, 957, 152, 235, 775, 586, 713, 2435, 1019] , [-32.882293, -68.859762]],
       8: ['Neuquen' , [989, 907, 1534, 1690, 1005, 1063, 676, 0, 1053, 1709, 543, 1529, 1410, 1182, 1370, 1658, 1591, 824, 643, 1049, 422, 1286, 1762, 479], [-38.952136, -68.059230]] ,
       9: ['Parana' , [375, 348, 500, 656, 427, 659, 790, 1053, 0, 658, 1345, 498, 2320, 622, 707, 959, 906, 757, 574, 19, 642, 566, 2635, 1030] , [-31.745060, -60.518284]],
       10: ['Posadas' , [834, 919, 291, 263, 857, 1098, 1384, 1709, 658, 0, 1951, 305, 2914, 980, 924, 1007, 992, 1306, 1200, 664, 1293, 827, 3207, 1624] , [-27.388928, -55.918591]],
       11: ['Rawson' , [1127, 1321, 1845, 1999, 1116, 1548, 1201, 543, 1345, 1951, 0, 1843, 975, 1647, 1827, 2120, 2054, 1340, 1113, 1349, 745, 1721, 1300, 327] , [-43.299332, -65.102075]],
       12: ['Resistencia' , [794, 669, 13, 161, 833, 802, 1121, 1529, 498, 305, 1843, 0, 2818, 678, 620, 729, 706, 1029, 961, 495, 1132, 523, 3130, 1526] , [-27.451791, -58.987015]],
       13: ['Rio Gallegos' , [2082, 2281, 2819, 2974, 2064, 2473, 2081, 1410, 2320, 2914, 975, 2818, 0, 2587, 2773, 3063, 2997, 2231, 2046, 2325, 1712, 2677, 359, 1294], [-51.625838, -69.221658]] ,
       14: ['S.F.d.V.d. Catamarca' , [979, 362, 691, 793, 1030, 149, 569, 1182, 622, 980, 1647, 678, 2587, 0, 189, 477, 410, 430, 540, 602, 915, 166, 2931, 1391] , [-28.468759, -65.779600]],
       15: ['S.M. de Tucuman' , [1080, 517, 633, 703, 1132, 330, 756, 1370, 707, 924, 1827, 620, 2773, 189, 0, 293, 228, 612, 727, 689, 1088, 141, 3116, 1562] , [-26.822205, -65.211730]],
       16: ['S.S. de Jujuy' , [1334, 809, 742, 750, 1385, 600, 1023, 1658, 959, 1007, 2120, 729, 3063, 477, 293, 0, 67, 874, 1017, 942, 1382, 414, 3408, 1855] , [-24.186368, -65.299711]],
       17: ['Salta' , [1282, 745, 719, 741, 1333, 533, 957, 1591, 906, 992, 2054, 706, 2997, 410, 228, 67, 0, 808, 950, 889, 1316, 353, 3341, 1790], [-24.812486, -65.410616]] ,
       18: ['San Juan' , [1005, 412, 1039, 1169, 1053, 283, 152, 824, 757, 1306, 1340, 1029, 2231, 430, 612, 874, 808, 0, 284, 740, 686, 583, 2585, 1141] , [-31.537198, -68.525925]],
       19: ['San Luis' , [749, 293, 969, 1117, 795, 435, 235, 643, 574, 1200, 1113, 961, 2046, 540, 727, 1017, 950, 284, 0, 560, 412, 643, 2392, 882] , [-33.292094, -66.314007]],
       20: ['Santa Fe' , [393, 330, 498, 654, 444, 640, 775, 1049, 19, 664, 1349, 495, 2325, 602, 689, 942, 889, 740, 560, 0, 641, 547, 2641, 1035] , [-31.621989, -60.696438]],
       21: ['Santa Rosa' , [579, 577, 1136, 1293, 602, 834, 586, 422, 642, 1293, 745, 1132, 1712, 915, 1088, 1382, 1316, 686, 412, 641, 0, 977, 2044, 477], [-36.620794, -64.281901]] ,
       22: ['Santiago del Estero' , [939, 401, 535, 629, 991, 311, 713, 1286, 566, 827, 1721, 523, 2677, 166, 141, 414, 353, 583, 643, 547, 977, 0, 3016, 1446], [-27.799076, -64.258781]] ,
       23: ['Ushuaia' , [2373, 2618, 3131, 3284, 2350, 2821, 2435, 1762, 2635, 3207, 1300, 3130, 359, 2931, 3116, 3408, 3341, 2585, 2392, 2641, 2044, 3016, 0, 1605], [-54.816960, -68.330233]] ,
       24: ['Viedma' , [799, 1047, 1527, 1681, 789, 1311, 1019, 479, 1030, 1624, 327, 1526, 1294, 1391, 1562, 1855, 1790, 1141, 882, 1035, 477, 1446, 1605, 0], [-40.820035, -63.001845]] }


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
    probabilidad = random.randint(0, 1)
    if probabilidad <= frecuenciaCrossover:
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
    else:
        hijo1 = padre1
        hijo2 = padre2
    return hijo1, hijo2

def mutacion(cromosoma):
    probabilidad = random.randint(0,1)
    if probabilidad <= frecuenciaMutacion:
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
frecuenciaCrossover = 0.75
frecuenciaMutacion = 0.25
ejecutarProgramaPorIteracion(2)


