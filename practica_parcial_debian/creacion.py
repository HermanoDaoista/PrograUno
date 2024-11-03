#una matrix de 4 x 10, 10 participantes (filas) 3 jurados + 1 bailarines (4 columnas)

#carga secuancial de notas inicio matriz con funcion, carga recorriendo con for
from funciones import *



def cargar_bailando_ok(matriz:list[list])->list[list]:
    
    I_BAILARIN = 0
    I_JURADO_UNO = 1
    I_JURADO_DOS = 2
    I_JURADO_TRES = 3
    I_PROMEDIO = 4
    numero_bailarin = 0
    
    
    for fil in range(len(matriz)):
        numero_bailarin +=1
        jurado_uno =  pedir_numero(f'Ingrese nota jurado_uno para el bailarin numero {numero_bailarin}: ', 'Error solo del 1 al 10', 1,10)
        jurado_dos =  pedir_numero(f'Ingrese nota jurado_dos para el bailarin numero {numero_bailarin}: ', 'Error solo del 1 al 10', 1,10)
        jurado_tres =  pedir_numero(f'Ingrese nota jurado_tres para el bailarin numero {numero_bailarin}: ', 'Error solo del 1 al 10', 1,10)
        nota_promedio = calcular_promedio_bailarines(jurado_uno,jurado_dos,jurado_tres) 
       
        
      
        
        matriz[fil][I_BAILARIN] = f'Bailarin {numero_bailarin}'
        matriz[fil][I_JURADO_UNO] = jurado_uno
        matriz[fil][I_JURADO_DOS] = jurado_dos
        matriz[fil][I_JURADO_TRES] = jurado_tres
        matriz[fil][I_PROMEDIO] = nota_promedio
        
    
    return matriz    

bailando = inicializar_matriz(3,5,0)
cargar_bailando(bailando)


def imprimir_matriz_con_encabezado(matriz:list[list])->None:
    print(f"{'Bailarin':<15}{'Jurado_uno':<15}{'Jurado_dos':<15}{'Jurados_tres':<15}{'nota_promedio':<15}")
    for fila in bailando:
        print(f'{fila[0]:<15}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}')
        

bailando =[['bailarin 1',9,6,3,3],
           ['bailarin 2',4,8,1,4],
           ['bailarin 3',5,5,6,6],
           ['bailarin 4',6,6,8,6]]      