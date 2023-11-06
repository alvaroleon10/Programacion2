'''
'EJERCICIO 2'

menu = """
##############################################
#Bienvenido al IES Jacarandá!!
    1. Alumnos que han entrado.
    2. Alumnos que han abandadonado el centro.
    3. Alumnos en el IES
    4. Salir
##############################################
"""
print(menu)
opcion = int(input("Seleccione una de las opciones anteriores (1/4): "))
totalAlumnos = 0

while opcion != 4:
    if opcion == 1:
        entran = int(input("¿Cuántos alumnos han entrado?: "))
        totalAlumnos += entran
    elif opcion == 2:
        salen = int(input("¿Cuántos alumnos han salido?: "))
        totalAlumnos -= salen
    elif opcion == 3:
        print(f'Actualmente hay {totalAlumnos} en el centro')
    else:
        print("Error, opción no válida")
    print(menu)
    opcion = int(input("Seleccione una de las opciones anteriores (1/4): "))


print("Ha salido del menú")

'''
'EJERCICIO 1'

opcion1 = input("Introduzca un elemento: (piedra,papel,tijera,lagarto,spock): ").upper()
opcion2 = input("Introduzca un elemento: (piedra,papel,tijera,lagarto,spock): ").upper()

while (opcion1 != 'PIEDRA' and opcion1 != 'PAPEL' and opcion1 != 'TIJERA' and opcion1 != 'SPOCK' and opcion1 != 'LAGARTO') or (opcion2 != 'PIEDRA' and opcion2 != 'PAPEL' and opcion2 != 'TIJERA' and opcion2 != 'SPOCK' and opcion2 != 'LAGARTO'):
    print("Uno o los dos elementos que usted ha introducido son incorrectos, pruebe de nuevo")
    print("----------------------------------------------------------------------------------")
    opcion1 = input("Introduzca un elemento: (piedra,papel,tijera,lagarto,spock): ").upper()
    opcion2 = input("Introduzca un elemento: (piedra,papel,tijera,lagarto,spock): ").upper()
if opcion1 == 'LAGARTO' and (opcion2 == 'SPOCK' or opcion2 == 'PAPEL'):
    print(f'{opcion1} GANA A {opcion2}')
elif opcion1 == 'SPOCK' and (opcion2 == 'TIJERA' or opcion2 == 'PIEDRA'):
    print(f'{opcion1} GANA A {opcion2}')
elif opcion1 == 'TIJERA' and (opcion2 == 'PAPEL' or opcion2 == 'LAGARTO'):
    print(f'{opcion1} GANA A {opcion2}')
elif opcion1 == 'PAPEL' and (opcion2 == 'SPOCK' or opcion2 == 'PIEDRA'):
    print(f'{opcion1} GANA A {opcion2}')
elif opcion1 == 'PIEDRA' and (opcion2 == 'LAGARTO' or opcion2 == 'TIJERA'):
    print(f'{opcion1} GANA A {opcion2}')
elif opcion2 == 'LAGARTO' and (opcion1 == 'SPOCK' or opcion1 == 'PAPEL'):
    print(f'{opcion2} GANA A {opcion1}')
elif opcion2 == 'SPOCK' and (opcion1 == 'TIJERA' or opcion1 == 'PIEDRA'):
    print(f'{opcion2} GANA A {opcion1}')
elif opcion2 == 'TIJERA' and (opcion1 == 'PAPEL' or opcion1 == 'LAGARTO'):
    print(f'{opcion2} GANA A {opcion1}')
elif opcion2 == 'PAPEL' and (opcion1 == 'SPOCK' or opcion1 == 'PIEDRA'):
    print(f'{opcion2} GANA A {opcion1}')
elif opcion2 == 'PIEDRA' and (opcion1 == 'LAGARTO' or opcion1 == 'TIJERA'):
    print(f'{opcion2} GANA A {opcion1}')
else:
    print("EMPATAN")