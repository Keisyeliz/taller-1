var_numInt = int(input('ingrese la cantidad de números a evaluar -> '))
contador = 0

for i in range(var_numInt):
    num = float(input('Ingrese el número -> '))
    if num >= 10 and num <= 20:
        contador += 1
        
print('la cantidad de número dentro del rango es:',contador)
    