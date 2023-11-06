'''
num = int(input("Introduzca un número: "))

for x in range(1,11):
    print(f'{num} x {x} = {num*x}')

print("-------------------")

i = 1

while i < 20:
    print("Hala Madrid")
    i += 1

print("-------------------")

indice = 1
num = int(input("Introduzca un número: "))

while indice < 11:
    print(f'{num} x {indice} = {num*indice}')
    indice += 1

'''

MENU_PRINCIPAL = '''
          Menú principal:
          ---------------
            1. Ingresar
            2. Sacar
            3. Consultar balance
            4. Imprimir menú
            5. Salir
      '''
  
print(MENU_PRINCIPAL)
opcion = int(input("Introduzca una opción: "))
total = 0

while opcion != 5:

  if opcion==1:
    cantidad = int(input("Introduzca la cantidad a ingresar: "))
    while cantidad < 0: 
      cantidad = int(input("Introduzca una cantidad válida: "))
    total +=cantidad

  elif opcion==2:
    cantidad = int(input("Introduzca la cantidad a sacar: "))
    while cantidad < 0 and cantidad > total: 
      cantidad = int(input("Introduzca una cantidad válida: "))
    total -=cantidad
  
  elif opcion==3:
    print(f"El saldo actual es de {total}€")

  elif opcion==4:
    print(MENU_PRINCIPAL)
  
  # Podemos utilizar el operador de multiplicación para repetir cadenas de texto
  # y la suma para concatenar cadenas:
  print("\n"*2+"*"*30)
  opcion = int(input("Introduzca una opción: "))
