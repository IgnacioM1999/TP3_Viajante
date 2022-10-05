# TP Viajante

import itertools
import numpy

diccionarioObjetos = {'Ciudad de Buenos Aires': [[0, 646, 792, 933, 53, 986, 985, 989, 375, 834, 1127, 794, 2082, 979, 1080, 1334, 1282, 1005, 749, 393, 579, 939, 2373, 799] , [ -34.6082787, -58.3708681]],
                      'Cordoba':[[646, 0, 677, 824, 698, 340, 466, 907, 348, 919, 1321, 669, 2281, 362, 517, 809, 745, 412, 293, 330, 577, 401, 2618, 1047] , [-31.4135, -64.18105]],
                      'Corrientes':[[792, 677, 0, 157, 830, 814, 1131, 1534, 500, 291, 1845, 13, 2819, 691, 633, 742, 719, 1039, 969, 498, 1136, 535, 3131, 1527] , [ -27.461195,-58.836841]],
                      'Formosa': [[933, 824, 157, 0, 968, 927, 1269, 1690, 656, 263, 1999, 161, 2974, 793, 703, 750, 741, 1169, 1117, 654, 1293, 629, 3284, 1681], [-26.18489, -58.17313]] ,
                      'La Plata': [[53, 698, 830, 968, 0, 1038, 1029, 1005, 427, 857, 1116, 833, 2064, 1030, 1132, 1385, 1333, 1053, 795, 444, 602, 991, 2350, 789] , [-34.92145, -57.95453]],
                      'La Rioja': [[986, 340, 814, 927, 1038, 0, 427, 1063, 659, 1098, 1548, 802, 2473, 149, 330, 600, 533, 283, 435, 640, 834, 311, 2821, 1311] , [-29.414280, -66.855750]],
                      'Mendoza': [[985, 466, 1131, 1269, 1029, 427, 0, 676, 790, 1384, 1201, 1121, 2081, 569, 756, 1023, 957, 152, 235, 775, 586, 713, 2435, 1019] , [-32.882293, -68.859762]],
                      'Neuquen': [[989, 907, 1534, 1690, 1005, 1063, 676, 0, 1053, 1709, 543, 1529, 1410, 1182, 1370, 1658, 1591, 824, 643, 1049, 422, 1286, 1762, 479], [-38.952136, -68.059230]] ,
                      'Parana': [[375, 348, 500, 656, 427, 659, 790, 1053, 0, 658, 1345, 498, 2320, 622, 707, 959, 906, 757, 574, 19, 642, 566, 2635, 1030] , [-31.745060, -60.518284]],
                      'Posadas': [[834, 919, 291, 263, 857, 1098, 1384, 1709, 658, 0, 1951, 305, 2914, 980, 924, 1007, 992, 1306, 1200, 664, 1293, 827, 3207, 1624] , [-27.388928, -55.918591]],
                      'Rawson': [[1127, 1321, 1845, 1999, 1116, 1548, 1201, 543, 1345, 1951, 0, 1843, 975, 1647, 1827, 2120, 2054, 1340, 1113, 1349, 745, 1721, 1300, 327] , [-43.299332, -65.102075]],
                      'Resistencia': [[794, 669, 13, 161, 833, 802, 1121, 1529, 498, 305, 1843, 0, 2818, 678, 620, 729, 706, 1029, 961, 495, 1132, 523, 3130, 1526] , [-27.451791, -58.987015]],
                      'Rio Gallegos': [[2082, 2281, 2819, 2974, 2064, 2473, 2081, 1410, 2320, 2914, 975, 2818, 0, 2587, 2773, 3063, 2997, 2231, 2046, 2325, 1712, 2677, 359, 1294], [-51.625838, -69.221658]] ,
                      'S.F.d.V.d. Catamarca': [[979, 362, 691, 793, 1030, 149, 569, 1182, 622, 980, 1647, 678, 2587, 0, 189, 477, 410, 430, 540, 602, 915, 166, 2931, 1391] , [-28.468759, -65.779600]],
                      'S.M. de Tucuman': [[1080, 517, 633, 703, 1132, 330, 756, 1370, 707, 924, 1827, 620, 2773, 189, 0, 293, 228, 612, 727, 689, 1088, 141, 3116, 1562] , [-26.822205, -65.211730]],
                      'S.S. de Jujuy': [[1334, 809, 742, 750, 1385, 600, 1023, 1658, 959, 1007, 2120, 729, 3063, 477, 293, 0, 67, 874, 1017, 942, 1382, 414, 3408, 1855] , [-24.186368, -65.299711]],
                      'Salta': [[1282, 745, 719, 741, 1333, 533, 957, 1591, 906, 992, 2054, 706, 2997, 410, 228, 67, 0, 808, 950, 889, 1316, 353, 3341, 1790], [-24.812486, -65.410616]] ,
                      'San Juan': [[1005, 412, 1039, 1169, 1053, 283, 152, 824, 757, 1306, 1340, 1029, 2231, 430, 612, 874, 808, 0, 284, 740, 686, 583, 2585, 1141] , [-31.537198, -68.525925]],
                      'San Luis': [[749, 293, 969, 1117, 795, 435, 235, 643, 574, 1200, 1113, 961, 2046, 540, 727, 1017, 950, 284, 0, 560, 412, 643, 2392, 882] , [-33.292094, -66.314007]],
                      'Santa Fe': [[393, 330, 498, 654, 444, 640, 775, 1049, 19, 664, 1349, 495, 2325, 602, 689, 942, 889, 740, 560, 0, 641, 547, 2641, 1035] , [-31.621989, -60.696438]],
                      'Santa Rosa': [[579, 577, 1136, 1293, 602, 834, 586, 422, 642, 1293, 745, 1132, 1712, 915, 1088, 1382, 1316, 686, 412, 641, 0, 977, 2044, 477], [-36.620794, -64.281901]] ,
                      'Santiago del Estero': [[939, 401, 535, 629, 991, 311, 713, 1286, 566, 827, 1721, 523, 2677, 166, 141, 414, 353, 583, 643, 547, 977, 0, 3016, 1446], [-27.799076, -64.258781]] ,
                      'Ushuaia': [[2373, 2618, 3131, 3284, 2350, 2821, 2435, 1762, 2635, 3207, 1300, 3130, 359, 2931, 3116, 3408, 3341, 2585, 2392, 2641, 2044, 3016, 0, 1605], [-54.816960, -68.330233]] ,
                      'Viedma': [[799, 1047, 1527, 1681, 789, 1311, 1019, 479, 1030, 1624, 327, 1526, 1294, 1391, 1562, 1855, 1790, 1141, 882, 1035, 477, 1446, 1605, 0], [-40.820035, -63.001845]] }
                

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
        #print("Se encontro un 0 => distancias de las otras ciudades sin el cero:",distanciasSinCero)
        distanciaMinima = min(distanciasSinCero)
    kmTotal = distanciaMinima
    print("distancia minima: ",distanciaMinima)
    #print("distaciasOtrasCiudades:", distanciasOtrasCiudades)
    indice = distanciasOtrasCiudadesFijas.index(distanciaMinima) #este indice es el indice de la ciudad en la lista distanciaOtrasCiudades que tiene la distancia mas corta con ciudadActual
    #print("el indice en distanciaOtrasCiudadesFijas de la distancia minima:",indice)
    c = ciudades[indice]
    #print("La distancia mas corta hacia la otra ciudad es: ", distanciaMinima, "correspondiente a:", c)
    return c, indice, kmTotal

def distanciaCortaCiudadInicial(ciudadInicial, indiceCiudadInicial, ciudadActual):
    l = []
    distancias = []
    #print("la ultima ciudad que se recorrio es:", ciudadActual)
    l.extend(diccionarioObjetos.get(ciudadActual))
    distancias.extend(l[0])
    distanciaACiudadInicial = distancias[indiceCiudadInicial]
    #print("La distancia hacia la ciudad inicial ", ciudadInicial," es:", distanciaACiudadInicial)
    return distanciaACiudadInicial 
    

#FUNCION PRINCIPAL
ciudades = []
ciudades.extend(list(diccionarioObjetos.keys()))
ciudadesMostrar = []
ciudadesMostrar.extend(list(diccionarioObjetos.keys()))
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
distanciasOtrasCiudadesFijas = []
a = list(diccionarioObjetos.get(ciudadActual))
distanciasOtrasCiudadesFijas.extend(a[0]) #esta lista se usa para, una vez obtenido el valor de la distanciaMinima, obtener el indice de ese valor y asi saber que ciudad es
distanciasOtrasCiudadesV2 = []
b = list(diccionarioObjetos.get(ciudadActual))
distanciasOtrasCiudadesV2.extend(b[0]) #en esta lista se van a eliminar las ciudades que ya se han recorrido
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
    d = list(diccionarioObjetos.get(ciudadActual))
    distanciasOtrasCiudadesFijas.extend(d[0])
    distanciasOtrasCiudadesV2.clear()
    e = list(diccionarioObjetos.get(ciudadActual))
    distanciasOtrasCiudadesV2.extend(e[0])
    print("distanciasOtrasCiudadesV2 antes de hacer el pop(remover elemento):",distanciasOtrasCiudadesV2)
    print("indice ciudades recorridas:",indiceCiudadesRecorridas)
    for r in indiceCiudadesRecorridas:
        distancia = distanciasOtrasCiudadesFijas[r]
        distanciasOtrasCiudadesV2.remove(distancia)
        #print("distancias otras ciudadesV2:",distanciasOtrasCiudadesV2)
    print("distanciasOtrasCiudadesV2 despues del pop:", distanciasOtrasCiudadesV2)
    print()
recorridos.append(ciudadInicial)
indiceCiudadInicial=ciudades.index(ciudadInicial)
kmTotal += distanciaCortaCiudadInicial(ciudadInicial, indiceCiudadInicial, ciudadActual)
print("el recorrido mas corto a todas las ciudades es:", recorridos,"con una cantidad de km recorridos de:", kmTotal)


        
#si es por heuristica, cuando estoy en una ciudad, hay que ver las distancias con esa ciudad y ver la mas chica.
# no se hace falta armar todas las soluciones porque sino se esta haciendo la exaustiva 

#SUMAR LOS KILOMETROS DE LA ULTIMA CIUDAD A LA CIUDAD INICIAL Y PONER COMO ULTIMA CIUDAD LA CIUDAD INICIAL

