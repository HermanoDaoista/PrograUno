


def get_int(mensaje: str, mensaje_error:str , minimo: int , maximo: int , numero_reintentos:int) -> int|None:
     reintentos = 1
     numero = input(mensaje)
     numero = int(numero)
     while numero < minimo or numero >  maximo:
         reintentos += 1
         numero = input(mensaje_error)
         numero = int(numero)
         if reintentos >= numero_reintentos:
             break
     return numero

resultado = get_int('Su numero: ' , 'error Su numero: ', 10 , 50 , 3)

def get_float(mensaje: str, mensaje_error:str , minimo: int , maximo: int , numero_reintentos:int) -> int|None:

     reintentos = 1
     numero = input(mensaje)
     numero = float(numero)
     while numero < minimo or numero >  maximo:
         reintentos += 1
         numero = input(mensaje_error)
         numero = float(numero)
         if reintentos >= numero_reintentos:
             break
     return numero

        
        
resultado = get_float('Su numero: ' , 'error Su numero: ', 10 , 50 , 3)


def get_string(palabra: str , caracteres: int , palabra_error: str , numero_reintentos : int) -> str| None: 
      palabra = input(palabra)
      palabra = str(palabra)
      contador = 1
      while len(palabra) != caracteres: 
            palabra = input(palabra_error)
            palabra = str(palabra)
            contador += 1
            if contador >= numero_reintentos:
                break
                      

resultado = get_string('Ingrese palabra: ' , 3 , 'error palabra: ' , 3)       