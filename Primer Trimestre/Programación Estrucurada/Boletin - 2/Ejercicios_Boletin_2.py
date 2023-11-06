'EJERCICIO 1'
'''
sueldo_bruto = 2000
sueldo_neto = 1560

print(sueldo_neto==sueldo_bruto-(sueldo_bruto*0.22))

dia_mayo = 19

print(dia_mayo > 1 and dia_mayo < 31)

num1 = 21
num2 = 15

print(num1%3==0 and num2%3==0)

nota = 7

print(nota>=5 and nota<=10)

nota1 = 5
nota2 = 5
nota3 = 5
notamedia = (nota1+nota2+nota3)/3

print(notamedia>=5)

print("---------------")

'EJERCICIO 2'

nota1 = 7
nota2 = 2
nota3 = 5

print(nota1<5 and nota2<5 and nota3<5)

saldo = 1250    
n_veces_descubierto = 6

print(not(saldo < 1000 or n_veces_descubierto > 5))

asignaturasAprobadas = 2
asignaturasCurso = 12

print(not(asignaturasAprobadas < asignaturasCurso*0.30))


mes = 9
dia = 31

print((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia == 31)


print("--------------------------")
'EJERCICIO 3'

a = "lluvia"
b = "sol"
c = "frio"

print(a and not (b) and (not c or not a) and b and not (c or not a)
and (not b and c))
'''
print("--------------------------")

'EJERCICIO 4'

'1. Niega a y afirma b, es decir a es False y b es True, sin embargo al tener un and b se convierte en False ya que a lo es'
'2. Al igual que el caso anterior, vuelve a ser False pero en este caso b se mantiene como True ya que el or no le hace cambiar'
'3. El not not implica una doble negacion, en castellano podría traducirlo como que a no es lo contrario de True, es decir, que no es False, por lo tanto es True'
'4. Tanto a como b presentan una negacion, un not, por lo cual al llevar un or y las dos negarse, tenemos un False'
'5. Si no me equivoco este apartado es igual que el 4 pero escrito de distinta forma ya que en este el not le afecta a ambas variables por estar dentro de un paréntesis'
'6. A diferencia del primer apartado aquí encontramos doble negación con and, por lo cual tenemos un not a (false) y otro not b (false), teniendo and, false y false, se queda false'