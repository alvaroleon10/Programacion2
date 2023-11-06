'EJERCICIO 1'
'''
from random import randint

listaNumeros = []

for i in range(10):
    listaNumeros.append(randint(0,1000))
print(listaNumeros)

'A'
def obtenerNumeroMayor(listaNumeros):
    mayor = listaNumeros[0]
    for i in range(len(listaNumeros)):
        if listaNumeros[i] > mayor:
            mayor = listaNumeros[i]
    return mayor

'B'
def obtenerNumeroMenor(listaNumeros):
    menor = listaNumeros[0]
    for i in range(len(listaNumeros)):
        if listaNumeros[i] < menor:
            menor = listaNumeros[i]
    return menor

'C'
def obtenerSuma(listaNumeros):
    suma = 0
    for i in range(len(listaNumeros)):
        suma += listaNumeros[i]
    return suma

'D'
def obtenerMedia(listaNumeros):
    contador = 0
    suma = 0
    for i in range(len(listaNumeros)):
        suma += listaNumeros[i]
        contador+=1
    media = suma/contador
    return media

'E'
def sustituirValor(listaNumeros):
    posicion = int(input("¿Qué posición desea cambiar?(0/9): "))
    while posicion < 0 or posicion > 9:
        posicion = int(input("Error, debe estar entre 1 y 10, pruebe de nuevo: "))
    numeroSustituto = int(input("¿Qué número desea introducir?(1/1000): "))
    while numeroSustituto < 1 or numeroSustituto > 1000:
        numeroSustituto = int(input("El número debe estar entre 1 y 1000, pruebe de nuevo: "))
    for i in range(len(listaNumeros)):
        if i == posicion:
            listaNumeros[i] = numeroSustituto
    return listaNumeros

    

print(obtenerNumeroMayor(listaNumeros))
print(obtenerNumeroMenor(listaNumeros))
print(obtenerSuma(listaNumeros))
print(obtenerMedia(listaNumeros))
print(sustituirValor(listaNumeros))

'EJERCICIO 2'

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def desplazar (lista):
    escribe = lista[0]
    guarda = 0
    for i in range(len(lista)):
        if i == len(lista)-1:
            lista[0] = escribe
        else:
            guarda = lista[(i+1)]
            lista[(i+1)] = escribe
            escribe = guarda       
    return (lista)

print(desplazar(lista))
'EJERCICIO 3'

dia = int(input("Introduzca un día del mes (1-31): "))
mes = int(input("Un mes del año (1-12): "))
anio = int(input("Un año cualquiera: "))
listaMeses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

while dia > 0:
    def obtenerFecha(dia,mes,anio):
        cadena = ""
        for i in range(len(listaMeses)+1):
            if i == mes:
                mes = listaMeses[i-1]
        cadena = f"La fecha en formato largo es {dia} de {mes} de {anio}"
        return cadena

    print(obtenerFecha(dia,mes,anio))
    dia = int(input("Introduzca un día del mes (1-31): "))
    mes = int(input("Un mes del año (1-12): "))
    anio = int(input("Un año cualquiera: ")) 


'EJERCICIO 4'

num = int(input("Introduzca un número: "))
listaNumeros = []

while num >= 0:
    listaNumeros.append(num)
    num = int(input("Introduzca un número: "))

def mostrarMayor(listaNumeros):
    mayor = 0
    for i in range(len(listaNumeros)):
        mayor = listaNumeros[0]
        if listaNumeros[i] > mayor:
            mayor = listaNumeros[i]
    return mayor

def mostrarPares(listaNumeros):
    listaPares = []
    for i in range(len(listaNumeros)):
        if listaNumeros[i]%2 == 0:
            listaPares.append(listaNumeros[i])
    return listaPares

print(mostrarMayor(listaNumeros))
print(mostrarPares(listaNumeros))

'EJERCICIO 5'

lista = ['Dí', 'buen', 'día', 'a', 'papá']

def riversada(lista):
    nuevaLista = []
    for i in range(len(lista),0,-1):
        nuevaLista.append(lista[i-1])
    return nuevaLista

print(riversada(lista))

'EJERCICIO 6'

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def estaOrdenada(lista):
    mensaje = True
    for i in range(len(lista)):
        if i == lista[i-1]:
            mensaje = True
        else:
            mensaje = False
    return mensaje

print(estaOrdenada(lista))

'EJERCICIO 7'

ficha1 = [2,1]
ficha2 = [3,4]
ficha1Valor1 = 0
ficha1Valor2 = 0
ficha2Valor1 = 0
ficha2Valor2 = 0

def encajan(ficha1,ficha2):
    encajan = True
    for i in range(len(ficha1)):
        ficha1Valor1 = ficha1[0]
        ficha1Valor2 = ficha1[1]
    for i in range(len(ficha2)):
        ficha2Valor1 = ficha2[0]
        ficha2Valor2 = ficha2[1]
    if (ficha1Valor1 == ficha2Valor1 or ficha1Valor1 == ficha2Valor2) or (ficha1Valor2 == ficha2Valor1 or ficha1Valor2 == ficha2Valor2):
        encajan = True
    else:
        encajan = False
    return encajan

print(encajan(ficha1,ficha2))

'EJERCICIO 8'
listaNums = []

num = int(input("Introduzca un número: "))

while num > 0:
    listaNums.append(num)
    num = int(input("Introduzca un número: "))

def numerosPrimos(listaNums):
    esPrimo = True
    listaPrimos = []
    
    for i in range (2,len(listaNums)):
        if listaNums[i]%i==0:
            esPrimo = False 
        else:
            listaPrimos.append(listaNums[i])
            esPrimo = True
    return listaPrimos

def sumatorioLista(listaNums):
    suma = 0
    for i in range(len(listaNums)):
        suma += listaNums[i]
    return suma

def mediaValores(listaNums):
    suma = 0
    contador = 0
    media = 0
    for i in range(len(listaNums)):
        suma+= listaNums[i]
        contador+=1
    media = suma/contador
    return media

'Apartado sin acabar'
def factorial(listaNums):
    listaFactous = []
    for i in range(len(listaNums)):
        factorial = 0
        contador = 0
        while contador < listaNums[i-1]:
            for i in range (1,listaNums[i]+1):
                factorial *= i
            listaFactous.append(factorial)
            contador+=1
    return listaFactous

print(numerosPrimos(listaNums))
print(sumatorioLista(listaNums))
print(mediaValores(listaNums))
print(factorial(listaNums))

'EJERCICIO 9'

listaNumeros = [4, 8, 19, 33, 45]

variableEntera = int(input("¿Qué valor le quiere dar a su variable 'k': "))

def mostrarMenores(listaNumeros):
    listaMenores = []
    for i in range(len(listaNumeros)):
        if listaNumeros[i] < variableEntera:
            listaMenores.append(listaNumeros[i])
    return listaMenores

def mostrarMayores(listaNumeros):
    listaMayores = []
    for i in range(len(listaNumeros)):
        if listaNumeros[i] > variableEntera:
            listaMayores.append(listaNumeros[i])
    return listaMayores

def mostrarMultiplos(listaNumeros):
    listaMultiplos = []
    for i in range(len(listaNumeros)):
        if variableEntera%listaNumeros[i]==0:
            listaMultiplos.append(listaNumeros[i])
    return listaMultiplos

print(mostrarMenores(listaNumeros))
print(mostrarMayores(listaNumeros))
print(mostrarMultiplos(listaNumeros))

'EJERCICIO 10'

numero = "101101B"

def conversor(numero):
    lista2 = []
    if numero[-1] == "B":
        numero = numero[0:len(numero)-1]
        for i in numero:
            if int(i) > 1:
                assert Exception("Los numeros binarios no son mayores que 1")
        n = 0
        for n in numero:
            lista2.append(n)
        x = 0
        y = len(lista2)-1
        producto = 0
        while x < len(lista2):
            producto += int(lista2[x]) * (2 ** y)
            x += 1
            y -= 1
        return producto
    if numero [-1] == "D":
        numero = numero[0:len(numero)-1]
        for i in numero:
            if not (0<=int(i)<9):
                assert Exception("La base decimal debe ser entre 0 y 9")
        numero = int(numero)
        binario = 0
        multiplicador = 1
        while numero != 0:
            binario += numero%2 * multiplicador
            numero //= 2
            multiplicador *= 10
        return binario
        
print (conversor(numero))


'EJERCICIO 11'
lista1 = [10,6,10,23,80]
lista2 = [3,9,80,10,10]
listaRepes = []
valorLista1 = 0

def intersect(lista1,lista2):
    for i in range(len(lista1)):
        valorLista1 = lista1[i]
        for i in range(len(lista2)):
            if lista2[i] == valorLista1 and valorLista1 not in listaRepes:
                listaRepes.append(valorLista1)
                
    return listaRepes

print(intersect(lista1,lista2))    

'EJERCICIO 12'
lista1 = [1,2,3,4,5,4]
lista2 = [3,4,5,6,4]
nuevaLista = []

def unionListas(lista1,lista2):
    for i in range(len(lista1)):
        if lista1[i] not in nuevaLista:
            nuevaLista.append(lista1[i])
    for i in range(len(lista2)):
        if lista2[i] not in nuevaLista:
            nuevaLista.append(lista2[i])
    return nuevaLista

print(unionListas(lista1,lista2))

'EJERCICIO 13'
listaNombres = ['Alvaro', 'Jose', 'Andrés', 'Anselmo', 'Juan', 'Anastasia']
letra = 'A'
valor = ''
nombres = []

def letraNombre (listaNombres, letra):
    for i in range(len(listaNombres)):
        valor = listaNombres[i]
        if valor[0] == letra:
            nombres.append(valor)
    return nombres

print(letraNombre(listaNombres,letra))

'EJERCICIO 14'

lista1 = [2, 4, 5, 7, 8, 10]
lista2 = [5, 19, 6, 38]
lista3 = [5, 0, 12, 52, 67, 33, 10]

def medirCadena (lista1, lista2, lista3):
    x = 0
    while x < len(lista1) and x < len(lista2) and x < len(lista3):
        if len(lista2) < len(lista1) > len(lista3):
            print("Lista 1 es la cadena más larga")
        elif len(lista1) < len(lista2) > len(lista3):
            print("Lista 2 es la cadena más larga")
        else:
            print("Lista 3 es la cadena más larga")
        x += 1

print(medirCadena(lista1,lista2,lista3))
'''



        




    