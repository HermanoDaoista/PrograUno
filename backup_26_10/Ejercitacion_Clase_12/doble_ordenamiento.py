# Ejercitación Clase 12 (Ordenamiento Doble Criterio y Introducción a Cadenas)

# ORDENAMIENTO DOBLE CRITERIO

# 1. Realizar una función que me permita ordenar una matriz de productos [nombre,precio,stock] por precio de mayor a menor y tomando como segundo criterio el stock (mayor a menor también)
from funciones import *
import operator


planilla = [['pilsen',267,98],
            ['fortin',267,76],
             ['coca', 1000, 5],
            ['pepsi',1000,98],
            ['tupy',1788,8]]
def ordenar_por_precio_y_stock(matriz:list[list]):
    I_PRECIO = 1
    I_STOCK = 2
    
    for i in range(len(matriz) - 1):
        for j in range(i+1,len(matriz)):
            if matriz[i][I_PRECIO] < matriz[j][I_PRECIO]:
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
            elif matriz[i][I_PRECIO] == matriz[j][I_PRECIO]:
                if matriz[i][I_STOCK] < matriz[j][I_STOCK]:
                    auxiliar = matriz[i]
                    matriz[i] = matriz[j]
                    matriz[j] = auxiliar
    return matriz

# ordenar_por_precio_y_stock(planilla)
# print(f'{'nombre':<10}{'precio':<10}{'stock':<10}')
# for fila in planilla:
#         print(f'{fila[0]:<10} {fila[1]:<10} {fila[2]:<10}')


# 2. Realizar una función que me permita ordenar una matriz de productos [nombre,precio,stock] por precio de mayor a menor y tomando como segundo criterio el nombre (alfabeticamente)
def ordenar_por_precio_y_nombre(matriz:list[list]):
    I_PRECIO = 1
    I_NOMBRE = 0
    
    for i in range(len(matriz) - 1):
        for j in range(i+1,len(matriz)):
            if matriz[i][I_PRECIO] < matriz[j][I_PRECIO]:
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
            elif matriz[i][I_PRECIO] == matriz[j][I_PRECIO]:
                if matriz[i][I_NOMBRE] > matriz[j][I_NOMBRE]:
                    auxiliar = matriz[i]
                    matriz[i] = matriz[j]
                    matriz[j] = auxiliar
    return matriz

# ordenar_por_precio_y_nombre(planilla)


# 3. Realizar una función que me permita ordenar una matriz (cualquiera) por doble criterio , recibirá la matriz a ordenar, el índice de la columna del primer criterio, el índice de la columna del segundo criterio, el orden de ordenamiento (mayor o menor) (mismo para ambos criterios) 
# Se puede usar la matriz del ejercicio 1 como ejemplo

def ordenar_por_doble_criterio(matriz:list[list],columna_uno:int, columna_dos:int,operador):
    for i in range(1,len(matriz)):
        for j in range(i+1,len(matriz)):
            if operador(matriz[i][columna_uno], matriz[j][columna_uno]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
            elif matriz[i][columna_uno] == matriz[j][columna_uno]:
                if operador(matriz[i][columna_dos], matriz[j][columna_dos]):   
                        auxiliar = matriz[i]
                        matriz[i] = matriz[j]
                        matriz[j] = auxiliar
    return matriz     

# funcion_ordenada = ordenar_por_doble_criterio(planilla,1,2,operator.gt)
# print(f'{"Nombre":<10} {"precios":<10} {"Stock":<10}')
# for fila in funcion_ordenada:
#     print(f'{fila[0]:<10} {fila[1]:<10} {fila[2]:<10}')
# funcion_ordenada_uno = ordenar_por_precio_y_stock(planilla)
# print(f'{"Nombre":<10} {"precios":<10} {"Stock":<10}')
# for fila in funcion_ordenada_uno:
#     print(f'{fila[0]:<10} {fila[1]:<10} {fila[2]:<10}')


# 4. Dada la función anterior mejorarla a tal nivel que me permita elegir un orden diferente para cada criterio, por ejemplo capaz quiero ordenar de mayor a menor el primer criterio y de menor a mayor el segundo criterio.
# Usar de base lo desarrollado en el ejercicio 2, debería funcionar para resolver de la misma manera. El criterio del precio se ordenará de mayor a menor y el criterio del nombre alfabéticamente (menor a mayor)


def ordenar_por_dos_criterios_diferentes(matriz:list[list],columna_uno:int,columna_dos:int,operador_uno,operador_dos):
    I_PRECIO = columna_uno
    I_NOMBRE = columna_dos
    
    
    for i in range(len(matriz) - 1):
        for j in range(i+1,len(matriz)):
            if operador_uno(matriz[i][I_PRECIO] , matriz[j][I_PRECIO]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
            elif matriz[i][I_PRECIO] == matriz[j][I_PRECIO]:
                if operador_dos(matriz[i][I_NOMBRE] , matriz[j][I_NOMBRE]):
                    auxiliar = matriz[i]
                    matriz[i] = matriz[j]
                    matriz[j] = auxiliar
    return matriz


    
# ordenar_por_dos_criterios_diferentes(planilla,1,0,operator.lt,operator.gt)
# print(f'{'Nombre':<10} {'Precio':<10} {'Stock':<10}')
# for fila in planilla:
#     print(f'{fila[0]:<10} {fila[1]:<10} {fila[2]:<10}')
