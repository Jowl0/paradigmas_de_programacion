#=================================
#  Joel Reyes Garcia
#=================================
#  Paradigmas de programacion
#  Matematica Algoritmica
#  ESFM-IPN  IPN
#=================================

#==============================================
#   Uso de reducciones (colapsar resultados)
#==============================================

#=====================================================
#   Multiplicacion de todos los numeros de la lista 
#=====================================================

from functools import reduce 

bigdata = [2,3,5,7,11,13,17,19,23,29 ]

#=================
#   Funcion x*Y
#=================
multiplicar = lambda x,y : x*y
suma = lambda x,y : x+y 

print (reduce(multiplicar,bigdata))
print (reduce(suma,bigdata))

#==============================================================
#   Reduce le aplica la funcion por pares a los resultados y
#   el siguiente elemento comenzando con los primeros 
#   elementos 
#==============================================================
