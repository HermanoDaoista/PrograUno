# 6.Ingresar un número. Determinar si el número es primo o no.

ingrese_numero = input('Ingrese un numero ')
ingrese_numero = int(ingrese_numero)
bandera_primo = 'Es primo'

for i in range (2 , ingrese_numero):

    resto = ingrese_numero % i

    if (resto == 0):
        bandera_primo = 'No es primo'
        break
       
        

print(bandera_primo)

