#Clase Funciones con Mariano Fernandez

# def calcular_precio_con_iva():
#     print('Hola') 

# calcular_precio_con_iva()

# def calcular_precio_con_iva(valor_sin_iva , iva= 21):
#     print(f'parametro requerido: {valor_sin_iva}')
#     print(f'Parametro opcional: {iva}')


# calcular_precio_con_iva(100 , 10 )    

def calcular_precio_con_iva(valor_sin_iva : float , iva : float = 21) -> float:
    '''
    Que hace- Calcula el precio con iva
    Que recibe- recibe precio sin iva y el porcentaje iva (opcional)
    Que retorna- devuelve el precion con el iva calculado 
    '''
    resultado = valor_sin_iva * (1 + (iva /100)) #Proceso #Resultado es variable local
    return resultado #Salida
precio_con_iva = calcular_precio_con_iva(1000)
print(precio_con_iva)
