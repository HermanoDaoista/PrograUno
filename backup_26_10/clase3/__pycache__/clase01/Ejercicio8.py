# 8. Ingresar un número y mostrar la tabla de multiplicar de ese número. 

# Por ejemplo si se ingresa el numero 3:
# 3 x 0 = 0 
# 3 x 1  = 3
# 3 x 2 = 6
# 3 x 3  = 9

ingrese_numero = input('Ingrese un numero ')
ingrese_numero = int(ingrese_numero)

for i in range (0 , 11 , 1):
    resultado = ingrese_numero * i
    print(f'{ingrese_numero} x {i} = {resultado}')