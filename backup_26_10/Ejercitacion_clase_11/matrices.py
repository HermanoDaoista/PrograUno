from funciones import *
import operator


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:10}', end= ' ')
        print('')    
#6 y 8. Crear una función para ordenar por apellido una matriz que tenga dos columnas (nombre-apellido) de la A-Z o viceversa dependiendo de un parámetro que se le envíe.
import operator
matrix = [['selim','ayala'],
          ['mario', 'bala'],
          ['raul', 'suarez'],
          ['ariel', 'martinez'],
          ['pedro', 'lopez']]

def ordenar_por_apellido(matriz: list[list], operador, fila: int):
    """ordena una matriz alfabeticamente, tambien funciona con enteros

    Args:
        matriz (list[list]): _recibe una matriz_
        operador (_type_): _recibe parametro de la funcion operator_
        fila (int): _un entero que representa la columna de la matriz que vamos a ordenar_

    Returns:
        _type_: _description_
    """
    for i in range(len(matriz) - 1):
        for j in range(i+1,len(matriz)):
            if operador(matriz[i][fila], matriz[j][fila]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
        
    return matriz

def ordenar_por_numero(matriz: list[list], operador, fila: int):
    """ordena una matriz alfabeticamente, tambien funciona con enteros

    Args:
        matriz (list[list]): _recibe una matriz_
        operador (_type_): _recibe parametro de la funcion operator_
        fila (int): _un entero que representa la columna de la matriz que vamos a ordenar_

    Returns:
        _type_: _description_
    """
    for i in range(len(matriz) - 1):
        for j in range(i+1,len(matriz)):
            if operador(matriz[i][fila], matriz[j][fila]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
        
    return matriz

            
# respuesta = ordenar_por_apellido(matrix , operator.gt, 0)
# mostrar_matriz(respuesta)
# 8. Vamos a guardar la información de un jugador de fútbol en una matriz con las siguientes columnas (nombre,apellido, partidos,goles,asistencias) 
# debemos:

# 1-Mostrar tabla de goleadores
# 2-Mostrar tabla de asistencias
# 3-Los 5 jugadores con más partidos.
# 4-Mostrar top 3 jugadores con más goles 
# 5-Mostrar top 3 jugadores con menos asistencias

# prode = [['pipi','romagnoli',5,1,3],
#          ['juan','saturno',10,7,1],
#          ['julian','centurion',4,5,4],
#          ['pepin', 'rodriguez',3,0,0],
#          ['mario','rata',4,0,0]]
prode = inicializar_matriz(5,5,0)

cargar_fulbito(prode)

encabezado = ['Nombre     ','Apellido         ','Partidos    ','Goles      ','Asistencias']

I_NOMBRE = 0
I_APELLIDO = 1
I_PARTIDOS = 2
I_GOLES = 3
I_AISTENCIAS = 4
 
#tabla de goleadores, tengo que ordenar mayor de la columna I_GOLES
 
 
# goleadores = ordenar_por_numero(prode, operator.lt, I_GOLES)
# imprimir_encabezado(encabezado)
# print('')
# mostrar_matriz(goleadores)

#tabla de asistencias, tengo que ordenar mayor de la columna I_ASISTENCIAS

# asistencias = ordenar_por_numero(prode,operator.lt,I_AISTENCIAS)
# imprimir_encabezado(encabezado)
# print('')
# mostrar_matriz(prode)

#los 5 primeros con mas partidos, ordeno mayor de fila partidos e imprimo solo los 5 primeros 

# partidos = ordenar_por_numero(prode,operator.lt,I_PARTIDOS)
# imprimir_encabezado(encabezado)
# print('')
# imprimir_por_filas(partidos,len(partidos))

#top 3 goleadores, imprimo los tres primeros
# partidos = ordenar_por_numero(prode,operator.lt,I_GOLES)
# print('               TOP GOLEADORES TORNEO APERTURA 89')
# print('')
# imprimir_encabezado(encabezado)
# print('')
# imprimir_por_filas(partidos,3)

#top 3 con menos asistencias, calculo menor de I_ASISTENCIAS e imprimo los tres primeros
# menos_asistencias = ordenar_por_numero(prode,operator.gt,I_AISTENCIAS)
# print('               TOP COMILONES TORNEO APERTURA 89')
# print('')
# imprimir_encabezado(encabezado)
# print('')
# imprimir_por_filas(menos_asistencias,3)



