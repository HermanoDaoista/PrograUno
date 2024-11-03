# 4.Se ingresan un máximo de 5 números o hasta que el usuario ingrese el número 0. Mostrar la suma y promedio de los mismos.

sumador_numeros = 0
contador_vueltas = 0

for i in range(5):

    ingrese_numero = input('Ingrese un numero ')
    ingrese_numero = int(ingrese_numero)

    if ingrese_numero == 0:
        break
    
    sumador_numeros += ingrese_numero
    contador_vueltas += 1
    
promedio_suma = sumador_numeros / contador_vueltas 

print(f'La suma es {sumador_numeros} y el promedio es {promedio_suma}')