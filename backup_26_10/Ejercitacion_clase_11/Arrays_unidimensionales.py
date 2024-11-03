#ARRAYS UNIDIMENSIONALES
import operator
#1.Realizar una función que ordene una lista de enteros de forma ascendente (menor a mayor) , la misma debería devolver False en caso de que se ya se encuentre ordenada. True en caso contrario
#lista = [2,6,5,2,7,1]
#lista_a = [1,2,3,4,5]
def ordenar_lista_ascendente(lista: list) -> bool:
    """ordena una lista de enteros de mayor a menor 

    Args:
        lista (list): recibe una lista de enteros

    Returns:
        bool: devuelve False si ya esta ordenada True si no 
    """
    retorno = True
    for i in range(len(lista) - 1):
     for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
           auxiliar = lista[i]
           lista[i] = lista[j]
           lista[j] = auxiliar
           retorno = False
    return retorno   

#2.Realizar una función que ordene una lista de enteros de forma descendente (mayor a menor) , la misma debería devolver False en caso de que se ya se encuentre ordenada. True en caso contrario

def ordenar_lista_descendente(lista: list) -> bool:
    """Ordena una lista de enteros de mayor a menor

    Args:
        lista (list): recibe una lista de enteros

    Returns:
        bool: devuelve False si ya esta ordenada True en caso contrario
    """

    
    retorno = True
    for i in range(len(lista) - 1):
     for j in range(i+1, len(lista)):
        if lista[i] < lista[j]:
           auxiliar = lista[i]
           lista[i] = lista[j]
           lista[j] = auxiliar
           retorno = False
    return retorno   


#lista = [2,6,5,2,7,1] 
#lista = [3,2,1]

# respuesta = ordenar_lista_descendente(lista)
# print(lista)
# print(respuesta)

# 3.Realizar una función que ordene una lista de enteros en orden ascendente o descendente dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de intercambios que se realizaron.


def ordenar_lista_por_operador(lista: list, operador) -> int:
    """recibe una lista de nteros y los ordena de mayor a menor o viceversa

    Args:
        lista (list): recibe una lista de enteros
        operador (_type_): recibe como argumento la funcion operador.gt o operador.lt

    Returns:
        int: devuelve la cantidad de intercambios que se hicieron hasta lograr ordenar
    """
    contador = 0
    for i in range(len(lista) - 1):
     for j in range(i+1, len(lista)):
        if operador(lista[i], lista[j]):
           auxiliar = lista[i]
           lista[i] = lista[j]
           lista[j] = auxiliar
           contador += 1
    return contador


#lista = [2,6,5,2,7,1] 
#lista = [3,2,1]


# 4.Realizar una función que ordene una lista de nombres de la alfabéticamente (A-Z) o viceversa (Z-A) dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de cambios que se realizaron. 
# Investigar cómo comparar str alfabéticamente en python.

lista = ['pedro', 'juan', 'raul', 'arathot', 'zaratul', 'ayala']
def ordenar_lista_alfabeticamente(lista: list, operador) -> int:
    """ordena por orden alfabetica una lista de string

    Args:
        lista (list): recibe una lista de string
        operador (_type_): funcion operador.gt operador.lt

    Returns:
        int: devuelve la cantidad de intercambios hasta estar ordenada
    """
    contador = 0
    for i in range(len(lista) - 1):
     for j in range(i+1, len(lista)):
        if operador(lista[i], lista[j]):
           auxiliar = lista[i]
           lista[i] = lista[j]
           lista[j] = auxiliar
           contador = 0
    return contador



#5. Similar a la función anterior, se debe realizar otra que ordene una lista de nombres por su largo, de manera ascendente o descendente, la función debe retornar la cantidad de cambios que se realizaron.

def ordenar_lista_alfabeticamente(lista: list, operador) -> int:
    """ordena por orden de longitud una lista de string

    Args:
        lista (list): recibe una lista de string
        operador (_type_): funcion operador.gt operador.lt

    Returns:
        int: devuelve la cantidad de intercambios hasta estar ordenada
    """
    contador = 0
    for i in range(len(lista) - 1):
     for j in range(i+1, len(lista)):
        if operador(len(lista[i]), len(lista[j])):
           auxiliar = lista[i]
           lista[i] = lista[j]
           lista[j] = auxiliar
           contador = 0
    return contador
 

# respuesta = ordenar_lista_por_operador(lista , operator.lt)
# print(lista)
# print(respuesta) 
