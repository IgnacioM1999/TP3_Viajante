import random

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

print("cromosoma mutado: ", cromosomaMutado)