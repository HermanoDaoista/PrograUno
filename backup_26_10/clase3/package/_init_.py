#from package.funciones import *

# import package.funciones as F

# F.Mensaje
# F.sumar_numeros_1

# import pygame

# pygame.display.set_mode([500 , 500])

# running = True
# while running:
#     for event in

def get_int(mensaje: str, minimo: int , maximo: int) -> int:
    reintentos = 0
    numero = input(mensaje)
    numero = int(numero)
    while numero < minimo or numero >  maximo:
        numero = input(f'Error {mensaje}')
        numero = int(numero)
        reintentos += 1
        if reintentos > 1:
            break
    return numero

#numero_ingresado = get_int()

#print(f'El numero ingresado es: {numero_ingresado}')

edad = get_int('ingres edad: ' , 15 , 20) #15-30
#while edad < 15 or edad > 30:
 #   edad = get_int('Ingrese edad: ')
#legajo = get_int('Error-ingrese su lejago') #1500-2756
 #lo mismo para validad
#nota = get_int('ingrese su nota') #1-10
 #lo mismo para validad
3