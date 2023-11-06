num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca un número: "))
num3 = int(input("Introduzca un número: "))

numeroMayor = 0
numeroMenor = 0
numeroMedio = 0

while (num1 > 0 and num2 > 0) or (num1 > 0 and num3 > 0) or (num2 > 0 and num3 > 0) or (num1 > 0 and num2 > 0 and num3 > 0):
    if num1 < num2 and num1 < num3:
        numeroMenor = num1
    elif num1 > num2 and num1 > num3:
        numeroMayor = num1
    elif (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
        numeroMedio = num1
    if num2 < num1 and num2 < num3:
        numeroMenor = num2
    elif num2 > num1 and num2 > num3:
        numeroMayor = num2
    elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
        numeroMedio = num2
    if num3 < num2 and num3 < num1:
        numeroMenor = num3
    elif num3 > num2 and num3 > num1:
        numeroMayor = num3
    elif (num3 > num2 and num3 < num1) or (num3 < num2 and num3 > num1):
        numeroMedio = num3
    print(f'Los numeros introducidos ordenados de mayor a menor quedarían así: {numeroMenor}, {numeroMedio}, {numeroMayor}')
    print("---------------------------------------------------------------------------------------------------------------")
    num1 = int(input("Introduzca un número: "))
    num2 = int(input("Introduzca un número: "))
    num3 = int(input("Introduzca un número: "))
print("ERROR")
print("Dos o más números de los que se han introducido son iguales o menores que cero")

