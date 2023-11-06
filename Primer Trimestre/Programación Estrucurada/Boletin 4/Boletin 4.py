'''
'EJERCICIO 1'

import math

cateto1 = float(input("Cateto 1: "))
cateto2 = float(input("Cateto 2: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print(f"La hipotenusa es: {hipotenusa}")

'EJERCICIO 2'

fahrenheit = float(input("Temperatura Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")


'EJERCICIO 3'
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

media = (num1 + num2 + num3) / 3
print(f"La media es: {media}")


'EJERCICIO 4'
total_compra = float(input("Ingrese el total de la compra: "))
descuento = 0.15 * total_compra
precio_final = total_compra - descuento
print(f"El cliente pagará: {precio_final} euros.")


'EJERCICIO 5'
num1 = float(input("Introduzca un número: "))
num2 = float(input("Introduzca otro número: "))

distancia = abs(num1 - num2)
print(f"La distancia es: {distancia}")


'EJERCICIO 6'
x1 = int(input("Coordenada x del primer punto: "))
y1 = int(input("Coordenada y del primer punto: "))
x2 = int(input("Coordenada x del segundo punto: "))
y2 = int(input("Coordenada y del segundo punto: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La distancia entre los dos puntos es: {distancia}")

'EJERCICIO 7'
import math

numero = int(input("Introduzca un número: "))
raiz_cuadrada = math.sqrt(numero)
raiz_cubica = numero**(1/3)
print(f"La raíz cuadrada es: {raiz_cuadrada}")
print(f"La raíz cúbica es: {raiz_cubica}")


'EJERCICIO 8'
monedas_2e = int(input("Cantidad de monedas de 2 euros: "))
monedas_1e = int(input("Cantidad de monedas de 1 euro: "))
monedas_50c = int(input("Cantidad de monedas de 50 céntimos: "))
monedas_20c = int(input("Cantidad de monedas de 20 céntimos: "))
monedas_10c = int(input("Cantidad de monedas de 10 céntimos: "))

total_euros = 2 * monedas_2e + 1 * monedas_1e + 0.5 * monedas_50c + 0.2 * monedas_20c + 0.1 * monedas_10c
total_céntimos = int((total_euros - int(total_euros)) * 100)

print(f"Tienes {int(total_euros)} euros y {total_céntimos} céntimos.")

'EJERCICIO 9'
base = int(input("Introduzca la base: "))
exponente = int(input("Introduzca el exponente: "))

if exponente > 0:
    resultado = base**exponente
elif exponente == 0:
    resultado = 1
else:
    resultado = 1 / (base**abs(exponente))

print(f"El resultado es: {resultado}")


'EJERCICIO 10'

lado_A = int(input("Introduzca un número: "))
lado_B = int(input("Introduzca otro número: "))
lado_C = int(input("Introduzca otro número: "))

if (lado_A**2) + (lado_B**2) == lado_C:
    print("Es triángulo rectángulo")
elif (lado_A == lado_B and lado_B != lado_C and lado_A != lado_C) or (lado_A == lado_C and lado_B != lado_C and lado_A != lado_B) or (lado_C == lado_B and lado_B != lado_A and lado_A != lado_C):
    print("Es triángulo isósceles")
elif (lado_A == lado_B and lado_B == lado_C and lado_C == lado_A):
    print("Es triángulo equilátero")
else:
    print("Es triángulo escaleno")

'EJERCICIO 11'

anio = int(input("Introduzca un año: "))

if (anio%4!=0) and (anio%400!=0):
    print("No es año bisiesto")
elif (anio%4 == 0) and (anio%100 != 0) and (anio%400 == 0):
    print("Si es bisiesto")

'EJERCICIO 12'

tipoUva = input("Tipo de la uva (A/B): ")
tamanioUva = int(input("Tamaño de la uva: "))

if tipoUva == 'a' or tipoUva == 'A':
    if tamanioUva == 1:
        print("Se le cargan 20 céntimos al precio inicial")
    elif tamanioUva == 2:
        print("Se le cargan 30 céntimos al precio inicial")
elif tipoUva == 'b' or tipoUva == 'B':
    if tamanioUva == 1:
        print("Se rebajan 30 céntimos al precio inicial")
    elif tamanioUva == 2:
        print("Se rebajan 50 céntimos al precio inicial")


'EJERCICIO 13'

alumnos = int(input("Número de alumnos que asistirán a la excursión: "))

if alumnos >= 100:
    print("Cada alumno deberá pagar 65 euros")
elif alumnos >= 50 and alumnos < 100:
    print("Cada alumno deberá pagar 70 euros")
elif alumnos >= 30 and alumnos < 50:
    print("Cada alumnos deberá pagar 95 euros")
else:
    print("El costo de la renta del autobús es de 4000 euros")


'EJERCICIO 14'

llamada = input("Día en el que se realiza la llamada: ").upper()
turno = input("Turno en el que se realiza la llamada (mañana/tarde): ").upper()
duracion = int(input("¿Cuántos minutos duró la llamada?: "))
costeLlamada = 0

if duracion <= 5:
    costeLlamada += 1
    if llamada == 'DOMINGO':
        costeLlamada += 1*0.03
    elif llamada != 'DOMINGO':
        if turno == 'MAÑANA':
            costeLlamada += 1*0.15
        elif turno == 'TARDE':
            costeLlamada += 1*0.10
    print(f'El coste de esta llamada es de: {costeLlamada}€')
elif duracion > 5 and duracion <= 8:
    costeLlamada += 0.8
    if llamada == 'DOMINGO':
        costeLlamada += 0.8*0.03
    elif llamada != 'DOMINGO':
        if turno == 'MAÑANA':
            costeLlamada += 0.8*0.15
        elif turno == 'TARDE':
            costeLlamada += 0.8*0.10
    print(f'El coste de esta llamada es de: {costeLlamada}€')
elif duracion > 8 and duracion <= 10:
    costeLlamada += 0.7
    if llamada == 'DOMINGO':
        costeLlamada += 0.7*0.03
    elif llamada != 'DOMINGO':
        if turno == 'MAÑANA':
            costeLlamada += 0.7*0.15
        elif turno == 'TARDE':
            costeLlamada += 0.7*0.10
    print(f'El coste de esta llamada es de: {costeLlamada}€')
else:
    costeLlamada += 0.5
    if llamada == 'DOMINGO':
        costeLlamada += 0.5*0.03
    elif llamada != 'DOMINGO':
        if turno == 'MAÑANA':
            costeLlamada += 0.5*0.15
        elif turno == 'TARDE':
            costeLlamada += 0.5*0.10
    print(f'El coste de esta llamada es de: {costeLlamada}€')


'EJERCICIO 15'

dia = int(input("Introduzca un número correspondiente a un día de la semana: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("ERROR, dicho número no corresponde a ningún día")

'EJERCICIO 16'

mes = int(input("Introduzca un número correspondiente a algún mes: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("Dicho mes tiene 31 días")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Dicho mes tiene 30 días")
elif mes == 2:
    print("Dicho mes, al ser febrero tiene 28 días")
else:
    print("ERROR, dicho número no corresponde con ningún mes")

'EJERCICIO 17'

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
menor = 0
otro = 0

if num1 < num2:
    menor = num1
    otro = num2
elif num2 < num1:
    menor = num2
    otro = num1

for i in range(menor,otro):
    if i%2==0:
        print(i)


'EJERCICIO 18'

limInferior = int(input("Introduzca un límite inferior: "))
limSuperior = int(input("Introduzca un límite superior: "))
suma = 0
numerosFuera = 0
coinciden = 0

while limInferior > limSuperior:
    limSuperior = int(input("Introduzca un límite superior: "))

numero = int(input("Introduzca un número: "))
while numero != 0:
    if numero > limInferior and numero < limSuperior:
        suma += numero
    if numero <= limInferior or numero >= limSuperior:
        numerosFuera += 1
    if numero == limInferior or numero ==limSuperior:
        coinciden += 1
    numero = int(input("Introduzca un número: "))

print(f"La suma de los números que están dentro del intervalo es: {suma}")
print(f'Hay {numerosFuera} números fuera del intervalo')
print(f'Coinciden {coinciden} números con los intervalos')



'EJERCICIO 19'

base = int(input("Introduzca la base: "))
exponente = int(input("Introduzca el exponente: "))
contador = 0
resultado = 1

if exponente < 0:
    print("ERROR")

if exponente == 0:
    print(f'El resultado es {resultado}')

elif exponente == 1:
    print(f'El resultado es {base}')

else:
    while contador < exponente:
        resultado*= base
        contador += 1
    print(f'El resultado es {resultado}')
    

'EJERCICIO 20'

contadorMeses = 1
cantidadTotal = 10

while contadorMeses <= 20:
    print(f'En el mes número {contadorMeses} pagará {cantidadTotal} euros')
    cantidadTotal*=2
    contadorMeses+=1
print(f'La cantidad total a pagar después de los 20 meses será de {cantidadTotal} euros')

'EJERCICIO 21'

numerosPrimos = int(input("¿Cuántos números primos desea mostrar?: "))

for i in range(2,numerosPrimos):
    if numerosPrimos%i != 0:
        print(i)

'''




