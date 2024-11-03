# Para un hospital veterinario

# Es necesario registrar el ingreso de las mascotas en la próxima hora (solo se pueden atender 20 mascotas), para esto hay que considerar los siguientes datos y encasillarlos en ciertos 
# diagnósticos para poder derivarlos adecuadamente:

# -Edad (Validar entre 1 y 25 años) 

# -Tipo: (Validar “gato”, “perro”, “loro”) 

# -Peso: (Más de 0 kg) -

# -Diagnóstico: (Validar “problemas digestivos”, “parásitos”, “infección”)

# -Vacuna antirrábica (validar “si”, ”no”)

# CALCULAR

# 1. Cantidad de mascotas sin vacuna antirrábica, cuya edad está entre los 4 y 12 años, que se presentaron por infección o parásitos.

# 2. El tipo de mascota más ingresada con problemas digestivos.

# 3. Edad y tipo de la mascota más vieja con vacuna antirrábica.

# 4. Porcentaje de mascotas vacunadas y no vacunadas.

# 5. Promedio de edad de los gatos.

'Rogelio Selim Ayala Div 313 TN'

contador_punto_uno = 0
bandera_mas_vieja = 0
contador_gato = 0
contador_loro = 0
contador_perro = 0
contador_sin_vacuna = 0
contador_con_vacuna = 0
contador_gato_dos = 0
acumulador_edad_gatos = 0
bandera_digestivos = True
for i in range (2):

    ingrese_edad = input('Ingrese la edad de la mascota: ')
    ingrese_edad = int(ingrese_edad)
    while ingrese_edad < 1 or ingrese_edad > 25:
        ingrese_edad = input('Ingrese un numero entre 1 y 25: ')
        ingrese_edad = int(ingrese_edad)
    
    ingrese_tipo = input('Ingrese tipo de mascota: ')
    while ingrese_tipo != 'gato' and ingrese_tipo != 'perro' and ingrese_tipo != 'loro':
        ingrese_tipo = input('ERROR escoja entre gato o perro o loro: ')

    ingrese_peso = input('Ingrese el peso: ') 
    ingrese_peso = int(ingrese_peso) 
    while ingrese_peso < 1:
        ingrese_peso = input('ERROR El peso debe ser superior a 0: ') 
        ingrese_peso = int(ingrese_peso)

    ingrese_diagnostico = input('Ingrese diagnostico: ')
    while ingrese_diagnostico !=  'problemas digestivos' and ingrese_diagnostico != 'parasitos' and ingrese_diagnostico != 'infeccion':
        ingrese_diagnostico = input('ERROR Ingrese solo - problemas digestivos o parasitos o infeccion: ')

    vacuna_antirrabica = input('Vacuna antirrabica S/N: ')
    while vacuna_antirrabica != 'S' and vacuna_antirrabica != 'N':
        vacuna_antirrabica = input('ERROR Vacuna antirrabica escoja por S/N: ')

    #1. Cantidad de mascotas sin vacuna antirrábica, cuya edad está entre los 4 y 12 años, que se presentaron por infección o parásitos.
    if vacuna_antirrabica == 'N':
        contador_sin_vacuna += 1
        if ingrese_edad > 3 and ingrese_edad < 13:
            if ingrese_diagnostico != 'problemas digestivos':
                contador_punto_uno += 1
    # 2. El tipo de mascota más ingresada con problemas digestivos.
    if ingrese_diagnostico == 'problemas digestivos':
        bandera_digestivos = False
        match ingrese_tipo:
            case 'gato':
                contador_gato += 1
            case 'loro':
                contador_loro += 1
            case 'perro':
                contador_perro += 1    
    if contador_gato > contador_loro and contador_gato > contador_perro :
            mascota_mas_ingresada = 'gato'
    else:
        if contador_loro > contador_gato and contador_loro > contador_perro :
            mascota_mas_ingresada = 'loro' 
        else:
            mascota_mas_ingresada = 'perro'
    # 3. Edad y tipo de la mascota más vieja con vacuna antirrábica.
    if vacuna_antirrabica == 'S':
        contador_con_vacuna += 1
        if bandera_mas_vieja == 0:
            edad_mascota_vieja = ingrese_edad
            tipo_mascota_vieja = ingrese_tipo
            bandera_mas_vieja = 1
        else:
            if ingrese_edad > edad_mascota_vieja:
                    edad_mascota_vieja = ingrese_edad
                    tipo_mascota_vieja = ingrese_tipo

    # 5. Promedio de edad de los gatos.    
    if ingrese_tipo == 'gato':
        contador_gato_dos += 1
        acumulador_edad_gatos += ingrese_edad

#4. Porcentaje de mascotas vacunadas y no vacunadas.

porcentaje_de_vacunados = (contador_con_vacuna * 100) / (i+1)
   
porcentaje_no_vacunados = (contador_sin_vacuna *100) / (i+1)

if contador_gato_dos >=1:
    
    promedio_edad_gatos = acumulador_edad_gatos / contador_gato_dos

if contador_punto_uno >= 1:
    print(f'La cantidad del punto uno es: {contador_punto_uno}')
else:
    print('No se cumplen las condiciones del punto uno')
if bandera_digestivos == False:
    print(f'El tipo mas ingresados con problemas digestivos es: {mascota_mas_ingresada}')
else:
    print('No hay mascotas con problemas digestivos')
if bandera_mas_vieja == 1:        
    print(f'La mascota mas vieja c/antirrabica tiene: {edad_mascota_vieja} y pertenece al tipo {tipo_mascota_vieja}')
else:
    print('No hay mascotas con antirrabica')
if contador_con_vacuna >= 1:         
    print(f'Existen un {porcentaje_de_vacunados} % de animales c/vacuna')
else:
    print('No hay mascotas con vacuna')

if contador_sin_vacuna >=1:
    print(f'Existen un {porcentaje_no_vacunados} % de animales s/vacuna')
else:
    print('No hay mascotas sin vacuna')            
if contador_gato_dos >=1:
    print(f'El promedio de edades de gatos es: {promedio_edad_gatos}') 
else:
    print('No hay gatos')    
    

            