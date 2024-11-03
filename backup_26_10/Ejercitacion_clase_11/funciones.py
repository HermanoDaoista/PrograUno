def inicializar_matriz(filas : int , columnas : int , valor_inicial : any) -> list:
    matriz = []

    for _ in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]

    return matriz

def pedir_str(mensaje : str, mensaje_error : str , minimo):
    cadena = str(input(mensaje))
    while len(cadena) < minimo:
        cadena = str(input(mensaje_error))
    return cadena

def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    '''Se encarga de pedir un numero entero y lo
    valida entre un rango. Retorna un numero'''
    numero = int(input(mensaje))
    while numero > maximo or numero < minimo:
        numero = int(input(mensaje_error))
    return numero

def mostrar_matriz(matriz : list[list]) -> str:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:10}' , end = ' ')
        print(' ')        
    

def cargar_fulbito(matriz:list[list])->list[list]:
    I_NOMBRE = 0
    I_APELLIDO = 1
    I_PARTIDOS = 2
    I_GOLES = 3
    I_AISTENCIAS = 4
    for fil in range(len(matriz)):
        nombre = pedir_str('Ingrese nombre: ' , 'Error al menos tres caracteres: ', 3)
        apellido = pedir_str('Ingrese Apellido: ' , 'Error al menos tres caracteres: ', 3)
        partidos =  pedir_numero('Ingrese partidos: ', 'Error ingrese un numero igual o mayor a cero: ', 0 , 99999999)
        goles = pedir_numero('Ingrese cantidad de goles: ' , 'Error no se pueden recibir numeros negativos: ' , 0 , 99999999)
        asistencias = pedir_numero('Ingrese cantidad de asistencias: ' , 'Error no se pueden recibir numeros negativos: ' , 0 , 99999999)
        matriz[fil][I_NOMBRE] = nombre
        matriz[fil][I_APELLIDO] = apellido
        matriz[fil][I_PARTIDOS] = partidos
        matriz[fil][I_GOLES] = goles
        matriz[fil][I_AISTENCIAS] = asistencias
    
    return matriz

def imprimir_encabezado(lista:list)->list:
    for i in range(len(lista)):
        print(lista[i], end= '')


def imprimir_por_filas(matriz:list[list], cantidad)-> str:
    
    for i in range(len(matriz)):
        cantidad -= 1
        if cantidad == -1:
            break
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:10}' , end = ' ')
        print(' ')               



