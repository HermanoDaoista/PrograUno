def inicializar_matriz(filas : int , columnas : int , valor_inicial : any) -> list:
    matriz = []

    for _ in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]

    return matriz

def cargar_bailando(matriz:list[list])->list[list]:
    matriz[0] = ['Bailarin', 'Jurado 1', 'Jurado 2', 'Jurado 3', 'promedio']
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

def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    '''Se encarga de pedir un numero entero y lo
    valida entre un rango. Retorna un numero'''
    numero = int(input(mensaje))
    while numero > maximo or numero < minimo:
        numero = int(input(mensaje_error))
    return numero

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:15}', end= ' ')
        print('')  


def imprimir_encabezado(lista:list)->list:
    for i in range(len(lista)):
        print(lista[i], end= '')


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

def encontar_gran_coincidencia(matriz:list[list], numero:int, columna:int)-> str:
    bandera = 0
    for i in range(len(matriz) - 1):
        for j in range(i+1,len(matriz)):
            if matriz[i][columna] == numero:
                bandera = 1
                print(matriz[i])
    if bandera == 0:
        print('No se encontro')  

def encontrar_aplazados(matriz:list[list], numero:int, columna:int)->list:
    auxiliar = []
   
    for i in range(len(matriz)):
        if matriz[i][columna] < numero:
            auxiliar += [matriz[i]]
        
    return  auxiliar  

def imprimir_por_filas(matriz:list[list], cantidad)-> str:
    
    for i in range(len(matriz)):
        cantidad -= 1
        if cantidad == -1:
            break
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:10}' , end = ' ')
        print(' ')      
        

            
                
                      

                
               
               
               
                  
            
                    




