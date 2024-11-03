# 1. Realizar una función recursiva que calcule la suma de los primeros números naturales:

# def sumar_naturales (numero:int) -> int:

# 5 + 4 + 3 + 2 + 1 = 15


def sumar_naturales (numero:int) -> int:
    if numero == 1:
        return 1
    else:
        return sumar_naturales(numero -1) + numero
        

print(sumar_naturales(10))

# 2. Realizar una función recursiva que calcule la potencia de un número:

# def calcular_potencia (base:int , exponente:int) -> int:

def calcular_potencia (base:int , exponente:int) -> int:
    if exponente == 1:
        return base
    else:
        return calcular_potencia(base , exponente -1) * base
        
    
print(calcular_potencia(2 , 5))

# 3. Realizar una función para calcular el número de Fibonacci (investigar que es) de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

# 	def calcular_fibonacci (numero:int) -> int:

def calcular_fibonacci (numero:int) -> int:
    if numero == 0:
        return 0
    else:
        if numero == 1:
            return 1
        else:
            return calcular_fibonacci(numero -1) + calcular_fibonacci(numero - 2)
            

print(calcular_fibonacci(8))

# Ejercitación Clase 5 (Funciones Avanzado)


# 1. Desarrollar una función que verifique el DNI de una persona, la misma recibirá un str (se asume que solamente contiene caracteres numéricos). Si la cantidad de caracteres es menor a 6 o mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True

# Para saber la cantidad de elementos de un str usamos la función len()

def verificar_dni(numero : str) -> bool:
    if len(numero) > 8 or len(numero) < 6:
        return False
    else:
        return True
    
print(verificar_dni('111111'))

# 2. Desarrollar una función que complete el número de DNI de una persona. Recibirá un str (se asume que solamente contiene caracteres numéricos), deberá medirla (len) y completar con ceros a la izquierda hasta llegar a un total de 8 caracteres, y devolviendo la cadena resultante. 
# En caso de que el dni sea invalido (que no tiene entre 6 y 8 caracteres) devolvera una cadena que dice : “DNI INVALIDO”

# Ej: Se ingresa “12345”, y devolverá “DNI INVALIDO”.
# Ej: Se ingresa “123456”, y devolverá “00123456”.
# Ej: Se ingresa “1234567”, y devolverá “01234567”.
# Ej: Se ingresa “12345678”, y devolverá “12345678”.
# Ej: Se ingresa “123456789”, y devolverá “DNI INVALIDO”.

# Nota: Reutilizar la función del ejercicio 1 para validar si el dni es válido

def autocompletar_dni(numero : str) -> str:
    if verificar_dni(numero) == False:
        mensaje = 'DNI INVALIDO'
    else:
        if len(numero) == 6:
            mensaje = '00' + numero
        else:
            if len(numero) == 7:
                mensaje = '0' + numero
            else:
                mensaje = numero
    return mensaje

print(autocompletar_dni('298000000000230'))                    