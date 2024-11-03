import random
import os

#Constantes -> para fecilitar el uso de eso números.

PIEDRA = 1
PAPEL = 2
TIJERA = 3

MAYOR = 1
MENOR = 2

def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('cls')

#PEDIR DATOS
def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    '''Se encarga de pedir un numero entero y lo
    valida entre un rango. Retorna un numero'''
    numero = int(input(mensaje))
    while numero > maximo or numero < minimo:
        numero = int(input(mensaje_error))
    return numero

#pedir_numero('su numero' , 'su ERROR' , 1 , 5)
#RANKINGS
def calcular_maximo(numero_uno:int,numero_dos:int) -> int:
    '''Calcula el mayor entre dos numeros
    recibe dos enteros y retorna el mayor'''
    if numero_uno > numero_dos:
        mayor = numero_uno
    else:
        mayor = numero_dos
    return mayor
#print(calcular_maximo(100 , 50))    

def calcular_porcentaje(cantidad_victorias:int,cantidad_partidas:int)->float:
    '''Calcula el porcentaje de victorias recibe la cantidad de victorias lo
     multiplica por 100 y lo divide por la cantidad de partidas, devuelve un entero '''
    porcentaje = (cantidad_victorias * 100) / cantidad_partidas
    return porcentaje

#print(calcular_porcentaje(1 , 10))

#JUEGOS EN GENERAL
def generar_respuesta_maquina(minimo:int,maximo:int) -> int:
    '''Genera un entero aleatorio entre un rango y lo
    devuelve '''
    respuesta_maquina = random.randint(minimo , maximo)
    return respuesta_maquina

#print(generar_respuesta_maquina(1 , 5))

#PIEDRA PAPEL O TIJERA
def verificar_ganador_ronda(respuesta_jugador:int,respuesta_maquina:int) -> str:
    '''Resuelve el ganador piedra papel tijera, recibe dos enteros
    y los compara. Devuelve un strig declarando el ganador '''
    if(respuesta_jugador == PIEDRA and respuesta_maquina == TIJERA) or (respuesta_jugador == PAPEL and respuesta_maquina == PIEDRA) or (respuesta_jugador == TIJERA and respuesta_maquina == PAPEL):
        ganador = 'Ganaste una batalla, pero no la Guerra'
    else:
        if(respuesta_maquina == PIEDRA and respuesta_jugador == TIJERA) or (respuesta_maquina == PAPEL and respuesta_jugador == PIEDRA) or (respuesta_maquina == TIJERA and respuesta_jugador == PAPEL):
            ganador = 'Esta gano yo, humano miserable'
        else:
            ganador = 'Es que no use toda mi fuerza '

    return ganador
#print(verificar_ganador_ronda(PIEDRA , PIEDRA))            

def verificar_ganador_partida(aciertos_jugador:int,aciertos_maquina:int) -> str:
    '''compara dos enteros y devuelve un str del mayor '''
    if aciertos_jugador > aciertos_maquina:
        ganador_partida = 'Ganas tú esta vez'
    else:
        ganador_partida = 'Gano yo jajaja'
    return ganador_partida
#print(verificar_ganador_partida(3, 3))        


def verificar_estado_partida(aciertos_jugador:int,aciertos_maquina:int,ronda_actual:int) -> bool:
    '''esta funcion se usa como condicional para el bucle while del jueguito piedra papel o tijera
    esta inicializada en True y dara False si se cumple la condicion de 2 aciertos de algunos de
    los contendientes o la cantidad de aciertos de alguno de los
     dos sea mayor en la ronda 3 o posterior'''
    estado_partida = True

    if aciertos_jugador == 2 or aciertos_maquina == 2:
        estado_partida = False
    else:
        if ronda_actual > 2:
            if aciertos_jugador > aciertos_maquina or aciertos_maquina > aciertos_jugador:
                estado_partida = False
    return estado_partida

#print(verificar_estado_partida(0 , 0, 6))                


def obtener_elemento(respuesta:int) -> str:
    '''Relaciona un entero con un str especifico
la usamos para asignar el nombre piedra al 1, papel al 2...etc'''
    if respuesta == 1:
        mensaje = 'PIEDRA'
    else:
        if respuesta == 2:
            mensaje = 'PAPEL'
        else:
            mensaje = 'TIJERA' 
    return mensaje
#print(obtener_elemento(1))               

def jugar_piedra_papel_tijera() -> str:
    aciertos_jugador = 0
    aciertos_maquina = 0
    contador_rondas = 0
    
    print("Bienvenido a la partida de Piedra Papel o Tijera")

    while verificar_estado_partida(aciertos_jugador,aciertos_maquina,contador_rondas):
        contador_rondas +=1
        print(f"Ronda: {contador_rondas}")
        
        #Pista: Debo pedirle al jugador que elija el elemento
        numero_jugador = pedir_numero('Ingrese Opcion 1-Piedra--2-Papel--3-Tijeras: ' , 'ERROR Ingrese Opcion 1-Piedra--2-Papel--3-Tijeras: ' , 1 , 3)
        numero_maquina = generar_respuesta_maquina(1 , 3)

        ganador_ronda = verificar_ganador_ronda(numero_jugador , numero_maquina)
        print(f'Yo elijo {obtener_elemento(numero_maquina)} contra tu {obtener_elemento(numero_jugador)}  {ganador_ronda}')
        
        #Pista: Debo elegir el elemento de la maquina
        #Pista: Debo saber quien gano la ronda (deberia mostrarlo tambien)
        if ganador_ronda == 'Ganaste una batalla, pero no la Guerra':
            aciertos_jugador += 1
        else:
            if ganador_ronda == 'Esta gano yo, humano miserable':
                aciertos_maquina += 1

     


        #NO BORRAR
        limpiar_consola()
    
    ganador_partida = verificar_ganador_partida(aciertos_jugador , aciertos_maquina)

        
        
    #Pista: Debo saber quien gano la partida
    #ganador = "???????"
            
    return ganador_partida

#print(jugar_piedra_papel_tijera())
        
        
#ADIVINA EL NUMERO

def mostrar_mensaje_final(puntaje_final:int)->None:
    '''Recibe un entero y le asigna un str como mensaje
    Nos sirve para asignarle un mensaje enpecifico a la 
    cantidad de aciertos'''
    if puntaje_final > 5:
        mensaje = 'WOW, Usted es psiquic'
    else:
        if puntaje_final >= 4:
            mensaje = 'Excelente eres muy bueno adivinando'
        else:
            if puntaje_final <= 3 and puntaje_final >= 1:
                mensaje = 'Buen trabajo adivinando'
            else:
                mensaje =  'Se ve que no eres bueno adivinando, más suerte la próxima'   
    return mensaje

#print(mostrar_mensaje_final(0))    
     

def jugar_adivina_numero() -> int:
    contador_intentos = 3
    puntaje_final = 0
    bandera_numero_maquina = 0
    while(contador_intentos != 0):
        contador_intentos -= 1
        numero_adivinado = pedir_numero('Adivine que numero eleji entre 1 al 9: ' , 'ERROR solo del 1 al 9 amigo' , 1 , 9)
        if bandera_numero_maquina == 0:
            numero_a_adivinar = generar_respuesta_maquina(1 , 9)
            bandera_numero_maquina = 1
        if numero_adivinado == numero_a_adivinar:
            puntaje_final += 1
            contador_intentos += 1
            print(f'Le pegaste habia elejido el {numero_a_adivinar}')
            bandera_numero_maquina = 0
        else:
            print(f'Ño Ño ño le pifiaste lejos')
        #Pista debo reutilizar funciones anteriores que use en el de piedra papel tijera no hacer todo de cero.
       
        print(f"Intentos restantes: {contador_intentos}")
        #NO BORRAR
        limpiar_consola()

    print(mostrar_mensaje_final(puntaje_final))    
    
    return puntaje_final

#print(jugar_adivina_numero())

#MAYOR MENOR

def verificar_cartas(carta:int, carta_posterior:int,eleccion_jugador:int) -> str:
    '''Compara tres enteros y devuelve un str con un mensaje especifico '''
    if (carta_posterior > carta and eleccion_jugador == 1) or (carta_posterior < carta and eleccion_jugador == 2):
        mensaje = 'Ganaste'
    else:
        if carta_posterior == carta:
            mensaje = 'Empate'
        else:
            mensaje = 'Perdiste'    
    return mensaje
#print(verificar_cartas(5 , 1 , 1))



    
def jugar_mayor_menor():
    puntuaje_final = 0
    bandera_numero_base = 0 
    numero_base = generar_respuesta_maquina(1 , 12)
    #Pista : Debo generar primero la carta random antes de jugar
    while(True):
        if bandera_numero_base == 1:
            numero_base = generar_respuesta_maquina(1 , 12)
        numero_jugador = pedir_numero(f'Elija 1 para mayor o 2 para menor del numero que {numero_base}: ' , 'ERROR solo 1 o 2 podes elejir: ' , 1 , 2)
        numero_siguiente = generar_respuesta_maquina(1 , 12)
        bandera_numero_base = 1
        quien_gana = verificar_cartas(numero_base , numero_siguiente , numero_jugador)
        print(f'Salio {numero_siguiente}')
        if quien_gana == 'Ganaste':
            puntuaje_final += 1
            print('Sumaste 1 punto')
        else:
            if quien_gana == 'Perdiste':
                print('Fuiste, amigo')
                break
        #Pista : Cuando pierdo debo salir del while

        #NO BORRAR
        limpiar_consola()
    
    return puntuaje_final
#print(jugar_mayor_menor())    