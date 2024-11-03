#CODIGO#

#diccionario = dict([('nombre','pitfall'),
 #                   ('edad',50),
  #                  ('dni', 2222222)])


# diccionario_dic = {

#     'nombre': 'mariano',
#     'edad': 23,
#     'dni' : 22222222


# diccionario = {}
# diccionario  ['nombre'] = 'pitfall'
# diccionario  ['edad'] = 34
# diccionario  ['dni'] = 2222222

# print(diccionario)
# print(f'nombre: {diccionario["nombre"]}')


# #metodo get()
# print(f"lala {diccionario.get('lala',999)}")

#modificacion/agregar
diccionario = dict([('nombre','pitfall'),
                   ('edad',50),
                   ('dni', 2222222)])

# diccionario['nombre'] = 'juan'

# #agregar
# diccionario['genero'] = 'trava'
# print(diccionario)

# 
#recorrer

# for elemento in diccionario:
#     print(f'{elemento} : {diccionario[elemento ]}')


#metodo values()

# valores = diccionario.values()
# print(valores)

# for elemento in diccionario:
#     print(elemento, end='-')

#metodo items()
# 
for clave, valor in diccionario.items():
    print(f'{clave.capitalize()} : {valor}')
    
    


