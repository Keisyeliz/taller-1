import os
os.system('cls')
var_totalGFlt =0
cons_computadorescritorioInt = 1000000 
cons_computadorportatilInt = 1500000
cons_tabletasInt = 500000
cons_videobeamInt = 400000
cons_tvInt = 800000

cant_computadorportatil = 0
total_computadorportatil = 0
cant_computadorescritorio = 0
total_computadorescritorio = 0
cant_tabletas = 0
total_tabletas = 0
cant_videobeam = 0
total_videobeam = 0
cant_tv = 0
total_tv = 0


var_nombreStr = input('Nombre del cliente -> ') 
var_contactoStr = input('Contacto del cliente -> ')
var_direccionStr = input('direccion del cliente -> ')
var_controlBln = True
while var_controlBln ==True:
    os.system('cls')
    print('cliente:  ',var_nombreStr)
    var_opcionStr = int(input('---MENÚ DE OPCIONES---\n\n1. computador portatil\n2. computador de escritorio\n3. Tabletas\n4. videobeam\n5. tv\n6. Facturar\n -> '))
    if var_opcionStr >= 1 and var_opcionStr <= 5:
        var_cantidadInt = int(input('Ingrese la cantidad->'))
        
    if var_opcionStr == 1:
        var_totalGFlt += (var_cantidadInt * cons_computadorportatilInt)
        cant_computadorportatil = var_cantidadInt
        total_computadorportatil = (var_cantidadInt * cons_computadorportatilInt)

        
    if var_opcionStr == 2:
        var_totalGFlt += (var_cantidadInt * cons_computadorescritorioInt)
        cant_computadorescritorio = var_cantidadInt
        total_computadorescritorio = (var_cantidadInt * cons_computadorescritorioInt)
    
    if var_opcionStr == 3:
        var_totalGFlt += (var_cantidadInt * cons_tabletasInt)
        cant_tabletas = var_cantidadInt
        total_tabletas = (var_cantidadInt * cons_tabletasInt)

    if var_opcionStr == 3:
        var_totalGFlt += (var_cantidadInt * cons_videobeamInt)
        cant_videobeam = var_cantidadInt
        total_videobeam = (var_cantidadInt * cons_videobeamInt)

    if var_opcionStr == 4:
        var_totalGFlt += (var_cantidadInt * cons_tvInt)
        cant_tv = var_cantidadInt
        total_tv = (var_cantidadInt * cons_tvInt)
        
    if var_opcionStr == 6:
            print('<<<<FACTURA>>>>')
            print('Nombre del cliente: ',var_nombreStr)
            print('Contacto del cliente: ',var_contactoStr)
            print('Direccion del cliente: ',var_direccionStr)
            print("Computadores portatiles: ", cant_computadorportatil,'$',total_computadorportatil)
            print("Computadores de escritorio: ", cant_computadorescritorio,'$',total_computadorescritorio)
            print("Tabletas: ", cant_tabletas,'$',total_tabletas)
            print("Videobeams: ", cant_videobeam,'$',total_videobeam)
            print("Televisores: ", cant_tv, '$',total_tv)

            print('El total a pagar es $',var_totalGFlt)
            print('Gracias por su compra')
            var_controlBln = False



   
