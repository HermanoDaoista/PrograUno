
from funciones import *
import operator

def ejecutar_menu():
    bandera = 0
    while(True):
        print("BAILANDO POR UN VINO\n1.Calificar bailarines\n2.Mostrar notas\n3.Ordenar bailarines jurado 2\n4.Triple siete\n5.Jurado malo\n6.TOP 3\n7.Verificar ganador\n8.Salir")
        
        opcion = pedir_numero("Su opcion: ","Opcion invalida ingrese números entre 1-5\nSu opcion:",1,8)
        
        if opcion == 1:
            #bailando = inicializar_matriz(6,5,0)
            #cargar_bailando(bailando)
            bailando = [['Bailarin Nro' ,'Jurado 1 ' ,'Jurado 2 ' ,'Jurado 3 ' , 'promedio'],        
                    ['Bailarin 1' ,   8     ,          3        ,       4     ,          8.0],
                    ['Bailarin 2' ,   3      ,         3         ,      4         ,      3.33],
                    ['Bailarin 3'  ,   9       ,        7         ,      7        ,       8.0],
                    ['Bailarin 4'  ,   5       ,        4          ,     3         ,      4.0],
                    ['Bailarin 5'  ,   8         ,      5         ,      6        ,       8.0]]
            bandera =1
            
        elif opcion == 2:
            
            mostrar_matriz(bailando)
            
            
        elif opcion == 3:
            jurado_dos = ordenar_por_numero(bailando,operator.lt,2)
            mostrar_matriz(jurado_dos)
            
        elif opcion == 4:
            encontrar_numero(bailando,7,4)
        elif opcion == 5:
            aplazados = encontrar_aplazados(bailando,4,3)
            mostrar_matriz(aplazados)
        elif opcion == 6:
            bailarines_top = ordenar_por_numero(bailando,operator.lt,4)
            imprimir_por_filas(bailarines_top,4)
        elif opcion == 7:
            mostrar_ganador_y_empates(bailando,4,1,operator.gt)
        elif opcion == 8:
            print("Saliendo...")
            break
        limpiar_consola()
    
ejecutar_menu()           
            
             
            
            
          
            
            

