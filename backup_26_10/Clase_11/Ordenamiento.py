'''Clase 11(o 10)'''#22/27 parcial de octubre-17simulacro

'''ORDENAMIENTO'''

matriz = [['pepe',1111,5],
         ['juan',2111,2],
         ['martin',1122,3],
         ['flor',1113,6],
         ['brat',1115,8]]

lista = [1,60,3,7,10,10]
lista_ordenada = [1,3,33,71,100,101]

'''Ordenamiento por burbujeo'''
# print('despues')
# print(lista)
#menor a mayor
# for i in range(len(lista)-1):

#     for j in range(i+1,len(lista)):
#         numero_izquierda = lista[i]
#         numero_derecha = lista[j]
#         if numero_izquierda > numero_derecha:   https://onlinegdb.com/gbKz2oNAi->profe
#             lista[i] = numero_derecha
#             lista[j] = numero_izquierda

        
# for i in range(len(lista)-1):
#     for j in range(i+1,len(lista)):
#         if lista[i] > lista[j]:
#             aux_izq = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux_izq
# print('antes')
# print(lista)
            
# '''Con matrices'''
# print('antes')
# print(matriz)

# for fil_i in range(len(matriz)-1):
#     for fil_j in range(fil_i+1,len(matriz)):
#         if matriz[fil_i][2] < matriz[fil_j][2]:
#             auxiliar = matriz[fil_i]
#             matriz[fil_i] = matriz[fil_j]
#             matriz[fil_j] = auxiliar




# print('despues')
# print(matriz)

def comprobar_orden(lista:list)-> bool:
    retorno = True
    for i in range(len(lista)-1):
     for j in range(i+1,len(lista)):
         if lista[i] > lista[j]:
             aux_izq = lista[i]
             lista[i] = lista[j]
             lista[j] = aux_izq  
             retorno = False
    return retorno         
print(comprobar_orden(lista))    

#https://www.onlinegdb.com/9ivShIrr- gdb cadenas

4
            
     














