#hacer un programa
#itera 10 veces
#matriz 10 filas , 5 columnas
#hacer un menu

from Funciones import *
I_NOMBRE = 0
I_APELLIDO = 1
I_DNI = 2
I_GENERO = 3
I_NOTAS = 4

def ejecutar_menu():
    bandera_carga = 0 
    
    while(True):
        print('SYSACAD\n1.Ingresar alumnos\n2.Mostrar alumnos\n3.Mostrar Promocionados\n4.Mostrar Aprobados\n5.Mostrar Desaprobados92\n6.buscar DNI\n7.Resultado alumnos\n8.Nota promedio total\n9.Promedio Masculinos\n10.Porcentaje por genero\n11.Alumnos Top\n12.Alumnos promedio\n13.Sañir')
        
        opcion = pedir_numero("Su opcion: ","Opcion invalida ingrese números entre 1-13\nSu opcion:",1,13)
        
        if opcion == 1:
                planilla = inicializar_matriz(2 , 5 , -1)
                cargar_estudiantes(planilla)
                bandera_carga = 1
           
        elif opcion == 2:
            if bandera_carga == 1:
                imprimir_resultado(planilla,'planilla')
        elif opcion == 3:
            if bandera_carga == 1:
                promocionados = anidar_lista_por_mayor_que(planilla,6,I_NOTAS)
                imprimir_resultado(promocionados, 'No se encontraron alumnos promocionados')       
        elif opcion == 4:
            if bandera_carga == 1:
                aprobados = anidar_lista_por_rango(planilla,3,6,I_NOTAS)
                imprimir_resultado(aprobados, 'No se encontraron aprobados')      
            
        elif opcion == 5:
            if bandera_carga == 1:
                desaprobados = anidar_lista_por_menor_que(planilla,4,I_NOTAS)
                imprimir_resultado(desaprobados , 'No se encontraron alumnos desaprobados')        
        elif opcion == 6:
            if bandera_carga == 1:
                pedir_dni = pedir_numero('Introdusca el DNI. ', 'Error Introdusca un numero valido',100000,99999999)
                busqueda = encontrar_numero(planilla,pedir_dni,I_DNI)
                imprimir_resultado(busqueda,f'El DNI {pedir_dni} no se encuentra en el sistema')
                print('')  
        elif opcion == 7:
            if bandera_carga == 1:
                promocion = (len(promocionados))
                aprobacion = (len(aprobados))
                desaprobacion = (len(desaprobados))
                print(f'Hay {promocion} alumnos promocionados')
                print(f'Hay {aprobacion} alumnos aprobados')
                print(f'Hay {desaprobacion} alumnos desaprobados')

        elif opcion == 8:
            if bandera_carga == 1:
                promedio = promediar_columna(planilla,I_NOTAS)
                print(f'El promedio de notas es {promedio}')

        elif opcion == 9:
            if bandera_carga == 1:
                promedio_masculinos = promediar_segun_genero(planilla,I_GENERO,I_NOTAS,'M')
                print(f'El promedio de notas es {promedio_masculinos}')

        elif opcion == 10:
            if bandera_carga == 1:
                alumnos_masculinos = promediar_los_generos(planilla,'M',I_GENERO,)
                print(f'Promedio de alumnos masculinos es de {alumnos_masculinos} %')
                alumnos_femeninos = promediar_los_generos(planilla,'F',I_GENERO,)
                print(f'Promedio de alumnos femeninos es de {alumnos_femeninos} %')
                alumnos_n_binarios = promediar_los_generos(planilla,'NB',I_GENERO,)
                print(f'Promedio de alumnos no binarios es de {alumnos_n_binarios} %')

        elif opcion == 11:
            if bandera_carga == 1:
                mejores_notas = encontrar_alumnos_mejor_nota(planilla,I_NOTAS)
                imprimir_resultado(mejores_notas,'')
        elif opcion == 12:
            if bandera_carga == 1:
                alumnos_promedios = encontrar_alumnos_promedio(planilla,I_NOTAS,promedio)
                imprimir_resultado(alumnos_promedios,'No hay alumnos que superen la nota promedio')
        elif opcion == 13:
            print("Saliendo...")
            break
        limpiar_consola()
                





            
            
    
ejecutar_menu()
            
                
            
                

                

            

                


            
            
            
               
               
