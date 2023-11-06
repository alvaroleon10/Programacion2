'''
'EJERCICIO 1'

nota = int(input("Introduzca una nota: "))

if nota >= 0 and nota <= 49:
    print("Suspenso")
elif nota >= 50 and nota <= 59:
    print("Suficiente")
elif nota >= 60 and nota <= 69:
    print("Bien")
elif nota >= 70 and nota <= 89:
    print("Notable")
elif nota >= 90 and nota <= 100:
    print("Sobresaliente")
else:
    print("Nota no válida")

'EJERCICIO 2'

dia = int(input("Introduzca dia: "))
mes = int(input("Introduzca mes: "))
hemisferio = input("¿Hemisferio norte o sur? N/S: ").upper()


if (mes==10 or mes==11) or (23<=dia<=31 and mes==9) or (mes==12 and 1<=dia<=21):
    if hemisferio == "NORTE":
        print("Es otoño")
    elif hemisferio == "SUR":
        print("Es primavera")
        
if (mes==1 or mes==2) or (21<=dia<=31 and mes==12) or (mes==3 and 1<=dia<=21):
    if hemisferio == "NORTE":
        print("Es verano")
    elif hemisferio == "SUR":
        print("Es invierno")
'''

'EJERCICIO 3'

fecha = input("Introduzca fecha: (formato dd-mm-yyyy): ")

