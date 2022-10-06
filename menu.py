#import CodigoTP3.py
#import TP3SinInput.py
from io import open
from os import system


salir = False
opcion = 0
 
while not salir:
    
    print ("1) Opcion A (Busqueda heurística a partir de ingreso de ciudad por el usuario")
    print ("2) Opcion B (Búsqueda heurística de cada ciudad")
    print ("3) Opcion C (Algortimo Genético con torneo)")
    print ("4) Opcion D (Algortimo Genético con torneo más elitismo)")
    print ("5) Salir")    
 
    opcion = input("Elige una opcion: ")
 
    if opcion == '1':
        system('cls')
        exec(open("CodigoTP3.py").read())
        system('pause')
    elif opcion == '2':
        system('cls')
        exec(open("TP3SinInput.py").read())
        system('pause')
    elif opcion == '3':
        system('cls')
        exec(open("TP3conAlgoritmoGenetico.py").read())   #solo torneo
        system('pause')
    elif opcion == '4':
        system('cls')
        exec(open("TP3conAlgoritmoGeneticoTorneoyElitismo.py").read()) #torneo y elitismo 
        system('pause')
    elif opcion == '5':
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
        system('pause')

    system('cls')
