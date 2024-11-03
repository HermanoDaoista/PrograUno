# Ejercitación Clase 14
# (Clase String)
import random
# 1. Realizar una función que reciba un string de una fecha de nacimiento en cualquiera de los dos formatos (DD-MM-AAAA) o (DD/MM/AAAA) y devuelva una lista de ENTEROS con el día mes y año convertidos a entero.
# Por ejemplo:
# Ingreso un string que diga “18-10-2024” y devuelve una lista así

# lista_enteros = [18,10,2024] -> Los str ya convertidos en int

def formatear_fecha_a_entero(cadena:str)->list:

    cadena = cadena.replace('/','-')
    partes = cadena.split('-')
    lista_enteros = [int(partes[0]),int(partes[1]),int(partes[2])]
    return lista_enteros

#print(formatear_fecha_a_entero('18/06/1982'))

# 2. Realizar una función que haga lo contrario a la función anterior, recibe una lista de enteros de 3 elementos y devuelve un str en formato fecha, también recibe el separador, pudiendo pasar ‘-’ o ‘/’.
# En caso de pasar cualquier otro separador o se le pase una lista que no tenga 3 elementos la función retorna None


def formatear_fecha_a_str(lista:list,separador:str)->str:
    # Verificar si la lista tiene exactamente 3 elementos y el separador es válido
    if len(lista) != 3 or separador not in ['-', '/']:
        return None
    
    # Convertir cada elemento de la lista a string y formatear la fecha
    dia, mes, anio = lista
    cadena = f"{dia:02d}{separador}{mes:02d}{separador}{anio}"
    return cadena

# lista_fecha = [25,9,1982]
# print(formatear_fecha_a_str(lista_fecha,'/'))


# 3.Realizar una función que reemplace todas las vocales de mi string por una letra aleatoria, devuelve una cadena resultado.
def reemplazar_vocales(cadena:str)->str:
    vocales = 'aeiouAEIOU'
    nueva_cadena = ''
    for letra in cadena:
        if letra in vocales:
            letra_aleatoria = chr(random.randint(65,122))
            nueva_cadena += letra_aleatoria
        else:
            nueva_cadena += letra    
    return nueva_cadena        

#print(reemplazar_vocales('dracula'))   
# 4.Realizar una función que me genere un número de legajo aleatorio para mi empleado, el mismo debe tener si o si 6 caracteres.
# El sistema debe generar un número aleatorio entre 1 y 125000, en caso de que el número generado sea menor a 6 caracteres rellenarlo con todos ceros a la izquierda.

def generar_legajo()->str:
    generar_numero = random.randint(1,125000)
    generar_numero_str = str(generar_numero).zfill(6)

    return generar_numero_str

#print(generar_legajo())


# 5. Crear una función que reciba una cadena de caracteres y devuelva otro string eliminando a los caracteres que se repiten más de una vez.
# Por ejemplo.
# “Mariano” -> “Mrino”
def suprimir_repetidos(cadena:str)->str:
    resultado = ''
    for letra in cadena:
        if cadena.count(letra) == 1:
            resultado += letra
    return resultado      

#print(suprimir_repetidos('hermanodaoista'))   

# 6. Crear una función que reciba una cadena de caracteres y retorne una matriz contando todas las vocales (no discriminar mayúsculas ni minúsculas)
# EJEMPLO “Mariano”



         




