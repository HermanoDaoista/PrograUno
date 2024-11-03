

# TAREA: 
# Realizar una calculadora en donde se le pida al usuario una operación
# Validar (“+” , “-” , “/”, “*”) en caso de no ser ninguno de esos especificar error

# (+) -> Suma
# (-) -> Resta
# (/) -> Dividir
# (*) -> Multiplicar

# Luego de tener el operador, pedir dos números y hacer la operación correspondiente.



ingrese_una_operacion = input('Ingrese una operacion aritmetica: ')
while ingrese_una_operacion != '+' and ingrese_una_operacion != '-' and ingrese_una_operacion != '*' and ingrese_una_operacion != '/':
    ingrese_una_operacion = input('ERROR Ingrese una operacion aritmetica: ')

ingrese_numero_uno = int(input('Ingrese un numero: '))

ingrese_numero_dos = int(input('Ingrese un numero: '))

match ingrese_una_operacion:
    case '+':
        resultado = ingrese_numero_uno + ingrese_numero_dos
    case '-':
        resultado = ingrese_numero_uno - ingrese_numero_dos
    case '*':
        resultado = ingrese_numero_uno * ingrese_numero_dos
    case '/':
        if ingrese_numero_dos != 0:
            resultado = ingrese_numero_uno / ingrese_numero_dos
        else:
            resultado = 'No se puede dividir por 0'   


print(f'{ingrese_numero_uno} {ingrese_una_operacion} {ingrese_numero_dos} = {resultado}')                   