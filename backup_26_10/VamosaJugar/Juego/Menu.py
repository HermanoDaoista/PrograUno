from Funciones import *

def ejecutar_menu():
    cantidad_victorias_jugador = 0
    cantidad_victorias_maquina = 0
    puntaje_maximo_adivina_numero = 0
    bandera_adivina = 0
    puntaje_maximo_mayor_menor = 0
    bandera_mayor_menor = 1
    puntaje_final_adivina_numero = 0
    puntaje_final_mayor_menor = 0
    bandera_pi_pa_ti = 0
    while(True):
        print("SALA DE JUEGOS\n1.Jugar al Piedra Papel o Tijera\n2.Jugar al Adivina el Número\n3.Jugar al Mayor/Menor\n4.Mostrar Rankings\n5.Salir")
        
        opcion = pedir_numero("Su opcion: ","Opcion invalida ingrese números entre 1-5\nSu opcion:",1,5)
        
        if opcion == 1:
            ganador = jugar_piedra_papel_tijera()
            
            if ganador == 'Ganas tú esta vez':
                cantidad_victorias_jugador += 1
            else:
                if ganador == 'Gano yo jajaja':
                    cantidad_victorias_maquina += 1    
            print(ganador)
            bandera_pi_pa_ti = 1
            #Pista : Deberia notificar quien gano la partida


        elif opcion == 2:
            puntaje_final_adivina_numero = jugar_adivina_numero()
            print(puntaje_final_adivina_numero)
        elif opcion == 3:
            puntaje_final_mayor_menor = jugar_mayor_menor()
            print(f'Tu puntaje es {puntaje_final_mayor_menor}')
        elif opcion == 4:
            if bandera_adivina == 0:
               puntaje_maximo_rankings = puntaje_final_adivina_numero
               bandera_adivina = 1 
            else:
                if puntaje_final_adivina_numero > puntaje_maximo_rankings:
                    puntaje_maximo_rankings = puntaje_final_adivina_numero   
            
            if bandera_pi_pa_ti == 1:
                rankings_jugador = calcular_porcentaje(cantidad_victorias_jugador , (cantidad_victorias_jugador + cantidad_victorias_maquina))
                rankings_maquina = calcular_porcentaje(cantidad_victorias_maquina , (cantidad_victorias_jugador + cantidad_victorias_maquina))
                print(f'El jugador lleva un {rankings_jugador} % de victoria y la maquina un {rankings_maquina} % de victorias')
            
            print(f'El puntake mas alto de adivina numero es {puntaje_maximo_adivina_numero}')
                

            
            #Pista : Tener en cuenta las variables creadas en la lineas 5 a 10 y lo que el documento dice.
        
        elif opcion == 5:
            print("Saliendo...")
            break
        limpiar_consola()
    
ejecutar_menu()
