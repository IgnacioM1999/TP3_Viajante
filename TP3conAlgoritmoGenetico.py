#TP3 El viajante con Algoritmo Genetico

import numpy

diccionarioObjetos = {'Cordoba' : [0, 677, 824, 698], 'Corrientes' : [646, 0, 677, 830], 'Formosa': [792, 677, 0, 968], 'La Plata': [698, 830, 968, 0]}
dic = {1: ['Cordoba', [0, 677, 824, 698]], 2:['Corrientes',[646, 0, 677, 830]], 3: ['Formosa', [792, 677, 0, 968]], 4: ['La Plata', [698, 830, 968, 0]]}


def crearPoblacionInicial(listaNumerosCromosoma): # crea la poblacion incial de 50 cromomosomas con los 23 genes
    poblacionIni = []
    for i in range(cromosomasPoblacion): # se crea 50 cromosomas
        cromosoma = numpy.random.permutation(listaNumerosCromosoma) #genera una permutacion aleatoria con la lista que se pasa como parametro
        poblacionIni.append(cromosoma)
    return poblacionIni

def funcionObjetivo():
    return

def funcionFitness(x, subLista) -> float: #El fitness del cromosoma se calcula como el cociente entre el valor de la función sobre la suma de todos los valores funcionales
    return x / sum(subLista)

def crossoverCiclico(cromo1, cromo2): #Se usa un crossover ciclico 
    return

def mutacion():
    return

cromosomasPoblacion = 50 # numero de cromosomas de las poblaciones
ciclos = 200 # Cantidad de ciclos
frecuenciaCrossover = 0
frecuenciaMutacion = 0
listaNumerosCromosoma = list(dic.keys())
numerosCromosomas = []
c = crearPoblacionInicial(listaNumerosCromosoma)
numerosCromosomas.extend(c)
print("poblacion inicial de cromosomas:")
for n in numerosCromosomas:
    print(n)


