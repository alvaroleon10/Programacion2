'EJERCICIO 1'

'''
menu =""" 
Bienvenido a Amazon Jacarandá, siguiendo este menu,
A) Añadir cliente
B) Mostrar los % de clientes premium y normales
G) Salir
Seleccione una de las opciones: 
"""
opcion = input(menu).upper()
personasPremium = 0
personasNormales = 0
nPersonas = 0

while opcion != 'G':


    if opcion == 'A':
        question = input("¿Su cuenta es premium? (S/N): ").upper()
        if question == 'S':
            personasPremium += 1
            nPersonas+=1
        elif question == 'N':
            personasNormales += 1
            nPersonas+=1
        else:
            print("Respuesta incorrecta")
        correo = input("Introduzca su correo electrónico: ")

    elif opcion == 'B':
        porcentajePremium = (personasPremium/nPersonas)*100
        porcentajeNormales = (personasNormales/nPersonas)*100

        print(f'El porcentaje correspondiente a personas premium es de {porcentajePremium}%')
        print(f'El porcentaje correspondiente a personas no premium es de {porcentajeNormales}%')
    
    else:
        print("Opción errónea")
    
    opcion = input(menu).upper()

'''
'EJERCICIO 2'

menu =""" 
Bienvenido a Amazon Jacarandá, siguiendo este menu,
A) Añadir cliente
B) Mostrar los % de clientes premium y normales
G) Salir
Seleccione una de las opciones: 
"""
opcion = input(menu).upper()
personasPremium = 0
personasNormales = 0
nPersonas = 0
importeMaxPremium = 0
productoPMasCaro = 0
codArtPMasCaro = ""
precioUnitarioProCaro = 0
unidadesProductoMasCaro = 0
codArtNMasVendido = ""
listaCodigosArt = []

while opcion != 'G':
    if opcion == 'A':
        contadorProductos = 0
        question = input("¿Su cuenta es premium? (S/N): ").upper()
        if question == 'S':
            personasPremium += 1
            nPersonas+=1
            nProductos = int(input("¿Cuántos productos ha adquirido?: "))
            while contadorProductos < nProductos:
                codArticuloPremium = int(input("Introduzca el código del artículo: "))
                if codArticuloPremium < 0:
                    print("Error de código de artículo")
                unidadesPremium = int(input("Cuántas unidades de dicho artículo ha adquirido?: "))
                precioUnitarioPremium= float(input("Precio unitario del artículo: "))
            importeMayor = nProductos*unidadesPremium*precioUnitarioPremium
            if importeMayor > importeMaxPremium:
                importeMaxPremium = importeMayor
            if precioUnitarioPremium > productoPMasCaro:
                productoPMasCaro = precioUnitarioPremium
                codArtPMasCaro = codArticuloPremium
                precioUnitarioProCaro = precioUnitarioPremium
                unidadesProductoMasCaro = unidadesPremium

        elif question == 'N':
            personasNormales += 1
            nPersonas+=1
            nProductos = int(input("¿Cuántos productos ha adquirido?: "))
            while contadorProductos < nProductos:
                codArticuloNormales = int(input("Introduzca el código del artículo: "))
                if codArticuloNormales < 0:
                    print("Error de código de artículo")
                listaCodigosArt.append(codArticuloNormales)
                unidadesNormales = int(input("Cuántas unidades de dicho artículo ha adquirido?: "))
                precioUnitarioNormales = float(input("Precio unitario del artículo: "))
            
        else:
            print("Respuesta incorrecta")
        correo = input("Introduzca su correo electrónico: ")
        
    elif opcion == 'B':
        porcentajePremium = (personasPremium/nPersonas)*100
        porcentajeNormales = (personasNormales/nPersonas)*100

        print(f'El porcentaje correspondiente a personas premium es de {porcentajePremium}%')
        print(f'El porcentaje correspondiente a personas no premium es de {porcentajeNormales}%')
    
    elif opcion == 'C':
        porcentajePremium = (personasPremium/nPersonas)*100
        print(f'El porcentaje correspondiente a personas premium es de {porcentajePremium}%')
        print(f'El importe máximo gastado en un pedido premium es de {importeMaxPremium}')
        print(f'Sobre el artículo más caro tenemos estos datos: CodArticulo: {codArtPMasCaro}, precioUnitario de: {precioUnitarioProCaro} y {unidadesProductoMasCaro} unidades')

    elif opcion == 'D':
        porcentajeNormales = (personasNormales/nPersonas)*100
        print(f'El porcentaje correspondiente a personas no premium es de {porcentajeNormales}%')
    else:
        print("Opción errónea")
    
    opcion = input(menu).upper()

