num = int(input("Introduzca un número: "))
numAnterior = 1
numPosterior = 10000000000000000000000000000000000000000000000000000000000000000

while num != 0:
    if numAnterior <= num:
        numAnterior = num
        creciente = True
    else:
        creciente = False
    if numPosterior >= num:
        numPosterior = True
        decreciente = True
    else:
        decreciente = False
    if numAnterior == num:
        coinciden = True
    
    num = int(input("Introduzca un número: "))

if creciente == True:
    print("Es creciente")
elif decreciente == True:
    print("Es decreciente")
else:
    print("Esta desordenado")
if coinciden == True:
    print("Hay números iguales")




