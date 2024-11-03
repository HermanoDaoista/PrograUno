#####################
import random
###### ########## #######

# def sumar_numeros():
#     un_numero = int(input('Ingrese un numero: '))
#     otro_numero = int(input('Ingrese un numero: '))
#     suma = un_numero + otro_numero

#     print(f'La suma es {suma}')

#     ####################
# sumar_numeros()
    


# def sumar_numeros_1():
#     un_numero = int(input('Ingrese un numero: '))
#     otro_numero = int(input('Ingrese un numero: '))
#     suma = un_numero + otro_numero
#     return suma

# resultado = sumar_numeros_1()

# print(f'la suma es: {resultado}')


# def sumar_numeros_2(un_numero , otro_numero):
#      suma = un_numero + otro_numero
#      print(f'La suma es: {suma}')

# # ######################################

# # un_numero = int(input('Ingrese un numero: '))
# # otro_numero = int(input('Ingrese un numero: ')) 
# # sumar_numeros_2(un_numero , otro_numero) 
# # 
# # 
# #   
# numero_uno = random.randint(1, 10)
# numero_dos = random.randint(15, 300)

# sumar_numeros_2(numero_uno , numero_dos)

def sumar_numeros_4(un_numero , otro_numero):
    suma = un_numero + otro_numero
    return suma 

numero_uno = random.randint(1, 10)
numero_dos = random.randint(15, 300)
numero_tres = random.randint(1, 10)
numero_cuatro = random.randint(15, 300)

jugada_pitfall = sumar_numeros_4(numero_uno , numero_dos)
jugada_daoista = sumar_numeros_4(numero_tres , numero_cuatro)

if jugada_daoista > jugada_pitfall:
    print(f'Gano Dao con {jugada_daoista} contra {jugada_pitfall}')
else:
    if jugada_daoista < jugada_pitfall:
        print(f'Gano Pit con {jugada_pitfall} contra {jugada_daoista}')
    else:
        print('Empate')        

