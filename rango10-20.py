var_numInt = int(input('ingrese la cantidad de números a evaluar -> '))
contadorInt = 1
contadornumInt = 0
while contadorInt <= var_numInt:
    numeroInt = int(input('ingrese un número -> '))
    if numeroInt >= 10 and numeroInt <= 20:
        contadornumInt += 1
    contadorInt += 1
print('La cantidad de números dentro de rango de 10-20 son: ', contadornumInt)
    
