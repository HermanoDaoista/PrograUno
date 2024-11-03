
import random
import os

def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('cls')

def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    """pide un numero y lo valida entre un rango

    Args:
        mensaje (str): mensaje para el input
        mensaje_error (str): mensaje de error para el input
        minimo (int): minimo que se puede introducir
        maximo (int): maximo que se puede introducir

    Returns:
        int: devuelve un entero validado
    """
    numero = int(input(mensaje))
    while numero > maximo or numero < minimo:
        numero = int(input(mensaje_error))
    return numero

def inicializar_matriz(filas : int , columnas : int , valor_inicial : any) -> list:
    """inicializa una matriz segun el numero de columnas y filas

    Args:
        filas (int): entero que representa la cantidad de filas
        columnas (int): entero que representa la cantidad de columnas
        valor_inicial (any): numero con que se inicaliza todos los valores de la matriz 

    Returns:
        list: devuelve una lista anidada
    """
    matriz = []
    for _ in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]

    return matriz

def cargar_bailando(matriz:list[list])->list[list]:
    matriz[0] = ['Bailarin Nro', 'Jurado 1', 'Jurado 2', 'Jurado 3', 'promedio']
    I_BAILARIN = 0
    I_JURADO_UNO = 1
    I_JURADO_DOS = 2
    I_JURADO_TRES = 3
    I_PROMEDIO = 4
    numero_bailarin = 0
    
    
    for fil in range(1, len(matriz)):
        numero_bailarin +=1
        jurado_uno =  pedir_numero('Ingrese nota: ', 'Error ingrese un numero del 1 al 10: ', 1 , 10)
        jurado_dos =  pedir_numero('Ingrese nota: ', 'Error ingrese un numero del 1 al 10: ', 1 , 10)
        jurado_tres =  pedir_numero('Ingrese nota: ', 'Error ingrese un numero del 1 al 10: ', 1 , 10)
        
        suma = jurado_uno + jurado_dos + jurado_tres
        nota_promedio = suma / 3
        
        matriz[fil][I_BAILARIN] = f'Bailarin {numero_bailarin}'
        matriz[fil][I_JURADO_UNO] = jurado_uno
        matriz[fil][I_JURADO_DOS] = jurado_dos
        matriz[fil][I_JURADO_TRES] = jurado_tres
        matriz[fil][I_PROMEDIO] = round(nota_promedio,2)
        
    
    return matriz

            
def mostrar_matriz(matriz:list[list]):
    """imprime una matriz

    Args:
        matriz (list[list]): recibe una lista anidada
    """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:<15}', end= ' ')
        print('')  

def imprimir_matriz_encolumnada(matriz: list[list]) -> None:
    for fila in matriz:
        print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<15}")


def ordenar_por_numero(matriz: list[list], operador, fila: int)-> list[list]:
    """ordena una matriz alfabeticamente, tambien funciona con enteros

    Args:
        matriz (list[list]): _recibe una matriz_
        operador (_type_): _recibe parametro de la funcion operator_
        fila (int): _un entero que representa la columna de la matriz que vamos a ordenar_

    Returns:
        _type_: _ddevuelve una lista anidada excluyendo la fila[0]
    """
    for i in range(1,len(matriz) - 1):
        for j in range(i+1,len(matriz)):
            if operador(matriz[i][fila], matriz[j][fila]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
        
    return matriz


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
    for i in range(1,len(matriz)):
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
    """recorre por filas una matriz y compara la columna indicada
    por menor 

    Args:
        matriz (list[list]): lista de listas
        numero (int): entero a comparar menor que 'numero'
        columna (int): la columna en la que vamos a comparar

    Returns:
        list: una lista o matriz con los menores encontrados
    """
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


def ordenar_doble_criterio(matriz:list[list],columna_uno:int,columna_dos:int,operador)->list[list]:
    """ordena una matriz por doble criterio

    Args:
        matriz (list[list]): recibe una matriz
        columna_uno (int): primer criterio a comparar
        columna_dos (int): segundo criterio a comparar
        operador (function): la funcion operator que deseamos usar

    Returns:
        list[list]: devulve una matriz ordenada
    """
    for i in range(1,len(matriz) - 1):
        for j in range(i+1,(len(matriz))):
            if operador(matriz[i][columna_uno], matriz[j][columna_uno]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar     
            elif matriz[i][columna_uno] == matriz[j][columna_uno]:
                if operador(matriz[i][columna_dos], matriz[j][columna_dos]) or (matriz[i][columna_dos] == matriz[j][columna_dos]):
                            auxiliar = matriz[i]
                            matriz[i]= matriz[j]
                            matriz[j] = auxiliar   
            
    return matriz  

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
    for i in range(1,len(matriz)-1):
        for j in range(i+1, len(matriz)):
            if matriz[i][columna_uno] == matriz[j][columna_uno] and matriz[i][columna_dos] == matriz[j][columna_dos]:
                matriz_de_iguales += [matriz[i]]
                matriz_de_iguales += [matriz[j]]
    return matriz_de_iguales                
                    
def mostrar_matriz(matriz:list[list]):
    """imprime una matriz

    Args:
        matriz (list[list]): recibe una lista anidada
    """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:<15}', end= ' ')
        print('')  

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
        print('')
                  
def verificar_si_es_matriz(matriz : list[list])-> bool | list: 
    """verifica si es o no matriz 

    Args:
        matriz (list[list]): matriz

    Returns:
        bool | list: devuelve verdadero o falso
    """
    retorno = False
    if type(matriz) == list:
        for fila in matriz:
            if type(fila) == list:
                retorno = True
           
    return retorno
            
            

    
def imprimir_resultado(matriz:list[list],mensaje:str) -> None:
    """verifica si es matriz o lista y las imprime,imprime mensaje sino

    Args:
        matriz (list[list]): una lista o una matriz 
        mensaje (str): mensaje que queremos dejar en caso de no ser lista o matriz
    """
    if verificar_si_es_matriz(matriz) == True:
        mostrar_matriz(matriz)
    else:
        if type(matriz) == list and len(matriz) > 0:
            imprimir_lista_encolumna(matriz)
        else:
            print(mensaje) 
    
def validad_genero(mensaje:str , mensaje_error:str , genero_a :str , genero_b: str , genero_c: str )->str:
    """valida si ingresamos una de las tres letras que designamos

    Args:
        mensaje (str): _'ingrese x cosa'
        mensaje_error (str): error ingrese x cosa
        genero_a (str): un str
        genero_b (str): un str
        genero_c (str): un str 

    Returns:
        str: un str
    """
    genero = input(mensaje)
    while genero != genero_a and genero != genero_b and genero != genero_c:
        genero = input(mensaje_error)
    return genero