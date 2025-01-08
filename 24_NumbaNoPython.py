#=================================
#  Joel Reyes Garcia
#=================================
#  Paradigmas de programacion
#  Matematica Algoritmica
#  ESFM-IPN  IPN
#=================================

#==================================
#   Importar numba, numpy y time 
#==================================
from numba import jit 
import numpy 
import time 

#====================================
#   Loop cualquiera en python puro
#====================================
def lento(a):
    t = 0.0 
    # Para cada renglon 
    for i in range (a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a + t

#=========================
#   Loop sin interprete 
#=========================
@jit(nopython = True) 
def rapido(a):
    t = 0.0
    # Para cada renglon
    for i in range (a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a + t

#================================================
#   Arreglo unidemensional lleno del 1 al 1000
#   Convertido en matriz de 100x100
#================================================
x = numpy.arange(10000).reshape(100,100)

#=======================================================
#   La primera llama incluye el timepo de compilacion 
#=======================================================
start = time.time()
rapido(x)
end = time.time()
print("Tiempo incluyendo compilacion = %s" %(end-start))

#=======================================================
#   La segunda es para obtener el tiempo de ejecucion 
#=======================================================
start = time.time()
rapido(x)
end = time.time()
print("Tiempo de ejecucion usando numba %s" %(end-start))

#===============================================
#   Tiempo sin de la funcion sin optimizacion
#===============================================
start = time.time()
lento(x)
end = time.time()
print("Tiempo de ejecucion en python puro = %s" %(end -start))
