# CADENAS

# 5. Realizar una función que me cuente la cantidad de vocales de mi cadena, la misma recibe una cadena y devuelve la cantidad de vocales que encontró.

def contar_vocales(cadena:str)-> int:
    contador_vocales = 0
    for i in range(len(cadena)):
        if cadena[i] == 'a' or cadena[i] == 'e' or  cadena[i] == 'i' or   cadena[i] == 'o' or  cadena[i] == 'u':
            contador_vocales += 1 
    return print(f'la cantidad de volales es {contador_vocales}')



def contar_vocales_gpt(cadena:str)->str:
    contador = 0
    for letra in cadena:
        if letra in 'aeiuoAEIOU':
            contador +=1 
    return contador

# contar = contar_vocales_gpt('parAguaya')
# print(f'hay {contar} vocales')        

# 6. Realizar una función que me cuente la cantidad de consonantes de mi cadena, la misma recibe una cadena y devuelve la cantidad de consonantes que encontró.
def contar_consonantes(cadena:str)->int:
    consonantes = 'B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z'
    consonantes_minusculas = 'b,c,d,f,g,h,k,l,m,n,p,q,r,s,t,v,w,x,y,z'
    contador = 0
    for letra in cadena:
        if letra in consonantes or  letra in consonantes_minusculas:
            contador += 1
    return contador        

#print(contar_consonantes('iNfusioNL'))

def eliminar_espacios_en_blanco(cadena:list)->str:
    cadena_sin_espacio = ''
    for caracter in cadena:
        if caracter != ' ':
            cadena_sin_espacio += caracter
    return cadena_sin_espacio

#print(eliminar_espacios_en_blanco('el mundo es mio'))
# 
# 8. Crear una función llamada repetir_cadena() que lo que va a hacer es replicar lo mismo que hace el operador * en cadenas pero separando las mismas por un espacio, se le pasa como parámetro la cadena que va a repetir, y un entero que me indique la cantidad de veces que la misma se va a repetir. 
# Devuelve como resultado una nueva cadena resultante

def repetor_cadena(cadena:list,cantidad:int)->None:
    
    if cantidad > 0:
        repetor_cadena(cadena,cantidad - 1)
        print(f'Eres un {cadena}', end=' ')
        
def repetir_cadena(cadena:str,cantidad:int)->str:
    nueva_cadena = ''
    for _ in range(cantidad):
        nueva_cadena += ' '
        nueva_cadena += cadena
    return nueva_cadena    

#print(repetir_cadena('Daokong',10))

