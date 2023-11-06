'''
'EJERCICIO 1'

for i in range (1,101):
    if i%7 == 0 and i%13 == 0:
        print(f'{i} (múltiplo de 7 y 13)')
    elif i%7 == 0:
        print(f'{i} (múltiplo de 7)')
    elif i%13 == 0:
        print(f'{i} (múltiplo de 13)')
    else:
        print(i)

'EJERCICIO 2'

number = int(input("Enter a number: "))

for i in range (1,11):
    print(f'{number}*{i}={number*i}')


'EJERCICIO 3'

number = int(input("How many numbers do you want input?: "))
contador = 0

while contador < number:
    num = int(input("Enter a number greater than 0: "))
    while num <= 0:
        num = int(input("The number is not valid, it should be greater than 0: "))
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
    contador+=1
print("FINISH, WELL DONE!")


'EJERCICIO 4'
number = int(input("Enter one number greater than 0: "))
suma = 0

while number <= 0:
    number = int(input("The number is not right, try again: "))

for i in range(1,number+1):
    suma+=i
print(f'The sum of the {number} first number is {suma}')


'EJERCICIO 5'

num = int(input("Enter a number (negative to finish): "))
contadorPositivos = 0

while num > 0:
    if num > 0:
        contadorPositivos += 1
    num = int(input("Enter a number (negative to finish): "))
print(f'You have entered {contadorPositivos} positive numbers')

'EJERCICIO 6'

number1 = int(input("Enter one number:"))
number2 = int(input("Enter one number:"))
resultado = 0
contador = 0

while contador < number2:
    resultado += number1
    contador+=1
print(f"The product is {resultado}")

'EJERCICIO 7'

number = int(input("How many numbers do you want to input: "))
contador = 0
suma = 0

while contador < number:
    num = int(input("Enter one number greater than 0: "))
    while num < 0:
        num = int(input("The number is not valid, it should be greater than 0: "))
    suma += num
    contador+=1
print(f'The medium is {suma/number}')


'EJERCICIO 8'

number = int(input("Enter one number: "))
question = input("Do you want to enter more numbers? (Y/N): ").upper()
menor = number

while question == 'Y':
    otherNum = int(input("Enter one number: "))
    if otherNum < menor:
        menor = otherNum
    question = input("Do you want to enter more numbers? (Y/N): ").upper()

print(f'The smallest number is {menor}')

'EJERCICIO 9'

number = int(input("Enter one number: "))
suma = 0

while number < 0:
    number = int(input("Enter one number: "))

for i in range(1,number):
    if number%i == 0:
        suma += i
if suma == number:
    print("The number is perfect")
else:
    print("The number is not perfect")


'EJERCICIO 10'

number = int(input("Enter one number greater than 0: "))
resultado = 1

if number == 0:
    print('The factorial is 1')

elif number == 1:
    print('The factorial is 1')

elif number == 2:
    print('The factorial is 2')

else:
    while number < 0:
        number = int(input("Invalid number, try again: "))

    for i in range (1,number+1):
        resultado*=i
    
    print(f'The factorial is {resultado}')
'''







