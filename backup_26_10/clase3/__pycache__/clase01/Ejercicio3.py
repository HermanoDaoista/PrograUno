# 3.Ingresar dos números mostrar desde el primer número hasta el segundo que ingresaron de manera ascendente, en caso de que el primer número sea mayor al segundo mostrarlos en orden descendente, si los números son iguales, mostrar sólo ese número.
# Por ejemplo: Si ingresaron 5 como primer número y 7 como segundo mostrar (5-6-7), si el primer número que ingresaron es 7 y el segundo un 5 mostrar (7-6-5)


numero_uno = input('ingrese primer numero ')
numero_uno = int(numero_uno)

numero_dos = input('Ingrese numero segundo ')
numero_dos = int(numero_dos)

if numero_uno > numero_dos:

        for i in range(numero_uno, numero_dos-1, -1):
                 print(i)
else:
        if numero_dos > numero_uno:
                
                for i in range(numero_uno-1, numero_dos, 1):
                        
                        print(i+1)
        else:
                print(numero_dos)        