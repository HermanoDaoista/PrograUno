# Ejercitación Clase 13 
# (Cadenas de Caracteres Algorítmicamente)

# 1. Realizar una función llamada es_alfabetico() que recibe una cadena y verifica si la misma tiene sólo caracteres alfabéticos (a-z/A-Z) -> No hace falta tener en cuenta los acentos y algún otro carácter

# Tener en cuenta los caracteres ASCII imprimibles que sólo sean letras

def es_alfabetico(cadena:list)->bool:
    
    retorno = True
    for caracter in cadena:
        if (ord(caracter) < 65 or ord(caracter) > 90) and ord(caracter) < 97 or ord(caracter) > 122:
            retorno = False
    return retorno       

                 

#2. Realizar una función llamada es_entero() que recibe una cadena y verifica si la misma tiene sólo caracteres numéricos (0-9) 

  
def es_entero(cadena:list)->bool:
    retorno = True
    for letra in cadena:
        if ord(letra) > 57 or ord(letra) < 48:
            retorno = False
            break
    return retorno
# 3. Realizar una función llamada es_alfanumerico() que recibe una cadena y verifica si la misma tiene sólo caracteres alfanuméricos (a-z/A-Z/0-9) 

# Tener en cuenta los caracteres ASCII imprimibles que sólo sean números enteros y caracteres alfabéticos.

def es_alfanumerico(cadena:list)->bool:
    retorno = True
    for caracter in cadena:
        if (ord(caracter) > 57 or ord(caracter) < 48) and (ord(caracter) > 123 or ord(caracter) < 65):
            retorno = False
    return retorno       

# 4. Realizar la función es_mayuscula() que me verifica que la cadena que le pase como parámetro está en mayúscula o no.
# Devuelve True si esa cadena está en mayúscula.
# Devuelve False en caso contrario

def es_mayuscula(cadena:list)->bool:
    retorno = True
    for caracter in cadena:
        if ord(caracter) > 90:
            retorno = False
    return retorno

   
# 5. Realizar la función es_minuscula() que me verifica que la cadena que le pase como parámetro está en minúscula o no.
# Devuelve True si esa cadena está en minúscula.
# Devuelve False en caso contrario

def es_minuscula(cadena:list)->bool:
    retorno = True
    for caracter in cadena:
        if ord(caracter) < 97:
            retorno = False
    return retorno

# 6. Realizar una función que me permita convertir un carácter de mi cadena a mayúscula, se le pasa como parámetro un str con un sólo carácter (validar que esto ocurra) y devuelve dicho carácter en mayúscula. 
# En caso de que el carácter no sea alfabético o ya se encuentre en mayúscula, devuelve ese mismo carácter sin cambios, en caso de que haya recibido un str con más de un carácter la función devuelve None.

def convertir_a_mayuscula(mensaje:str,mensaje_error:str)->str:
    
    letra = input(mensaje)
    while len(letra) > 1:
        letra = input(mensaje_error)
    if ord(letra) > 96 and ord(letra) < 123:
        letra = chr(ord(letra) - 32)
        
    return letra
#print(convertir_a_mayuscula('ingrese caracter: ' , 'error solo uno: '))

# 7. Realizar una función que me permita convertir un carácter de mi cadena a minúscula, se le pasa como parámetro un str con un sólo carácter (validar que esto ocurra) y devuelve dicho carácter en minúscula. 
# En caso de que el carácter no sea alfabético o ya se encuentre en mayúscula, devuelve ese mismo carácter sin cambios, en caso de que haya recibido un str con más de un carácter la función devuelve None.

def convertir_a_minuscula(mensaje:str,mensaje_error:str)->str:
    
    letra = input(mensaje)
    while len(letra) > 1:
        letra = input(mensaje_error)
    if ord(letra) > 64 and ord(letra) < 91:
        letra = chr(ord(letra) + 32)
        
    return letra

# 8.Realizar una función que me permita convertir toda mi cadena a mayúscula, se le pasa una cadena y devuelve la misma convirtiendo cada carácter alfabético en minúscula a mayúscula.
# Los otros caracteres que no sean alfabéticos simplemente los deja como está.

def convertir_cadena_a_mayusculas(cadena:list):
    cadena_mayuscula = ''
    for caracter in cadena:
        if  ord(caracter) > 96 and ord(caracter) < 123:
            caracter = chr(ord(caracter) - 32) 
            cadena_mayuscula += caracter
            continue
        cadena_mayuscula += caracter
    return cadena_mayuscula  

#print(convertir_cadena_a_mayusculas('pitFdfdggdll'))   
# 
# 9.Realizar una función que me permita convertir toda mi cadena a minúscula, se le pasa una cadena y devuelve la misma convirtiendo cada carácter alfabético en mayúscula a minúscula.
# Los otros caracteres que no sean alfabéticos simplemente los deja como está.
def convertir_cadena_a_minusculas(cadena:list):
    cadena_minuscula = ''
    for caracter in cadena:
        if  ord(caracter) > 64 and ord(caracter) < 91:
            caracter = chr(ord(caracter) + 32) 
            cadena_minuscula += caracter
            continue
        cadena_minuscula += caracter
    return cadena_minuscula  

#10.Crear una función llamada capitalizar_texto(), en la que recibe una cadena y devuelve la misma con la primer letra en mayúscula y todas las demás en minúscula.
def  capitalizar_texto(cadena:list):
    cadena_formateada = ''
    bandera = 0
    for caracter in cadena:
        if bandera == 0:
            if ord(caracter) > 97 and ord(caracter) < 123:
                caracter = chr(ord(caracter) -32)
                bandera = 1
            else:                                       #<------asi si agora ne
                if ord(caracter) > 64 and ord(caracter) < 91:
                    caracter = chr(ord(caracter) + 32)
        cadena_formateada += caracter   
                
    return cadena_formateada         
                    
#print(capitalizar_texto('gfgfgfgfg'))     
            
             
def capitalizar_texto_gpt(cadena:str) ->str:
    cadena_formateada = ''
    for i in range(len(cadena)):
        caracter = cadena[i]
        if i == 0:
            if caracter >= 'a' and caracter <= 'z':
                caracter = chr(ord(caracter) - 32)
        else:
            if caracter >= 'A' and caracter <= 'Z':
                caracter = chr(ord(caracter) + 32)
        cadena_formateada += caracter 
    return cadena_formateada  
                

#print(capitalizar_texto_gpt('hdahshdahhahsdKJHHHHJHJH'))    
# 
# 11.Crear una función llamada generar_titulo(), en la que recibe una cadena y devuelve la misma con cada palabra con la primera letra mayúscula y todas las demás en minúscula

#Ejemplo: “hOla mUNdO” —>  “Hola Mundo”

def generar_titulo(cadena:str)-> str:
    cadena_titulo = ''
    for i in range(len(cadena)):
        
        if i == 0 or cadena[i -1] == ' ':
            if  ord(cadena[i]) > 96 and ord(cadena[i]) < 123:
                 cadena_titulo += chr(ord(cadena[i]) - 32) 
            else: 
                cadena_titulo += cadena[i]    
        else:
            cadena_titulo += cadena[i]    

    return cadena_titulo
                

#print(generar_titulo('selim Invencible el capo de tuti Los capos'))    

# 12.Crear una función llamada formatear_nombre_apellido() en la que recibe una cadena cualquiera y extrae sólo el nombre y apellido de la misma en el formato correcto: (Nombre Apellido)

# Ejemplo: 

# cadena = “123mAriAnO ferNanDEZ 911%@”
# cadena_resultado = formatear_nombre_apellido(cadena)
# print(cadena_resultado) —> “Mariano Fernandez”

        
def formatear_nombre_apellido(cadena:str)->str:
    cadena_nombre_apellido = ''
    
    for caracter in cadena:
        if (es_alfabetico(caracter) == True) or (caracter == ' '):
            cadena_nombre_apellido += caracter
           
    return generar_titulo(cadena_nombre_apellido)
        
# 13. Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos consecutivos.
# Ejemplo: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”. 

def suprimir_consecutivos(cadena:str)->str:
    cadena_nueva = ' '
    for i in range(len(cadena)):
        if cadena[i] != cadena[i-1]:
            cadena_nueva += cadena[i]
    return capitalizar_texto(cadena_nueva)
    
       
           
# 14. Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma. 
# Ejemplo: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.

def suprimir_vocales(cadena:str)->str:
    cadena_nueva = ''
    for i in range(len(cadena)):
        if cadena[i] != 'a' and cadena[i] != 'e' and cadena[i] != 'i' and cadena[i] != 'o' and cadena[i] != 'u':
            cadena_nueva += cadena[i]
    return cadena_nueva

       

def suprimir_vocales_op(cadena:str)->str:
    cadena_nueva = ''
    vocales = ('a','e','i','o','u')
    for i in range(len(cadena)):
        if cadena[i] not in vocales:
            cadena_nueva += cadena[i]
    return cadena_nueva
        

#print(suprimir_vocales_op('pitfall'))  


# 15.Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena. 
# Ejemplo: Si recibe la cadena “El origen del gen” y la subcadena “gen” deberá retornar el valor 2.

def buscar_subcadena(cadena, subcadena):
    longitud_cadena = len(cadena)
    longitud_subcadena = len(subcadena)
    contador = 0

    for i in range(longitud_cadena - longitud_subcadena + 1):
        if cadena[i:i + longitud_subcadena] == subcadena:
            contador += 1
             

    return contador
#todavia no entiendo bien el algoritmo este pero prefiero pasar al siguiente ejercicio

#print(buscar_subcadena('el origen del gen por genes encongen', 'gen'))

            
            


    



           
                    
                


