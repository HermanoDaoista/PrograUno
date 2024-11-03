from funciones import * 

import operator
# def cargar_bailando(matriz:list[list])->list[list]:
#     I_BAILARIN = 0
#     I_JURADO_UNO = 1
#     I_JURADO_DOS = 2
#     I_JURADO_TRES = 3
#     I_PROMEDIO = 4
#     suma_notas = 0
#     numero_bailarin = 0
    
#     for fil in range(len(matriz)):
#         numero_bailarin +=1
#         jurado_uno =  pedir_numero('Ingrese nota: ', 'Error ingrese un numero del 1 al 10: ', 1 , 10)
#         jurado_dos =  pedir_numero('Ingrese nota: ', 'Error ingrese un numero del 1 al 10: ', 1 , 10)
#         jurado_tres =  pedir_numero('Ingrese nota: ', 'Error ingrese un numero del 1 al 10: ', 1 , 10)
#         suma = jurado_uno + jurado_dos + jurado_tres
#         nota_promedio = suma / 3
#         promedio_redondo = round(nota_promedio,2)

#         matriz[fil][I_BAILARIN] = numero_bailarin
#         matriz[fil][I_JURADO_UNO] = jurado_uno
#         matriz[fil][I_JURADO_DOS] = jurado_dos
#         matriz[fil][I_JURADO_TRES] = jurado_tres
#         matriz[fil][I_PROMEDIO] = promedio_redondo
        
    
#     return matriz

# bailando = inicializar_matriz(5,5,0)
# cargar_bailando(bailando)
# mostrar_matriz(bailando)


def ordenar_por_numero(matriz: list[list], operador, fila: int)-> list[list]:
    """ordena una matriz alfabeticamente, tambien funciona con enteros

    Args:
        matriz (list[list]): _recibe una matriz_
        operador (_type_): _recibe parametro de la funcion operator_
        fila (int): _un entero que representa la columna de la matriz que vamos a ordenar_

    Returns:
        _type_: _ddevuelve una lista anidada
    """
    for i in range(1,len(matriz) - 1):
        for j in range(i+1,len(matriz)):
            if operador(matriz[i][fila], matriz[j][fila]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
        
    return matriz

def imprimir_matriz_encolumnada(matriz: list[list]) -> None:
    for fila in matriz:
        print(f"{fila[0]:<12} {fila[1]:<10} {fila[2]:<10} {fila[3]:<10} {fila[4]:<10}")


# imprimir_matriz_encolumnada(matriz)

# ordenada = ordenar_por_numero(matriz,operator.lt,2)

# imprimir_matriz_encolumnada(ordenada)

def imprimir_lista_encolumna(lista:list)->None:
    """imprime una lista con espacio a elejir

    Args:
        lista (list): una lista
    """
    for i in range(len(lista)):
        print(f'{lista[i]:<16}' , end = '')
        

def encontrar_numero(matriz: list[list], numero:int, columna:int)->None:
    """encuentra conincidencias en una columna de la matriz
    las muestra junto con el encabezado de la fila[0]

    Args:
        matriz (list[list]): recibe una matriz
        numero (int): la coincidencia a bsucar
        columna (int): el lugar donde buscar
    """
    bandera = 0
    matrix = []
    for i in range(len(matriz)):
        if matriz[i][columna] == numero:
            matrix +=  [matriz[i]]
            bandera = 1
           
    if bandera == 1:
        imprimir_lista_encolumna(matriz[0])
        print('')
        mostrar_matriz(matrix)
    else:    
        print('No se encontro')  
def encontrar_aplazados(matriz:list[list], numero:int, columna:int)->list:
    auxiliar = []
   
    for i in range(1,len(matriz)):
        if matriz[i][columna] < numero:
            auxiliar += [matriz[i]]
        
    return  auxiliar  

def imprimir_por_filas(matriz:list[list], filas:int)->None:
    """imprime las filas que le indiques de una matriz

    Args:
        matriz (list[list]): recibe una matriz
        filas (int): la cantidad de filas que queremos imprimir
    """
    for i in range(filas):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:<15}',end='')
        print('')    

def resolver_punto_siete(matriz:list[list],columna_uno:int,columna_dos:int,operador)->list[list]:
    """ordena una matriz por doble criterio

    Args:
        matriz (list[list]): recibe una matriz
        columna_uno (int): primer criterio a comparar
        columna_dos (int): segundo criterio a comparar
        operador (function): la funcion operator que deseamos usar

    Returns:
        list[list]: devulve una matriz ordenada
    """
    bandera_empate = 0
    matriz_empate = []
    for i in range(1,len(matriz) - 1):
        for j in range(i+1,(len(matriz))):
            if operador(matriz[i][columna_uno], matriz[j][columna_uno]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar     
            elif matriz[i][columna_uno] == matriz[j][columna_uno]:
                if operador(matriz[i][columna_dos], matriz[j][columna_dos]):
                            auxiliar = matriz[i]
                            matriz[i]= matriz[j]
                            matriz[j] = auxiliar   
                elif matriz[i][columna_dos] == matriz[j][columna_dos]:
                    bandera_empate = 1
                    matriz_empate  += [matriz[i]]
                    matriz_empate  += [matriz[j]]
    if bandera_empate == 0:
        imprimir_lista_encolumna(matriz[0])
        print('')
        imprimir_lista_encolumna(matriz[1])
    else:
        mostrar_matriz(matriz_empate)     


def encontrar_iguales_en_dos_columnas(matriz:list[list], columna_uno:int, columna_dos:int)->list[list]|None:
    """recorre una mtriz para ver si coinciden en dos columnas diferentes

    Args:
        matriz (list[list]): recibe una matriz
        columna_uno (int): primer criterio
        columna_dos (int): segundo criterio

    Returns:
        list[list]: una matriz o NONE
    """
    matriz_de_iguales = []
    for i in range(len(matriz)-1):
        for j in range(i+1, len(matriz)):
            if matriz[i][columna_uno] == matriz[j][columna_uno] and matriz[i][columna_dos] == matriz[i][columna_dos]:
                matriz_de_iguales += matriz[i]
                matriz_de_iguales += matriz[j]
    return matriz_de_iguales                
                    
matriz = [['Bailarin Nro' ,'Jurado 1 ' ,'Jurado 2 ' ,'Jurado 3 ' , 'promedio'],        
            ['Bailarin 1' ,   9     ,          3        ,       4     ,          7.0],
            ['Bailarin 2' ,   3      ,         3         ,      4         ,      3],
            ['Bailarin 3'  ,   7       ,        7         ,      7        ,       7.0],
            ['Bailarin 4'  ,   7       ,        4          ,     3         ,      7.0],
            ['Bailarin 5'  ,   4         ,      5         ,      6        ,       6.0]]
#resolver_punto_siete(matriz,4,1,operator.gt)


def mostrar_ganador_y_empates(matriz: list[list], columna_uno: int, columna_dos: int, operador) -> None:
    """Ordena una matriz por doble criterio y muestra al ganador o los que empataron.

    Args:
        matriz (list[list]): Recibe una matriz.
        columna_uno (int): Primer criterio (columna 4).
        columna_dos (int): Segundo criterio (columna 1).
        operador (function): Función que define el operador de comparación.
    """
    ganador = matriz[1]  
    empates = []         

    
    for i in range(2, len(matriz)):
        if operador(matriz[i][columna_uno], ganador[columna_uno]):
            
            ganador = matriz[i]
            empates = []  
        elif matriz[i][columna_uno] == ganador[columna_uno]:
            
            if operador(matriz[i][columna_dos], ganador[columna_dos]):
                ganador = matriz[i]  
                empates = []         
            elif matriz[i][columna_dos] == ganador[columna_dos]:
                
                empates += [matriz[i]]

                  
    
    
    if empates:
        imprimir_lista_encolumna(matriz[0])
        print('')
        imprimir_lista_encolumna(ganador)
        print('')
        mostrar_matriz(empates)
    else:
        imprimir_lista_encolumna(matriz[0])
        print('')
        imprimir_lista_encolumna(ganador)

mostrar_ganador_y_empates(matriz,4,1,operator.gt)    