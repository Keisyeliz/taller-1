

codigoInt = int(input('Código-> '))
nombreStr = input('Nombre -> ')
existenciasInt = 0
controlBln = True
import os
while controlBln == True:
    os.system('cls')
    print('codigo: ',codigoInt,' \nNombre: ',nombreStr,'\nExistencias: ',existenciasInt)
    opcionStr = input('1. Compras\n2. Ventas\n3. Reportes\n4. Salir\n -> ')
    cantidadInt = int(input('Cantidad-> '))
    
    if opcionStr == '1':
        existenciasInt += cantidadInt
        
    if opcionStr == '2':
        existenciasInt -= cantidadInt
        if cantidadInt <= existenciasInt:
           existenciasInt -= cantidadInt
        else:
            print ('No hay suficientes existencias')
            
    if opcionStr == '3':
        print('Cantidad de existencias actuales del inventario',existenciasInt)
        enter = input ('<ENTER>')
        
    if opcionStr == '4':
        controlBln = False