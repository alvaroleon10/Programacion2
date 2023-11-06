'EJERCICIO 1'
'''
numero = int(input("Introduzca un número: "))

if numero%2 == 0:
    print("El número es par")

else:
    print("El número es impar")

'EJERCICIO 2'

num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))

if num1 == num2:
    print("Los números introducidos son iguales")
elif num1 > num2:
    print("El primer numero es mayor que el segundo")
else:
    print("El segundo numero introducido es mayor que el primero")

'EJERCICIO 3'

num = int(input("Introduzca un número: "))

if num%2 == 0 and num%3 == 0:
    print("El número introducido es multiplo de 2 y 3")
elif num%2 == 0:
    print("El número introducido es multiplo de 2")
elif num%3 == 0:
    print("El numero introducido es multiplo de 3")

'EJERCICIO 4'

edad = int(input("Introduzca edad: "))

while edad >= 100:
    edad = int(input("Edad debe ser menor que 100 años, pruebe otra vez: "))
if edad >= 0 and edad <= 12:
        print("Niño")
elif edad >= 13 and edad <= 17:
        print("Adolescente")
elif edad >= 18 and edad <= 29:
        print("Joven")
else:
        print("Adulto")


'EJERCICIO 5'

num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca un número: "))
num3 = int(input("Introduzca un número: "))
num4 = int(input("Introduzca un número: "))

media = (num1+num2+num3+num4)/4
print("La media es " + str(media))
if num1 > media:
       print(num1)
if num2 > media:
       print(num2)
if num3 > media:
       print(num3)
if num4 > media:
       print(num4)

'EJERCICIO 6'

caracter = input("Introduzca un caracter: ")

if caracter == 'a' or caracter == 'A':
    print("Es la vocal A")
if caracter == 'e' or caracter == 'E':
    print("Es la vocal E")
if caracter == 'i' or caracter == 'I':
    print("Es la vocal I")
if caracter == 'o' or caracter == 'O':
    print("Es la vocal O")
if caracter == 'u' or caracter == 'U':
    print("Es la vocal U")

'EJERCICIO 7'

estadoCivil = input("Introduzca su estado civil (S/V/C/D): ").upper()
edad = int(input("Introduzca su edad: "))

if estadoCivil == 'S' or estadoCivil == 'D' and edad < 35:
    print("Le corresponde un 12% de retención")
elif edad > 50:
    print("Le corresponde un 8'5% de retención")
elif estadoCivil == 'V' or estadoCivil == 'C' and edad < 35:
    print("Le corresponde un 11'3% de retención")
else:
    print("Le corresponde un 10'5% de retención")


'EJERCICIO 8'

hora1 = int(input("Introduzca una hora: "))
minutos1 = int(input("Introduzca minutos: "))
segundos1 = int(input("Introduzca segundos: "))

hora2 = int(input("Introduzca una hora: "))
minutos2 = int(input("Introduzca minutos: "))
segundos2 = int(input("Introduzca segundos: "))

if hora1 > 0 and hora1 < 24 and hora2 > 0 and hora2 < 24 and minutos1 >= 0 and minutos1 < 60 and minutos2 >= 0 and minutos2 < 60 and segundos1 >= 0 and segundos1 < 60 and segundos2 >= 0 and segundos2 < 60 :
    if hora1 > hora2:
        print("Hora 1 es mayor")
    elif hora2 < hora1:
        print("Hora 2 es mayor")
    elif hora1 == hora2:
        if minutos1 > minutos2:
            print("Hora 1 es mayor")
        elif minutos2 > minutos1:
            print("Hora 2 es mayor")
        elif minutos1 == minutos2:
            if segundos1 > segundos2:
                print("Hora 1 es mayor")
            elif segundos2 > segundos1:
                print("Hora 2 es mayor")
            elif segundos1 == segundos2:
                print("Las horas son iguales")


'EJERCICIO 9'

tipoProducto = input("¿Qúe tipo de producto es? (A/B/C): ").upper()
precioProducto = float(input("Precio del producto: "))

if tipoProducto == 'A':
    print("Se le aplica un 7% de descuento")
elif tipoProducto == 'C' or precioProducto < 500:
    print("Se le aplicará un 12% de descuento")
else:
    print("9% de descuento")


'EJERCICIO 10'

num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))
caracter = input("Introduzca un operador aritmetico: ")

if caracter == '+':
    print(f'La suma entre los dos numeros es: {num1+num2}')
elif caracter == '-':
    print(f'La resta es: {num1-num2}')
elif caracter == '*':
    print(f'El producto es: {num1*num2}')
elif caracter == '/':
    print(f'La división es igual a: {num1/num2}')
else:
    print("ERROR, operador aritmético inválido")
'''