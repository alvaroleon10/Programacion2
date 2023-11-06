'''
'EJERCICIO 1'

numero = int(input("Write an integer number: "))

def calcularFactorial(numero):
    resultado = 1
    for i in range(1,numero+1):
        resultado *= i
    return resultado

print(calcularFactorial(numero))

'EJERCICIO 2'
year = int(input("Write a year: "))

def isLeapYear(year):
    mensaje = True
    if (year%4==0 and year%100 == 0):
        mensaje = False
    elif year%4 == 0:
        mensaje = True
    elif (year%100 == 0 and year%400) == 0:
        mensaje = True
    elif (year%100==0):
        mensaje = False
    else:
        print("ERROR")
    return mensaje

print(isLeapYear(year))

'EJERCICIO 3'

month = input("Write a month: ").upper()

def computeDaysInMonth(month):
    dias = 0
    if (month == 'ENERO' or month == 'MARZO' or month == 'MAYO' or month == 'JULIO' or month == 'AGOSTO' or month == 'OCTUBRE' or month == 'DICIEMBRE'):
        dias = 31
    elif (month == 'ABRIL' or month == 'JUNIO' or month == 'SEPTIEMBRE' or month == 'NOVIEMBRE'):
        dias = 30
    elif (month == 'FEBRERO'):
        dias = 28
    else:
        print("ERROR")
    return dias

print(computeDaysInMonth(month))

'EJERCICIO 4'

fecha = [9,9,2003]

def getDayOfWeek (fecha):
    a = (14 - fecha[1]) / 12
    y = fecha[2] - a
    m = fecha[1] + 12 * a - 2
    d = (fecha[0] + y + y/4 - y/100 + y/400 + (31*m)/12) % 7
    return d

print(getDayOfWeek(fecha))

'EJERCICIO 5'

base = int(input("Write a number: "))
exponente = int(input("Write another number: "))

def powerlt(base,exponente):
    resultado = 1
    contador = 0
    while contador < exponente:
        resultado*=base
        contador+=1
    if exponente == 0:
        resultado = 0
    return resultado

print(powerlt(base,exponente))

'EJERCICIO 6'

num = 4567
numeros = ["0","1","2","3","4","5","6","7","8","9"]
def getNumberOfDigits(num, numeros):
    num1 = str(num)
    digitos = 0
    for i in num1:
        if i in numeros :
            digitos += 1
        else:
            pass
    return digitos
print(getNumberOfDigits(num, numeros))

'EJERCICIO 7'

num = int(input("Write one number: "))

def isPrime(num):
    primo = True
    for i in range(2,num):
        if num%i==0:
            primo=False
    return primo

print(isPrime(num))

'EJERCICIO 8'

from math import sqrt
a = 10
b = 4
c = 7
def solveSecondOrderEquation(a,b,c):
    if not(((b**2)-4*a*c) > 0):
        return None
    else:
        x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)  
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)  
    return x1,x2
print(solveSecondOrderEquation(a, b, c))

'EJERCICIO 9'

number = int(input("Write one number: "))

def getPrimeDivisors(number):
    primos = []
    divisores = []
    for i in range(2,number):
        primo = True
        if number%i == 0:
            primo = False
        else:
            primos.append(i)
    for i in primos:
        if number%i == 0:
            divisores.append(i)
    return divisores

print(getPrimeDivisors(number))

'EJERCICIO 10'

num1 = 10
num2 = 8

def isFriendNumber(num1,num2):
    resultado1 = 0
    resultado2 = 0
    friends = True
    for i in range(1,num1-1):
        if num1%i==0:
            resultado1+=i
    for i in range(1,num2-1):
        if num2%i==0:
            resultado2+=i
    if resultado1 == num2 and resultado2 == num1:
        friends = True
    else:
        friends = False
    return friends

print(isFriendNumber(num1,num2))
'''
    

            
    
        

