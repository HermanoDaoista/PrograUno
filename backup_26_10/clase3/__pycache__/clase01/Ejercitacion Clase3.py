# Ejercitación Clase 3 (Funciones)

# 1.Crear una función que reciba dos números (acumulador y contador) y calcule el promedio, en caso de que haya división por cero imprimir un mensaje de error y retornar 0.

def calcular_promedio(acumulador , contador):
    if contador != 0:
        promedio = acumulador / contador
        return promedio
    else:
        promedio = print(f'Error Division por 0')
        return 0 
promedio = calcular_promedio (10 , 0)  

print(promedio)

# 2.Crear una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.

def calcular_area_rectangulo(largo , ancho):
    area = largo * ancho
    return area

area_rectangulo = calcular_area_rectangulo(5 , 5)

print(area_rectangulo)

    

# 3.Crear una función que verifique si un número es par o no, devuelve True si es par, y False si es impar

def determinar_par_o_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(determinar_par_o_impar(120))    


# 4.Crear una función que verifique si un primo o no, devuelve True si es primo, False si no lo es

def calcular_numero_primo(numero):
    for i in range (2 , numero):

        resto = numero % i

        if (resto == 0):
            return False
            break
        else:
            return True

print(calcular_numero_primo(11))        

# 5.Crear una función qué encuentre el máximo entre tres números. Debe aceptar tres argumentos y retornar el número más grande.

def calcular_el_maximo(numero_uno , numero_dos , numero_tres):
    if numero_uno > numero_dos and numero_uno > numero_tres:
        return numero_uno
    else:
        if  numero_dos > numero_tres:
            return numero_dos
        else:
            return numero_tres
        
print(calcular_el_maximo(numero_uno=250 , numero_dos=10 , numero_tres=20))        

# 6.Crear una función qué encuentre el mínimo entre tres números. Debe aceptar tres argumentos y retornar el número más chico.

def calcular_el_minimo(numero_uno , numero_dos , numero_tres):
    if numero_uno < numero_dos and numero_uno < numero_tres:
        return numero_uno
    else:
        if  numero_dos < numero_tres:
            return numero_dos
        else:
            return numero_tres
        
print(calcular_el_minimo(numero_uno=3 , numero_dos=100 , numero_tres=20))         

# 7. Crear una función qué se encargue de dividir dos números, la misma debe recibir como parámetro dos números y retornar el resultado. Validar división por cero.

def division_dos_numeros(numero_uno , numero_dos) -> float:
    if numero_dos != 0:
        division = numero_uno / numero_dos
        return division
    else:
        return 'Error division por 0'
    
division = division_dos_numeros(10 , 0)
print(division)    

# 8. Crear una función qué se encargue de multiplicar dos números, la misma debe recibir como parámetro dos números y retornar el resultado.

def multiplicar_dos_numeros(numero_uno , numero_dos):
 multiplicacion = numero_uno * numero_dos
 return multiplicacion

multiplicacion = multiplicar_dos_numeros(1 , 40)
print(multiplicacion)






# TAREA. 

# Realizar una función que me permita sumar dos números de las cuatro maneras siguientes.

# Una función sumar1 que reciba dos números y retorne el resultado
# Una función sumar2 que reciba dos números y no retorne nada (o sea que la función se encargue de mostrar el resultado)
# Una función sumar3 que no reciba nada y se encargue de pedir dos números y retornar el resultado
# Una función sumar4 que no reciba nada y no retorne nada, por ende se va encargar de pedir los numeros y de mostrar el resultado.
