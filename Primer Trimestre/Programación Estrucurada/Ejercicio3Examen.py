menu = '''
Buenas!! Bienvenido al apartado de incidencias del IES JACARANDÁ
----------------------------------------------------------------
'''
nIncidentes = 0
nLeves = 0
nModerados = 0
nGraves = 0
nEso = 0
nPost = 0

print(menu)
pregunta = input("¿Desea usted incluir un nuevo incidente? (S/N): ").upper()

while pregunta != 'S' and pregunta != 'N':
    pregunta = input("Disculpe las molestias, pero debe responder con sí(S) o no(N): ").upper()

while pregunta == 'S':
    tipoIncidente = input("Introduzca el tipo de incidente. Leve(L), Moderado(M) o Grave(G): ").upper()
    while tipoIncidente != 'L' and tipoIncidente != 'M' and tipoIncidente != 'G':
        tipoIncidente = input("Disculpe las molestias, pero debe responder L/M/G: ").upper()
    if tipoIncidente == 'L':
        nLeves += 1
    elif tipoIncidente == 'M':
        nModerados += 1
    else:
        nGraves += 1
    nivel = input("¿En que nivel se ha producido este incidente? ESO(E) o Post-Obligatoria(P): ").upper()
    while nivel != 'E' and nivel != 'P':
        nivel = input("Disculpe las molestias, pero debe responder con E/P: ").upper()
    if nivel == 'E':
        nEso += 1
    else:
        nPost += 1
    nIncidentes += 1
    print("Gracias, el incidente quedó registrado con éxito!")
    pregunta = input("¿Desea usted incluir un nuevo incidente? (S/N): ").upper()

porcentajeEso = (nEso/nIncidentes)*100
porcentajePost = (nPost/nIncidentes)*100
print(f'Se han producido {nIncidentes} incidentes en el centro: {nLeves} de ellos son leves, {nModerados} moderados y {nGraves}, siendo el {porcentajeEso}% en ESO y el {porcentajePost}% en Post-Obligatoria')





