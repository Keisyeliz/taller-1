
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
        existenciasInt -= cantidadInt
        if cantidadInt <= existenciasInt:
           existenciasInt -= cantidadInt
        else:
            print ('No hay suficientes existencias')
            
    if var_opcionStr == 3:
        print('Cantidad de existencias actuales del inventario',existenciasInt)
        enter = input ('<ENTER>')
        
    if var_opcionStr == 4:
        controlBln = False

         
