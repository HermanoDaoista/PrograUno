import os
import random

def inicializar_matriz(filas : int , columnas : int , valor_inicial : any) -> list:
    matriz = []

    for _ in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]

    return matriz

def mostrar_matriz(matriz : list[list]) -> str:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:10}' , end = ' ')
        print(' ')        
    
     

def verificar_si_es_matriz(matriz : list[list])-> bool | list: 
    retorno = False
    if type(matriz) == list:
        for fila in matriz:
            if type(fila) == list:
                retorno = True
           
    return retorno


    
def verificar_dimencion_de_la_matriz(matriz_a : list[list], matriz_b : list[list])-> bool | list:
    if len(matriz_a) == len(matriz_b):
        for i in range(len(matriz_a)):    
                if len(matriz_a[i]) == len(matriz_b[i]):
                    retorno = True
                else:
                    retorno = []
            
    else:
        retorno = []
    return retorno

   
def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('clear')


def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    '''Se encarga de pedir un numero entero y lo
    valida entre un rango. Retorna un numero'''
    numero = int(input(mensaje))
    while numero > maximo or numero < minimo:
        numero = int(input(mensaje_error))
    return numero

def pedir_str(mensaje : str, mensaje_error : str , minimo):
    cadena = str(input(mensaje))
    while len(cadena) < minimo:
        cadena = str(input(mensaje_error))
    return cadena

def validad_genero(mensaje:str , mensaje_error:str , genero_a :str , genero_b: str , genero_c: str ):
    genero = input(mensaje)
    while genero != genero_a and genero != genero_b and genero != genero_c:
        genero = input(mensaje_error)
    return genero

def generar_notas(minimo:int,maximo:int) -> int:
    '''Genera un entero aleatorio entre un rango y lo
    devuelve '''
    notas = random.randint(minimo , maximo)
    return notas
def cargar_estudiantes(matriz:list[list])->list[list]:
    I_NOMBRE = 0
    I_APELLIDO = 1
    I_DNI = 2
    I_GENERO = 3
    I_NOTAS = 4
    for fil in range(len(matriz)):
        nombre = pedir_str('Ingrese nombre: ' , 'Error al menos tres caracteres: ', 3)
        apellido = pedir_str('Ingrese Apellido: ' , 'Error al menos tres caracteres: ', 3)
        dni =  pedir_numero('Ingrese su DNI: ', 'Error DNI fuera de rango: ', 99999 , 99999999)
        genero = validad_genero('Ingrese genero: ' , 'Error debe escojer uno: ' , 'M','F','NB')
        nota = generar_notas(5,10) 
        matriz[fil][I_NOMBRE] = nombre
        matriz[fil][I_APELLIDO] = apellido
        matriz[fil][I_DNI] = dni
        matriz[fil][I_GENERO] = genero
        matriz[fil][I_NOTAS] = nota
    return matriz
   
def anidar_lista_por_mayor_que(matriz:list, mayor:int ,columna:int)->list[list]:
    lista_mayor = []
    for fil in range(len(matriz)):
        if matriz[fil][columna] > mayor:
         lista_mayor[len(matriz) :] = [matriz[fil]]

    return lista_mayor   


def mostrar_lista(lista : list[list]) -> str:
    for i in range(len(lista)):
            print(f'{lista[i]:6}' , end='')

def anidar_lista_por_rango(matriz:list[list],minimo:int,maximo:int, columna:int)-> list:
    lista = [] 
    for fil in range(len(matriz)):
        if matriz[fil][columna] > minimo and matriz[fil][columna] < maximo:
            lista[len(lista) :] = [matriz[fil]]
        
    return lista            
        
def anidar_lista_por_menor_que(matriz:list, menor:int ,columna:int)->list[list]:
    lista_menor = []
    for fil in range(len(matriz)):
        if matriz[fil][columna] < menor:
         lista_menor[len(matriz) :] = [matriz[fil]]

    return lista_menor 
def encontrar_numero(matriz:list,numero:int,columna:int)->list[list]:
    buscado = []
    for fil in range(len(matriz)):
        if numero == matriz[fil][columna]:
            buscado = matriz[fil]
            break
    return buscado   

def imprimir_resultado(matriz:list[list],mensaje:str) -> None:
    if verificar_si_es_matriz(matriz) == True:
        mostrar_matriz(matriz)
    else:
        if type(matriz) == list and len(matriz) > 0:
            mostrar_lista(matriz)
        else:
            print(mensaje) 

def promediar_columna(matriz:list,columna:int) -> float:
    notas_sumana = 0
    promedio = 0
    for fila in range(len(matriz)):
        notas_sumana = notas_sumana + matriz[fila][columna]
    if len(matriz) != 0:
        promedio = notas_sumana / len(matriz)

    return promedio 

def promediar_segun_genero(matriz:list[list] , columna_uno:int, columna_dos:int,genero)->float:
    contador_genero = 0
    suma_genero = 0
    for fil in range(len(matriz)):
        if matriz[fil][columna_uno] == genero:
            contador_genero += 1
            suma_genero = suma_genero + matriz[fil][columna_dos]
            promedio = suma_genero / contador_genero
    return promedio

def promediar_los_generos(matriz:list[list], genero:str,columna:int)->int:
    contador_genero = 0
    porcentaje = 0
    for fil in range(len(matriz)):
        if matriz[fil][columna] == genero:
            contador_genero += 1
        if contador_genero > 0:
            porcentaje = (contador_genero * 100)/len(matriz) 

    return porcentaje

def encontrar_alumnos_mejor_nota(matriz:int , columna:int)-> list:
    mayor = matriz[0][columna]
    for fil in range(len(matriz)):
        if matriz[fil][columna] > mayor:
            mayor = matriz[fil][columna]
    lista_mejor_nota = []
    for fil in range(len(matriz)):
        if mayor == matriz[fil][columna]:
            lista_mejor_nota[len(matriz) :] = [matriz[fil]]

    return lista_mejor_nota

def encontrar_alumnos_promedio(matriz:list[list],columna:int,promedio:float)->list:
    lista_promedio = []
    for fil in range(len(matriz)):
        if matriz[fil][columna] > promedio:
            lista_promedio[len(matriz) :] = [matriz[fil]]
    return lista_promedio



              
