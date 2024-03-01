
codigoInt = int(input('Código-> '))
nombreStr = input('Nombre -> ')
existenciasInt = 0
controlBln = True
import os
while controlBln == True:
    os.system('cls')
    print('codigo: ',codigoInt,' \nNombre: ',nombreStr,'\nExistencias: ',existenciasInt)
    var_opcionStr = int(input('1. Compras\n2. Ventas\n3. Reportes\n4. Salir\n -> '))
    if var_opcionStr >= 1 and var_opcionStr <= 2:
        cantidadInt = int(input('Ingrese la cantidad->'))
    
    if var_opcionStr == 1:
        existenciasInt += cantidadInt
        
    if var_opcionStr == 2:
        if cantidadInt <= existenciasInt:
            existenciasInt -= cantidadInt
        else:
            print('\nNo hay suficientes existencias')
        enter = input('<ENTER>')

    if var_opcionStr == 3:
        print('Cantidad actual de inventario:', existenciasInt)
        
    if var_opcionStr == 4:
        controBln = False
