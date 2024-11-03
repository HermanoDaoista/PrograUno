# La división de higiene está trabajando en un control de stock para productos sanitarios. 
# Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos: 
# 1. El tipo (validar "barbijo", "jabón" o "alcohol") 
# 2. El precio: (validar entre 100 y 300) 
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades) 
# 4. La marca y el Fabricante. 

# Se debe informar lo siguiente: 
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante. 
# B. Del ítem con más unidades, el fabricante. 
# C. Cuántas unidades de jabones hay en total.
'Rogelio Ayala Div 313 TN'

bandera_barbijo = 0
bandera_mas_unidades = 0
acumulador_jabones = 0
unidades_barbijo = 0
for i in range (5):

     ingrese_tipo = input('Escoja una opcion barbijo-jabon-alcohol:  ')

     while ingrese_tipo != 'barbijo' and ingrese_tipo != 'jabon' and ingrese_tipo != 'alcohol':
          
           ingrese_tipo = input('ERROR INGRESE SOLO : barbijo o jabon o alcohol:  ')

     ingrese_precio = input(' Ingrese Precio $ ')
     ingrese_precio = int(ingrese_precio)  
     while ingrese_precio < 100 or ingrese_precio > 300:    
           ingrese_precio = input('ERROR  Ingrese un valor entre 100 y 300:  ')
           ingrese_precio = int(ingrese_precio) 

     ingrese_unidades = input('Ingrese la cantidad:  ')       
     ingrese_unidades = int(ingrese_unidades)
     while ingrese_unidades <= 0 or ingrese_unidades > 1000:   
        ingrese_unidades = input('ERROR Ingrese de 1 a 1000 unidades:  ')       
        ingrese_unidades = int(ingrese_unidades)

     ingrese_marca = input('Ingrese la marca: ')
     ingrese_fabricante = input('Ingrese Fabricante: ') 
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante. 
     if ingrese_tipo == 'barbijo':
          if bandera_barbijo == 0:
            barbijo_mas_caro = ingrese_precio  
            unidades_barbijo = ingrese_unidades
            fabricante_barbijo = ingrese_fabricante
            bandera_barbijo = 1 
          else:
               if bandera_barbijo == 1 or ingrese_unidades > unidades_barbijo:
                    bandera_barbijo == 0
                    barbijo_mas_caro = ingrese_precio 
                    unidades_barbijo = ingrese_unidades
                    fabricante_barbijo = ingrese_fabricante     
# B. Del ítem con más unidades, el fabricante. 
    
     if bandera_mas_unidades == 0:
          items_mas_unidades = ingrese_unidades
          fabricante_mas_unidades = ingrese_fabricante
          bandera_barbijo = 1
     else: 
          if ingrese_unidades > items_mas_unidades:
                items_mas_unidades = ingrese_unidades
                fabricante_mas_unidades = ingrese_fabricante

# C. Cuántas unidades de jabones hay en total.

     if ingrese_tipo == 'jabon':
           acumulador_jabones += ingrese_unidades


#INFORMES
if unidades_barbijo > 0:
    print(f'El mas caro de los barbijos costo: {barbijo_mas_caro} y son un total de {unidades_barbijo} y lo fabrica {fabricante_barbijo}')
else: 
     print('No se vendieron barbijos')
if acumulador_jabones > 0:
     print(f'usted tiene un total de {acumulador_jabones} de jabones')
else:
     print('No hay jabones') 

print(f'El fabricante con mas items es {fabricante_mas_unidades} con {items_mas_unidades} de unidades')            