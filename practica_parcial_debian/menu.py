from funciones import *
import operator
I_JURADO_UNO = 1
I_JURADO_DOS = 2
I_JURADO_TRES = 3
I_PROMEDIO = 4


def ejecutar_menu():
    bandera = 0
    while(True):
        print("BAILANDO POR UN VINO\n1.Calificar bailarines\n2.Mostrar notas\n3.Ordenar bailarines jurado 2\n4.Triple siete\n5.Jurado malo\n6.TOP 3\n7.Verificar ganador\n8.Salir")
        
        opcion = pedir_numero("Su opcion: ","Opcion invalida ingrese números entre 1-5\nSu opcion:",1,8)
        
        if opcion == 1:
            bailando = inicializar_matriz(4,5,0)
            #cargar_bailando_ok(bailando)
            bailando =[['bailarin 1',1,6,3,7],
           ['bailarin 2',4,8,1,4],
           ['bailarin 3',5,9,8,7],
           ['bailarin 4',10,6,8,7]]      
        elif opcion == 2:
            
            imprimir_matriz_con_encabezado(bailando)
            
            
            
        elif opcion == 3:
            jurado_dos = ordenar_por_numero(bailando,operator.lt,I_JURADO_DOS)
            imprimir_matriz_con_encabezado(jurado_dos)
            
           
            
        elif opcion == 4:
            encontrar_numero(bailando,7,I_PROMEDIO)
        elif opcion == 5:
            jurado_malo = encontrar_aplazados(bailando,4,I_JURADO_TRES)
            imprimir_matriz_con_encabezado(jurado_malo)
        elif opcion == 6:
            top_tres_promedio = ordenar_por_numero(bailando,operator.lt,I_PROMEDIO)
            imprimir_por_filas(top_tres_promedio,3)
            
        elif opcion == 7:
            mostrar_ganador_y_empates(bailando,I_PROMEDIO,I_JURADO_UNO,operator.gt)
          
        elif opcion == 8:
            print("Saliendo...")
            break
        limpiar_consola()
    
ejecutar_menu()           