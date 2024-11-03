from Funciones import *


planilla = inicializar_matriz(2 , 5 , -1)

I_NOMBRE = 0
I_APELLIDO = 1
I_DNI = 2
I_GENERO = 3
I_NOTAS = 4
def cargar_estudiantes(matriz:list[list])->list[list]:
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
   

planilla = [['pepe', 'lapo' , 255555 , 'M' , 3],
            ['juan' , 'peronista', 555555 , 'M' , 1],
            ['luan', 'feng' , 5666633 , 'F' , 5],
            ['keshin' , 'arie' , 6665856 , 'F', 4],
            ['theleb' ,'Kaarna' , 8777787 , 'M', 5],
            ['zaratul', 'familia', 5889998,'M',4]]
#planilla = [[2,2,2,2,10]]



#mostrar_matriz(planilla)
'''mostrar alumnos promocionados-nota mayor a 6'''
def anidar_lista_por_menor_que(matriz:list, menor:int ,columna:int)->list[list]:
    lista_menor = []
    for fil in range(len(matriz)):
        if matriz[fil][columna] < menor:
         lista_menor[len(matriz) :] = [planilla[fil]]

    return lista_menor

def anidar_lista_por_mayor_que(matriz:list, mayor:int ,columna:int)->list[list]:
    lista_mayor = []
    for fil in range(len(matriz)):
        if matriz[fil][columna] > mayor:
         lista_mayor[len(matriz) :] = [matriz[fil]]

    return lista_mayor

        
        
#mostrar_matriz(lista_Promocionados)
# 4.Mostrar Alumnos Aprobados:Mostrar sólo la información de los alumnos con nota 4,5 , en caso de no haber informar que no hay
def anidar_lista_por_rango(matriz:list[list],minimo:int,maximo:int, columna:int)-> list:
    lista = [5] 
    for fil in range(len(matriz)):
        if matriz[fil][columna] > minimo and matriz[fil][columna] < maximo:
            lista[len(lista) :] = [matriz[fil]]
        
    return lista




# 5.Mostrar Alumnos Desaprobados:Mostrar sólo la información de los alumnos con nota menor a 4 , en caso de no haber informar que no hay.
# lista_desaprobados = [] 
# for fil in range(len(planilla)):
#     if planilla[fil][I_NOTAS] < 4: 
#         lista_desaprobados[len(lista_desaprobados) :] = [planilla[fil]]

# 6.Buscar Alumno por DNI:Se debe ingresar el DNI de un alumno y buscar si se encuentra o no en el sistema, mostrar su información también.
def encontrar_numero(matriz:list,numero:int,columna:int)->list[list]:
    for fil in range(len(matriz)):
        if numero == matriz[fil][columna]:
            buscado = matriz[fil]
            break
    return buscado

#7.La cantidad de alumnos promocionados, aprobados y desaprobados

# def verificar_si_es_matriz(matriz : list[list])-> bool | list: 
#     retorno = False
#     if type(matriz) == list:
#         for fila in matriz:
#             if type(fila) == list:
#                 retorno = True
           
#     return retorno

# planilla = ['pepe', 'lapo' , 255555 , ' M' , 6]
           



# def imprimir_resultado(matriz:list[list],mensaje:str) -> None:
#     if verificar_si_es_matriz(matriz) == True:
#         mostrar_matriz(matriz)
#     else:
#         if type(matriz) == list and len(matriz) > 0:
#             mostrar_lista(matriz)
#         else:
#             print(mensaje)       


#imprimir_resultado(planilla,'No se encontro')
# def promediar_columna(matriz:list,columna) -> float:
#     notas_sumana = 0
#     promedio = 0
#     for fila in range(len(matriz)):
#         notas_sumana = notas_sumana + matriz[fila][columna]
#     if len(matriz) != 0:
#         promedio = notas_sumana / len(matriz)

#     return promedio   

#print(promediar_columna(planilla , I_NOTAS)) 

# def promediar_segun_genero(matriz:list[list] , columna_uno:int, columna_dos:int,genero)->float:
#     contador_genero = 0
#     suma_genero = 0
#     for fil in range(len(matriz)):
#         if matriz[fil][columna_uno] == genero:
#             contador_genero += 1
#             suma_genero = suma_genero + matriz[fil][columna_dos]
#             promedio = suma_genero / contador_genero
#     return promedio    

#print(promediar_segun_genero(planilla,I_GENERO,I_NOTAS, 'M'))    

# def promediar_los_generos(matriz:list[list], genero:str,columna:int)->int:
#     contador_genero = 0
#     porcentaje = 0
#     for fil in range(len(matriz)):
#         if matriz[fil][columna] == genero:
#             contador_genero += 1
#         if contador_genero > 0:
#             porcentaje = (contador_genero * 100)/len(matriz) 

#     return porcentaje

#print(promediar_los_generos(planilla,'M',I_GENERO))

# def encontrar_alumnos_mejor_nota(matriz:int , columna:int)-> list:
#     mayor = matriz[0][columna]
#     for fil in range(len(matriz)):
#         if matriz[fil][columna] > mayor:
#             mayor = matriz[fil][columna]
#     lista_mejor_nota = []
#     for fil in range(len(matriz)):
#         if mayor == matriz[fil][columna]:
#             lista_mejor_nota[len(matriz) :] = [matriz[fil]]

#     return lista_mejor_nota

# def encontrar_alumnos_promedio(matriz:list[list],columna:int,promedio:float)->list:
#     lista_promedio = []
#     for fil in range(len(matriz)):
#         if matriz[fil][columna] > promedio:
#             lista_promedio[len(matriz) :] = [matriz[fil]]
#     return lista_promedio

def anidar_lista_por_rango(matriz:list[list],minimo:int,maximo:int, columna:int)-> list:
    lista = [] 
    for fil in range(len(matriz)):
        if matriz[fil][columna] > minimo and matriz[fil][columna] < maximo:
            lista[len(lista) :] = [matriz[fil]]
        
    return lista 

alumno = anidar_lista_por_rango(planilla,3,6,I_NOTAS)  
imprimir_resultado(alumno, 'No hay')         





          



 # lista_menor[len(matriz) :] = [matriz[fil]]
       
