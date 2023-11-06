'MOCK EXAM'
'''
'EJERCICIO 1'

eleccion1 = input("Elija un piedra, papel, tijera, lagarto o spock: ").upper()
eleccion2 = input("Elija un piedra, papel, tijera, lagarto o spock: ").upper()

while not(eleccion1 == 'PIEDRA' or eleccion1 == 'PAPEL' or eleccion1 == 'TIJERA' or eleccion1 == 'LAGARTO' or eleccion1 == 'SPOCK') or not(eleccion2 == 'PIEDRA' or eleccion2 == 'PAPEL' or eleccion2 == 'TIJERA' or eleccion2 == 'LAGARTO' or eleccion2 == 'SPOCK'):
    print("Elemento erróneo, vuelva a introducir los dos valores")
    print("------------------------------------------------------")
    eleccion1 = input("Elija un piedra, papel, tijera, lagarto o spock: ").upper()
    eleccion2 = input("Elija un piedra, papel, tijera, lagarto o spock: ").upper()
if eleccion1 == 'PIEDRA' and (eleccion2 == 'LAGARTO' or eleccion2 == 'TIJERA'):
    print("Gana piedra")
elif eleccion1 == 'LAGARTO' and (eleccion2 == 'SPOCK' or eleccion2 == 'PAPEL'):
    print("Gana lagarto")
elif eleccion1 == 'SPOCK' and (eleccion2 == 'TIJERA' or eleccion2 == 'PIEDRA'):
    print("Gana spock")
elif eleccion1 == 'TIJERA' and (eleccion2 == 'LAGARTO' or eleccion2 == 'PAPEL'):
    print("Gana tijera")
elif eleccion1 == 'PAPEL' and (eleccion2 == 'PIEDRA' or eleccion2 == 'SPOCK'):
    print("Gana papel")
elif eleccion2 == 'PIEDRA' and (eleccion1 == 'LAGARTO' or eleccion1 == 'TIJERA'):
    print("Gana piedra")
elif eleccion2 == 'LAGARTO' and (eleccion1 == 'SPOCK' or eleccion1 == 'PAPEL'):
    print("Gana lagarto")
elif eleccion2 == 'SPOCK' and (eleccion1 == 'TIJERA' or eleccion1 == 'PIEDRA'):
    print("Gana spock")
elif eleccion2 == 'TIJERA' and (eleccion1 == 'LAGARTO' or eleccion1 == 'PAPEL'):
    print("Gana tijera")
elif eleccion2 == 'PAPEL' and (eleccion1 == 'PIEDRA' or eleccion1 == 'SPOCK'):
    print("Gana papel")
elif eleccion1 == eleccion2:
    print("EMPATE")



'''
'EJERCICIO 3'

tamanioEmpresa = int(input("¿Cuántas personas hay en la empresa?: "))
while tamanioEmpresa < 0:
    tamanioEmpresa = int(input("Número de empleados inválido, pruebe de nuevo: "))
contadorPersonas = 0
contadorPython = 0
contadorJava = 0
contadorHombresPython = 0
contadorMujeresPython = 0
contadorHombresJava = 0
contadorMujeresJava = 0
edadPython = 1
edadJava = 1

while contadorPersonas < tamanioEmpresa:

    edad = int(input("Introduzca su edad: "))
    while edad < 18 or edad > 65:
        edad = int(input("Edad inválida, debe ser entre 18 y 65 años, pruebe de nuevo: "))
    sexo = input("Introduzca su sexo (M/H): ").upper()
    while sexo != "H" and sexo != "M":
        sexo = input("Sexo inválido, pruebe de nuevo: ").upper()
    lenguaje = input("Introduzca su lenguaje de programación habitual (python o java): ").upper()
    while lenguaje != 'JAVA' and lenguaje != 'PYTHON':
        lenguaje = input("Lenguaje inválido, pruebe de nuevo: ").upper()

    if lenguaje == 'PYTHON':
        contadorPython+=1
        edadPython+=edad
        if sexo=='H':
            contadorHombresPython+=1
        elif sexo == 'M':
            contadorMujeresPython+=1
    
    elif lenguaje == 'JAVA':
        contadorJava+=1
        edadJava+=edad
        if sexo=='H':
            contadorHombresJava+=1
        elif sexo=='M':
            contadorMujeresJava+=1

    contadorPersonas+=1

mediaEdadPython = edadPython/contadorPython
mediaEdadJava = edadJava/contadorJava
porcentajePython = (contadorPython/tamanioEmpresa)*100 
porcentajeJava = (contadorJava/tamanioEmpresa)*100

print(f'El {porcentajePython}% de empleados utiliza Python, de los que {contadorHombresPython} son hombres y {contadorMujeresPython} son mujeres y su edad media es de {mediaEdadPython}')
print(f'El {porcentajeJava}% de empleados utiliza Java, de los que {contadorHombresJava} son hombres y {contadorMujeresJava} son mujeres y su edad media es de {mediaEdadJava}')

