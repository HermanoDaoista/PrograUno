from Funciones import *

def sumar_matrices(matrix_a : list[list], matrix_b : list[list])-> list[list]:
    matrix_c = []
    
    for fil in range(len(matrix_a)):
        fila_suma = []
        for col in range (len(matrix_a[fil])):
            suma = matrix_a[fil][col] + matrix_b[fil][col]
            fila_suma.append(suma)
        matrix_c.append(fila_suma)    
    
    return matrix_c   

#matrix_a = [[1,2,3],
#             [3,2,1],
#            [2,5,7]] 
# matrrix_b =[[5,6,7],
#             [7,6,5]]    
# matrix = sumar_matrices(matrix_a , matrrix_b)


def multiplicar_matrices(matriz : list[list] , escalar : int)-> list[list]:
    matriz_m = []
    #
    for fil in range(len(matriz)):
        fila_multiplicada = []
        for col in range(len(matriz[fil])):
            multiplicacion = matriz[fil][col] * escalar
            fila_multiplicada.append(multiplicacion)
        matriz_m.append(fila_multiplicada)    
    return matriz_m


def invertir_matrices(matriz : list[list])-> list[list]:
    matriz_m = []
    #
    for fil in range(len(matriz)):
        fila_multiplicada = []
        for col in range(len(matriz[fil])):
            multiplicacion = matriz[fil][col] * -1
            fila_multiplicada.append(multiplicacion)
        matriz_m.append(fila_multiplicada)    
    return matriz_m




def trasponer_matriz(matriz : list[list]) -> list[list]:
    
 traspuesta = []

 for _ in range(len(matriz[0])):
     fila_vacia =  [0] * len(matriz)
     traspuesta.append(fila_vacia)

 for i in range(len(matriz)):
     for j in range(len(matriz[i])):
         traspuesta[j][i] = matriz[i][j]

 return traspuesta


def multiplicar_matrices_ej(matriz_a : list[list] , matriz_b : list[list])->list:
    matriz_c = [] 
    suma = 0
    if (len(matriz_a[0]) == len(matriz_b)):
        for i in range(len(matriz_a)):
            fila_multiplicada = []
            for j in range(len(matriz_a[0])):
                multiplicar = matriz_a[i][j] * matriz_b[j][i]
                suma = suma + multiplicar
                fila_multiplicada.append(suma)
            matriz_c.append(fila_multiplicada)
        retorno = matriz_c
    else:
        retorno = matriz_c
    return retorno 



  

        







            
  



