# 7.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

contador_primo = 0

ingrese_numero = input('Ingrese un numero ')
ingrese_numero = int(ingrese_numero)

for n in range(2, ingrese_numero +1):
    bandera = True
    for i in range(2,n):
        if n % i == 0:
            bandera = False
            break
    if bandera:

        contador_primo += 1
        print(F'{n}')

print(f'Hay {contador_primo} numeros primos')          
        

        


