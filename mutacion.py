"""import random

cromosoma = [1,2,3,4]

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
print("cromosoma antes de la mutacion: ", cromosoma)
cromosomaMutado = mutacion(cromosoma)

print("cromosoma mutado: ", cromosomaMutado)"""

import random

frecuenciaCrossover=0.75

def crossoverCiclico(padre1, padre2):  # Se usa un crossover ciclico
    probabilidad = random.uniform(0, 1)
    print("probabilidadCrossover: ",probabilidad)
    if probabilidad <= frecuenciaCrossover:
        cont = 0
        hijo1 = []
        # hijo2 = []
        hijo1.append(padre1[0])
        # hijo2.append(padre2[0])
        genBuscado = padre2[0]
        cont += 1
        listaUsados = []
        listaUsados.append(padre1[0])
        while (cont <= len(padre1) - 1):
            if (padre1[cont] == genBuscado):
                hijo1.append(padre1[cont])
                listaUsados.append(padre1[cont])
                # hijo2.append(padre2[cont])
                genBuscado = padre2[cont]
            else:
                if(padre2[cont] in listaUsados):
                    hijo1.append(padre1[cont])
                    listaUsados.append(padre1[cont])
                else:
                    hijo1.append(padre2[cont])
                    # hijo2.append(padre1[cont])
            cont += 1
    else:
        hijo1 = padre1
        # hijo2 = padre2

    print(listaUsados)
    return hijo1


padre1 = [3,7,5,8,9,12,18,6,1,13,10,2,17,21,4,14,19,11,16,20,15]
padre2 = [6,9,10,5,13,7,12,4,17,3,15,18,2,19,20,1,16,11,8,21,14]

hijo=[]
hijo = crossoverCiclico(padre1,padre2)
print("padre1: ",padre1)
print("padre2: ",padre2)
print("hijo: ",hijo)
