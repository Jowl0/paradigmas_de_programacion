#=================================
#  Joel Reyes Garcia
#=================================
#  Paradigmas de programacion
#  Matematica Algoritmica
#  ESFM-IPN  IPN
#=================================


#====================
#   Uso de filtros
#====================

#============================================================
#   Hacer una lista de los numeros por arriba del promedio 
#============================================================

# Modulo de estadistica 
import statistics 

bigdata = [1.3,2.7,0.8,4.1,4.3,-0.1]
promedio = statistics.mean(bigdata)
print(promedio)

#========================================================================
#   Hazme una lista de elementos que cumplan la condicion x > promedio 
#   filtrer (condicion,datos)
#========================================================================
print(list(filter(lambda x : x > promedio, bigdata)))

#=======================
#   Limpiar los datos 
#=======================
paises = ["","Argentina","","Brasil","","Chile","Mexico","","Colombia","","","Cuba","Venezuela"]

#====================================
#   Filtra lo que no contiene nada 
#====================================
print(list(filter(None,paises)))
