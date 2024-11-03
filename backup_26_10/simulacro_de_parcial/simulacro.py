"""tuki"""

#tuki-tuki
#10 bailarines 

from funciones import *
import operator

I_JURADO_UNO = 0
I_JURADO_DOS = 1
I_JURADO_TRES = 2
I_PROMEDIO = 3

bailando = inicializar_matriz(2,4,0)

cargar_bailando(bailando)
#mostrar notas
bailando =[[9,6,3,3],
           [4,8,1,4],
           [5,5,6,6],
           [6,6,8,6]]

encabezado = ['Nro de participante  ', 'Nota Jurado 1  ', 'Nota Jurado 2  ','Nota Jurado 3  ','Nota promedio  ']
imprimir_encabezado(encabezado)
print('')
mostrar_matriz(bailando)


#ordenar bailarines jurados dos

mayor_nota_jurado_dos = ordenar_por_numero(bailando,operator.lt,I_JURADO_DOS)

mostrar_matriz(mayor_nota_jurado_dos)

#la gran siete 

encontar_gran_coincidencia(bailando,7,3)

#jurado malo menor a 4

aplazados = encontrar_aplazados(bailando,4,I_JURADO_TRES)
mostrar_matriz(aplazados)

#Muestro el top 3 ordeno de mayor a menor en la fila promedio y luego imprimo los tres primeros

top_tres_promedios = ordenar_por_numero(bailando, operator.lt, I_PROMEDIO)

imprimir_por_filas(top_tres_promedios, 3)






